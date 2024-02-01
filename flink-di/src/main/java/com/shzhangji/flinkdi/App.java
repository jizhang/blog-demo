package com.shzhangji.flinkdi;

import java.util.List;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;

public class App {
  public static void main(String[] args) throws Exception {
    var env = StreamExecutionEnvironment.getExecutionEnvironment();
    env.setParallelism(1);

    var source = env.fromCollection(List.of(1L));
    source.map(new UserMapper()).print();

    env.execute();
  }
}
