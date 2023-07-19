<template>
  <div id="app">
    <b-navbar toggleable="md" type="dark" class="navbar">
      <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
      <b-navbar-brand to="/">DW</b-navbar-brand>
      <b-collapse is-nav id="nav_collapse">
        <b-navbar-nav>
          <b-nav-item to="/table-list">Table List</b-nav-item>
          <b-nav-item to="/non-strict">Non Strict</b-nav-item>
          <b-nav-item to="/local-copy">Local Copy</b-nav-item>
          <b-nav-item to="/explicit-update">Explict Update</b-nav-item>
          <b-nav-item to="/computed-property">Computed Property</b-nav-item>
          <b-nav-item to="/map-fields">Map Fields</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style scoped>
.navbar {
  min-height: 64px;
  background-color: #563d7c;
}
</style>
