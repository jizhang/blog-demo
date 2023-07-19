# -*- coding: utf-8 -*-

from __future__ import print_function
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


with beam.Pipeline(options=PipelineOptions()) as p:
    lines = p | 'Create' >> beam.Create(['cat dog', 'snake cat', 'dog'])

    counts = (
        lines
        | 'Split' >> (beam.FlatMap(lambda x: x.split(' '))
                      .with_output_types(unicode))
        | 'PairWithOne' >> beam.Map(lambda x: (x, 1))
        | 'GroupAndSum' >> beam.CombinePerKey(sum)
    )

    counts | 'Print' >> beam.ParDo(lambda (w, c): print('%s: %s' % (w, c)))
