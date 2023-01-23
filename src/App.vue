<!-- <template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/Streaming">Streaming</router-link> |
      <router-link to="/MultiCamera">MultiCamera</router-link>
    </nav>
    <router-view/>
  </div>
</template> -->

<!-- <style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style> -->
<template>
  <div>
    <sidebar-menu-akahon 
      @search-input-emit="search"
      
    />
    <router-view/>
  </div>
</template>

<script>
import SidebarMenuAkahon from "@/components/Sidebar-menu.vue"

export default {
  name: "App",
  components: {
    SidebarMenuAkahon,
  },
  methods: {
    // search(val) {
      
    // }
  }
}
</script>

<style></style>
