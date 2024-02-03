package com.shzhangji.flinkdi;

import com.google.inject.AbstractModule;
import com.google.inject.Provides;
import com.google.inject.Singleton;
import com.zaxxer.hikari.HikariConfig;
import com.zaxxer.hikari.HikariDataSource;
import javax.sql.DataSource;

public class DatabaseModule extends AbstractModule {
  @Provides
  @Singleton
  public DataSource provideDataSource() {
    var config = new HikariConfig();
    config.setJdbcUrl("jdbc:mysql://localhost:3306/flink_di");
    config.setUsername("root");
    config.setPassword("");
    return new HikariDataSource(config);
  }

  @Provides
  @Singleton
  public UserRepository provideUserRepository(DataSource dataSource) {
    return new UserRepositoryImpl(dataSource);
  }
}
