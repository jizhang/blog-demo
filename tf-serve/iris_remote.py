# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow_serving.apis import classification_pb2
from tensorflow_serving.apis import regression_pb2
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2
from grpc.beta import implementations
import common

channel = implementations.insecure_channel('127.0.0.1', 9000)
stub = prediction_service_pb2.beta_create_PredictionService_stub(channel)

inputs = common.get_test_inputs()
examples = []
for index, row in inputs.iterrows():
    example = tf.train.Example()
    for col, value in row.iteritems():
        example.features.feature[col].float_list.value.append(value)
    examples.append(example)

request = classification_pb2.ClassificationRequest()
request.model_spec.name = 'default'
request.input.example_list.examples.extend(examples)

response = stub.Classify(request, 10.0)

outputs = inputs.copy()
for index, row in outputs.iterrows():
    max_class = max(response.result.classifications[index].classes, key=lambda c: c.score)
    outputs.loc[index, 'ClassId'] = max_class.label
    outputs.loc[index, 'Probability'] = max_class.score
print(outputs)
