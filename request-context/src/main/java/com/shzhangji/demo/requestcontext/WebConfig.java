package com.shzhangji.demo.requestcontext;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Component
@RequiredArgsConstructor
public class WebConfig implements WebMvcConfigurer {
  private final UserInterceptor userInterceptor;

  @Override
  public void addInterceptors(InterceptorRegistry registry) {
    registry.addInterceptor(userInterceptor);
  }
}
