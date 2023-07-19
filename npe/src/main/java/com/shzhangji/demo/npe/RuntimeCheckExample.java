package com.shzhangji.demo.npe;

import com.google.common.base.Preconditions;
import lombok.NonNull;

import java.util.Objects;

public class RuntimeCheckExample {

  public void testObjects(Object arg) {
    Object checked = Objects.requireNonNull(arg, "arg must not be null");
    checked.toString();
  }

  public void testGuava(Object arg) {
    Object checked = Preconditions.checkNotNull(arg, "%s must not be null", "arg");
    checked.toString();
  }

  public void testLombok(@NonNull Object arg) {
    arg.toString();
  }

  public void testLombokGenerated(Object arg) {
    if (arg == null) {
      throw new NullPointerException("arg is marked @NonNull but is null");
    }
    arg.toString();
  }

  public static void main(String[] args) {
    new RuntimeCheckExample().testLombokGenerated(null);
  }

}
