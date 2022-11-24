<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <button type="button" class="btn btn-primary">Start</button>
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/DrawGoogleMap.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  }
}
</script>
