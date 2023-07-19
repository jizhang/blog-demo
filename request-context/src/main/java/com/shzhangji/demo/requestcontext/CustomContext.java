package com.shzhangji.demo.requestcontext;

import lombok.Data;
import org.springframework.stereotype.Component;
import org.springframework.web.context.annotation.RequestScope;

@Data
@Component
@RequestScope
public class CustomContext {
  private User user;
}
