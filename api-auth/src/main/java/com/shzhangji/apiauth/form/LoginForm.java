package com.shzhangji.apiauth.form;

import jakarta.validation.constraints.NotBlank;
import lombok.Data;

@Data
public class LoginForm {
  @NotBlank
  private String username;
  @NotBlank
  private String password;
}
