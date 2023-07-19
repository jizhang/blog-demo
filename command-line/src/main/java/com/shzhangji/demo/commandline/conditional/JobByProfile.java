package com.shzhangji.demo.commandline.conditional;

import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Profile;
import org.springframework.stereotype.Component;

@Slf4j
@Component
@Profile("JobByProfile")
public class JobByProfile implements CommandLineRunner {
  @Override
  public void run(String... args) throws Exception {
    log.info("Run JobByProfile");
  }
}
