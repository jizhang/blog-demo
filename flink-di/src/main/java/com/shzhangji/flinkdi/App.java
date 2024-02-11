package com.shzhangji.flinkdi;

import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.datastream.DataStreamSource;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;

public class App {
  public static void main(String[] args) throws Exception {
    var env = StreamExecutionEnvironment.getExecutionEnvironment();
    env.setParallelism(1);
    env.disableOperatorChaining();

    DataStreamSource<Long> source = env.fromElements(1L);
    DataStream<User> users = source.map(new UserMapper());
    users.print();

    env.execute();
  }
}
