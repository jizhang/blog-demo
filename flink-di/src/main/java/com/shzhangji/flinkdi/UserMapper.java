package com.shzhangji.flinkdi;

import jakarta.inject.Inject;
import java.util.Objects;
import org.apache.flink.api.common.functions.RichMapFunction;
import org.apache.flink.configuration.Configuration;

public class UserMapper extends RichMapFunction<Long, User> {
  @Inject
  UserRepository userRepository;

  @Override
  public void open(Configuration parameters) throws Exception {
    AppInjector.injectMembers(this);
  }

  @Override
  public User map(Long userId) throws Exception {
    Objects.requireNonNull(userId, "User ID is null");
    return userRepository.getById(userId).orElseThrow(() -> new RuntimeException("User not found"));
  }
}
