package com.shzhangji.demo.npe;

import edu.umd.cs.findbugs.annotations.CheckForNull;
import edu.umd.cs.findbugs.annotations.NonNull;

public class SpotBugsExample {

  @NonNull
  private Object returnNonNull() {
    return null;
  }

  @CheckForNull
  private Object returnNullable() {
    return null;
  }

  public void testReturnNullable() {
    Object obj = returnNullable();
    System.out.println(obj.toString());
  }

  private void argumentNonNull(@NonNull Object arg) {
    System.out.println(arg.toString());
  }

  public void testArgumentNonNull() {
    argumentNonNull(null);
  }

  public void testNullableArgument(@CheckForNull Object arg) {
    System.out.println(arg.toString());
  }

}
