package com.shzhangji.flinkdi;

import com.google.inject.Guice;
import com.google.inject.Injector;

public class AppInjector {
  private static class Holder {
    static final Injector INJECTOR = Guice.createInjector(new DatabaseModule());
  }

  private AppInjector() {}

  public static void injectMembers(Object instance) {
    Holder.INJECTOR.injectMembers(instance);
  }

  public static Injector getInjector() {
    return Holder.INJECTOR;
  }
}
