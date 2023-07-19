package com.shzhangji.demo.commandline.differentpackage;

import com.shzhangji.demo.commandline.common.UserService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;


// @SpringBootApplication
// @Import(UserService.class)
@SpringBootApplication(scanBasePackages = {
    "com.shzhangji.demo.commandline.common",
    "com.shzhangji.demo.commandline.differentpackage",
})
@Slf4j
@RequiredArgsConstructor
public class JobDifferentPackage implements CommandLineRunner {
  private final UserService userService;

  public static void main(String[] args) {
    SpringApplication.run(JobDifferentPackage.class, args);
  }

  @Override
  public void run(String... args) {
    log.info("Run JobDifferentPackage");
  }
}
