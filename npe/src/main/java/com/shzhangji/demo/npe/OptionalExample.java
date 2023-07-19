package com.shzhangji.demo.npe;

import java.util.*;

public class OptionalExample {

  public void testOptional() {
    Optional<String> opt;

    // create
    opt = Optional.empty();
    opt = Optional.of("text");
    opt = Optional.ofNullable(null);

    // test & get
    if (opt.isPresent()) {
      opt.get();
    }

    // fall back
    opt.orElse("default");
    opt.orElseGet(() -> "default");
    opt.orElseThrow(() -> new NullPointerException());

    // operate
    opt.ifPresent(value -> {
      System.out.println(value);
    });
    opt.filter(value -> value.length() > 5);
    opt.map(value -> value.trim());
    opt.flatMap(value -> {
      String trimmed = value.trim();
      return trimmed.isEmpty() ? Optional.empty() : Optional.of(trimmed);
    });
  }

  static class Address {
    String zipCode;

    Optional<String> getZipCode() {
      return Optional.ofNullable(zipCode);
    }
  }

  static class User {
    Address address;

    Optional<Address> getAddress() {
      return Optional.ofNullable(address);
    }
  }

  Optional<User> getUser() {
    return Optional.of(new User());
  }

  public void testChaining() {
    // getUser().getAddress().getZipCode()
    String zipCode = getUser()
        .flatMap(User::getAddress)
        .flatMap(Address::getZipCode)
        .orElse("");
  }

  public void testStreamApi() {
    List<String> stringList = Arrays.asList("aaa", "bbb");
    stringList.stream().findFirst().orElse("default");
    stringList.stream()
        .max(Comparator.naturalOrder())
        .ifPresent(System.out::println);
  }

  public void testPrimitiveType() {
    OptionalInt opt = OptionalInt.of(256);
  }

  public static void main(String[] args) {
    new OptionalExample().testStreamApi();
  }

}
