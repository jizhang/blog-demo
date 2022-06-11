<script setup lang="ts">
import 'bootstrap/dist/css/bootstrap.min.css'
</script>

<template>
  <ul>
    <li><router-link to="/demo1">Demo1</router-link></li>
    <li><router-link to="/demo2">Demo2</router-link></li>
    <li><router-link to="/demo3">Demo3</router-link></li>
    <li><router-link to="/form-demo">Form demo</router-link></li>
  </ul>
  <router-view />
</template>

<style>
#app {
  padding: 15px;
}
</style>
