# -*- coding: utf-8 -*-

import pandas as pd
import tensorflow as tf

COLUMN_NAMES = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']
SPECIES = ['Setosa', 'Versicolor', 'Virginica']
BATCH_SIZE = 100
STEPS = 1000

# load data
y_name = 'Species'

train = pd.read_csv('data/iris_training.csv', names=COLUMN_NAMES, header=0)
train_x, train_y = train, train.pop(y_name)

test = pd.read_csv('data/iris_test.csv', names=COLUMN_NAMES, header=0)
test_x, test_y = test, test.pop(y_name)

# prepare input / eval fn
def train_input_fn(features, labels, batch_size):
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))
    dataset = dataset.shuffle(1000).repeat().batch(batch_size)
    return dataset

def eval_input_fn(features, labels, batch_size):
    features = dict(features)
    inputs = (features, labels) if labels is not None else features
    dataset = tf.data.Dataset.from_tensor_slices(inputs)
    dataset = dataset.batch(batch_size)
    return dataset

# create classifier

# feature columns
# [
#     _NumericColumn(key='SepalLength', shape=(1,), default_value=None, dtype=tf.float32, normalizer_fn=None),
#     _NumericColumn(key='SepalWidth', shape=(1,), default_value=None, dtype=tf.float32, normalizer_fn=None),
#     _NumericColumn(key='PetalLength', shape=(1,), default_value=None, dtype=tf.float32, normalizer_fn=None),
#     _NumericColumn(key='PetalWidth', shape=(1,), default_value=None, dtype=tf.float32, normalizer_fn=None)
# ]
feature_columns = [tf.feature_column.numeric_column(key=key)
                   for key in train_x.keys()]

classifier = tf.estimator.DNNClassifier(
    feature_columns=feature_columns,
    hidden_units=[10, 10],
    n_classes=3)

classifier.train(
    input_fn=lambda: train_input_fn(train_x, train_y, batch_size=BATCH_SIZE),
    steps=STEPS)

# evaluate
eval_result = classifier.evaluate(
    input_fn=lambda: eval_input_fn(test_x, test_y, batch_size=BATCH_SIZE))

print('Test set accuracy: {accuracy:0.3f}'.format(**eval_result))

# predict
expected = ['Setosa', 'Versicolor', 'Virginica']
predict_x = {
    'SepalLength': [5.1, 5.9, 6.9],
    'SepalWidth': [3.3, 3.0, 3.1],
    'PetalLength': [1.7, 4.2, 5.4],
    'PetalWidth': [0.5, 1.5, 2.1],
}

predictions = classifier.predict(
    input_fn=lambda: eval_input_fn(predict_x, labels=None, batch_size=BATCH_SIZE))

for prediction, expect in zip(predictions, expected):
    class_id = prediction['class_ids'][0]
    probability = prediction['probabilities'][class_id]
    print('Prediction is "{}" ({:.1f}%), expected "{}"'.format(
        SPECIES[class_id], 100 * probability, expect))

# export model

# feature specification
# {
#     'SepalLength': FixedLenFeature(shape=(1,), dtype=tf.float32, default_value=None),
#     'SepalWidth': FixedLenFeature(shape=(1,), dtype=tf.float32, default_value=None),
#     'PetalLength': FixedLenFeature(shape=(1,), dtype=tf.float32, default_value=None),
#     'PetalWidth': FixedLenFeature(shape=(1,), dtype=tf.float32, default_value=None)
# }
feature_spec = tf.feature_column.make_parse_example_spec(feature_columns)
serving_input_receiver_fn = tf.estimator.export.build_parsing_serving_input_receiver_fn(feature_spec)
export_dir = classifier.export_savedmodel('export', serving_input_receiver_fn)
print('Exported to {}'.format(export_dir))
