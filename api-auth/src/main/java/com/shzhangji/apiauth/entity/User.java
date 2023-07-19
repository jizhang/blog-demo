package com.shzhangji.apiauth.entity;

import java.util.Collection;
import java.util.Collections;
import java.util.Date;
import java.util.Set;
import lombok.Data;
import org.springframework.data.relational.core.mapping.Table;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

@Data
@Table
public class User implements UserDetails {
  private Integer id;
  private String username;
  private String password;
  private String nickname;
  private Date createdAt;
  private Date updatedAt;

  @Override
  public Collection<? extends GrantedAuthority> getAuthorities() {
    return Set.of();
  }

  @Override
  public boolean isAccountNonExpired() {
    return true;
  }

  @Override
  public boolean isAccountNonLocked() {
    return true;
  }

  @Override
  public boolean isCredentialsNonExpired() {
    return true;
  }

  @Override
  public boolean isEnabled() {
    return true;
  }
}
