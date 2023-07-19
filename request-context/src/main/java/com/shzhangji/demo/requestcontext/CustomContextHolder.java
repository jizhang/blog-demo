package com.shzhangji.demo.requestcontext;

import org.springframework.stereotype.Component;

@Component
public class CustomContextHolder {
  private static final ThreadLocal<CustomContext> holder = new ThreadLocal<>();

  public void set(CustomContext context) {
    holder.set(context);
  }

  public CustomContext get() {
    return holder.get();
  }

  public void remove() {
    holder.remove();
  }
}
