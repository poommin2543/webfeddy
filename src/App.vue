<template>
  <div id="app">
     <DrawGoogleMap />
  </div>
</template>

<script>
import DrawGoogleMap from "./components/DrawGoogleMap";

export default {
 name: 'App',
 components: {
   DrawGoogleMap
 }
}
</script>

<style>
#app {
 font-family: Avenir, Helvetica, Arial, sans-serif;
 -webkit-font-smoothing: antialiased;
 -moz-osx-font-smoothing: grayscale;
 text-align: center;
 color: #000000;
 margin-top: 50px;
}
</style>