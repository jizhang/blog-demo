package com.shzhangji.demo.commandline.dispatcher;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.context.ApplicationContext;

@Slf4j
@RequiredArgsConstructor
public class JobDispatcherA implements Runnable {
  private final ApplicationContext context;

  @Override
  public void run() {
    log.info("Run JobDispatcherA in application context {}", context);
  }
}
