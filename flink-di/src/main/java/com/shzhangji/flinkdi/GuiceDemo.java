package com.shzhangji.flinkdi;

import com.google.inject.AbstractModule;
import com.google.inject.Guice;
import com.google.inject.ImplementedBy;
import com.google.inject.Inject;
import com.google.inject.Provides;
import com.google.inject.Singleton;
import com.google.inject.name.Named;
import com.zaxxer.hikari.HikariConfig;
import com.zaxxer.hikari.HikariDataSource;
import javax.sql.DataSource;

public class GuiceDemo {
  @ImplementedBy(UserRepoImpl.class)
  interface UserRepo {
    void print();
  }

  @Singleton
  static class UserRepoImpl implements UserRepo {
    @Inject @Named("product")
    DataSource dataSource;

    public void print() {
      System.out.println(dataSource);
    }
  }

  static class DemoModule extends AbstractModule {
    @Provides @Named("customer") @Singleton
    public DataSource provideCustomerDataSource() {
      return new HikariDataSource();
    }

    @Provides @Named("product") @Singleton
    public DataSource provideProductDataSource() {
      return new HikariDataSource();
    }
  }

  public static void main(String[] args) {
    var injector = Guice.createInjector(new DemoModule());
    var repo = injector.getInstance(UserRepo.class);
    repo.print();

    System.out.println(repo == injector.getInstance(UserRepo.class));
  }
}
