package com.shzhangji.flinkdi;

import com.google.inject.Guice;
import com.google.inject.Injector;

public class AppInjector {
  private static class Holder {
    static final Injector INJECTOR = Guice.createInjector(new DatabaseModule());
  }

  public static Injector getInjector() {
    return Holder.INJECTOR;
  }
}
