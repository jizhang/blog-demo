FROM flink:1.8.1-scala_2.12

ARG hadoop_jar
ARG job_jar

ENV FLINK_CONF=$FLINK_HOME/conf/flink-conf.yaml

RUN set -x && \
  sed -i -e "s/jobmanager\.heap\.size:.*/jobmanager.heap.size: 128m/g" $FLINK_CONF && \
  sed -i -e "s/taskmanager\.heap\.size:.*/taskmanager.heap.size: 256m/g" $FLINK_CONF

COPY --chown=flink:flink $hadoop_jar $job_jar $FLINK_HOME/lib/

USER flink
