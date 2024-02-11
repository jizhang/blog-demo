package com.shzhangji.flinkdi;

import java.util.Date;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class User {
  private long id;
  private String username;
  private Date createdAt;
}
