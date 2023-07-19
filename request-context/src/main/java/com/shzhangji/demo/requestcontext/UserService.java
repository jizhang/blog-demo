package com.shzhangji.demo.requestcontext;

import javax.servlet.http.HttpServletRequest;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.web.context.request.RequestAttributes;
import org.springframework.web.context.request.RequestContextHolder;

@Slf4j
@Service
@RequiredArgsConstructor
public class UserService {
  private final HttpServletRequest request;
  private final CustomContext context;
  private final CustomContextHolder holder;

  public User getFromRequest() {
    var user = (User) request.getAttribute("user");
    log.info("Get from HttpServletRequest: {}", user);
    return user;
  }

  public User getFromScoped() {
    log.info("Get from request-scoped context: {}", context.getUser());
    return context.getUser();
  }

  public User getFromCustomContextHolder() {
    var user = holder.get().getUser();
    log.info("Get from CustomContextHolder: {}", user);
    return user;
  }

  public User getFromRequestContextHolder() {
    var user = (User) RequestContextHolder.currentRequestAttributes()
        .getAttribute("user", RequestAttributes.SCOPE_REQUEST);
    log.info("Get from RequestContextHolder: {}", user);
    return user;
  }
}
