package com.shzhangji.flinkdi;

import java.util.Optional;

public interface UserRepository {
  Optional<User> getById(long id);
}
