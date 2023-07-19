package com.shzhangji.demo.requestcontext;

import javax.servlet.http.HttpServletRequest;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestAttribute;
import org.springframework.web.bind.annotation.RestController;

@Slf4j
@RestController
@RequiredArgsConstructor
public class UserController {
  private final UserService service;

  @GetMapping("/ping")
  public String ping() {
    return "pong";
  }

  @GetMapping("/current-user")
  public String getCurrentUser(HttpServletRequest request, @RequestAttribute("user") User userFromAttribute) {
    var user = (User) request.getAttribute("user");
    log.info("Get from HttpServletRequest: {}", user);

    log.info("Get from RequestAttribute: {}", userFromAttribute);

    user = service.getFromRequest();
    user = service.getFromScoped();
    user = service.getFromCustomContextHolder();
    user = service.getFromRequestContextHolder();

    return user.getUsername();
  }
}
