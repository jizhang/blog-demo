# -*- coding: utf-8 -*-

from __future__ import print_function
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


class Print(beam.PTransform):
    def expand(self, pcoll):
        return pcoll | beam.ParDo(print)


class SplitFn(beam.DoFn):
    def process(self, element):
        return element.split(' ')


class SplitAndPairWithOneFn(beam.DoFn):
    def process(self, element):
        for word in element.split(' '):
            yield (word, 1)


with beam.Pipeline(options=PipelineOptions()) as p:
    lines = p | 'Create' >> beam.Create(['cat dog', 'snake cat', 'dog'])
    lines | beam.ParDo(SplitAndPairWithOneFn()) | Print()
