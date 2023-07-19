package com.shzhangji.demo.npe;

import org.springframework.jdbc.core.JdbcTemplate;

import java.util.Collection;
import java.util.Collections;
import java.util.List;


public class CodingConventionExample {

  public void testString(String str, Object obj) {
    if (str != null && str.equals("text")) {}
    if ("text".equals(str)) {}

    if (obj != null) { obj.toString(); }
    String.valueOf(obj); // "null"
  }

  public void testUtils(String str, Collection<?> col) {
    org.springframework.util.StringUtils.hasLength(str);
    org.springframework.util.CollectionUtils.isEmpty(col);

    com.google.common.base.Strings.isNullOrEmpty(str);

    org.apache.commons.collections4.CollectionUtils.isEmpty(col);
  }

  public void methodA(Object arg1) {
    methodB(arg1, new Object[0]);
  }

  public void methodB(Object arg1, Object[] arg2) {
    for (Object obj : arg2) {} // no null check
  }

  public void testJdbc() {
    JdbcTemplate jdbcTemplate = new JdbcTemplate();
    jdbcTemplate.queryForList("SELECT 1");
    jdbcTemplate.queryForObject("SELECT 1", Integer.class);
  }

  public <T> List<T> testReturnCollection() {
    return Collections.emptyList();
  }

}
