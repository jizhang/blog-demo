package com.shzhangji.apiauth.repository;

import com.shzhangji.apiauth.entity.User;
import java.util.Optional;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface UserRepository extends CrudRepository<User, Integer> {
  Optional<User> findByUsername(String username);
}

