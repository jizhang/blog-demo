package com.shzhangji.flinkdi;

import java.sql.SQLException;
import java.util.Objects;
import javax.sql.DataSource;
import org.apache.flink.api.common.functions.RichMapFunction;
import org.apache.flink.configuration.Configuration;

public class UserMapper extends RichMapFunction<Long, User> {
  transient DataSource dataSource;

  @Override
  public void open(Configuration parameters) throws Exception {
    var injector = AppInjector.getInjector();
    dataSource = injector.getInstance(DataSource.class);
  }

  @Override
  public User map(Long userId) throws Exception {
    Objects.requireNonNull(userId, "User ID is null");
    return getUserInfo(userId);
  }

  private User getUserInfo(long userId) throws SQLException {
    try (var conn = dataSource.getConnection()) {
      var stmt = conn.prepareStatement("SELECT username, created_at FROM user WHERE id = ?");
      stmt.setLong(1, userId);
      var rs = stmt.executeQuery();
      if (rs.next()) {
        var user = new User();
        user.setId(userId);
        user.setUsername(rs.getString("username"));
        user.setCreatedAt(rs.getTimestamp("created_at"));
        return user;
      }
      throw new RuntimeException("Record not found");
    }
  }
}
