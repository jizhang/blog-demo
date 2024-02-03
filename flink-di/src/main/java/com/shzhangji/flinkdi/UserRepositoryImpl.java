package com.shzhangji.flinkdi;

import com.google.inject.Inject;
import java.sql.SQLException;
import java.util.Optional;
import javax.sql.DataSource;

public class UserRepositoryImpl implements UserRepository {
  private DataSource dataSource;

  @Inject
  public UserRepositoryImpl(DataSource dataSource) {
    this.dataSource = dataSource;
  }

  @Override
  public Optional<User> getById(long id) {
    try (var conn = dataSource.getConnection()) {
      var stmt = conn.prepareStatement("SELECT username, created_at FROM user WHERE id = ?");
      stmt.setLong(1, id);
      var rs = stmt.executeQuery();
      if (rs.next()) {
        var user = new User();
        user.setId(id);
        user.setUsername(rs.getString("username"));
        user.setCreatedAt(rs.getTimestamp("created_at"));
        return Optional.of(user);
      }
      return Optional.empty();
    } catch (SQLException e) {
      throw new RuntimeException(e);
    }
  }
}
