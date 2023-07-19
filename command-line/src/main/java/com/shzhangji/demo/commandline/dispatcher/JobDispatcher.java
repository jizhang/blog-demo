package com.shzhangji.demo.commandline.dispatcher;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.config.AutowireCapableBeanFactory;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.stereotype.Component;

@Slf4j
@Component
@RequiredArgsConstructor
public class JobDispatcher implements ApplicationRunner {
  private final AutowireCapableBeanFactory factory;

  @Override
  public void run(ApplicationArguments args) throws Exception {
    var jobArgs = args.getOptionValues("job");
    if (jobArgs == null || jobArgs.size() != 1) {
      throw new IllegalArgumentException("Invalid argument --job");
    }

    var jobClass = Class.forName("com.shzhangji.demo.commandline.dispatcher." + jobArgs.get(0));
    var job = (Runnable) factory.createBean(jobClass);
    job.run();
  }
}
