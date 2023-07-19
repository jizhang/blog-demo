# -*- coding: utf-8 -*-

import os
import pandas as pd
import tensorflow as tf
import common

# load model
export_dir = common.get_export_dir()
predict_fn = tf.contrib.predictor.from_saved_model(export_dir)

# prepare test features
inputs = common.get_test_inputs()
examples = common.create_examples(inputs)

# predict
predictions = predict_fn({'inputs': examples})

print(common.assemble_result(inputs, predictions))
