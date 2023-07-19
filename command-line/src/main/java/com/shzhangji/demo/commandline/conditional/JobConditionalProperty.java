package com.shzhangji.demo.commandline.conditional;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.autoconfigure.condition.ConditionalOnProperty;
import org.springframework.stereotype.Component;

@Slf4j
@Component
@RequiredArgsConstructor
@ConditionalOnProperty(name = "job", havingValue = "JobConditionalProperty")
public class JobConditionalProperty implements CommandLineRunner {
  @Override
  public void run(String... args) {
    log.info("Run JobConditionalProperty");
  }
}
