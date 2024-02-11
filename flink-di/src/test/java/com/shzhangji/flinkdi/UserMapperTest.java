package com.shzhangji.flinkdi;

import java.util.Date;
import java.util.Optional;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

public class UserMapperTest {
  @Test
  public void testMap() throws Exception {
    var userRepository = mock(UserRepository.class);
    when(userRepository.getById(1L))
        .thenReturn(Optional.of(new User(1L, "jizhang", new Date())));

    var userMapper = new UserMapper();
    userMapper.userRepository = userRepository;
    assertEquals("jizhang", userMapper.map(1L).getUsername());
  }
}
