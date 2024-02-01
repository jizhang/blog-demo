package com.shzhangji.flinkdi;

import java.util.Date;
import lombok.Data;

@Data
public class User {
  private long id;
  private String username;
  private Date createdAt;
}
