package com.shzhangji.apiauth;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

class DemoApplicationTest {
  @Test
  void testGeneratePassword() {
    var encoder = new BCryptPasswordEncoder();
    var password = encoder.encode("888888");
    Assertions.assertTrue(encoder.matches("888888", password));
    System.out.println("{bcrypt}" + password);
  }
}
