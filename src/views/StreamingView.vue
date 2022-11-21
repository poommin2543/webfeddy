<template>
  <div>
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <Streaming />
  </div>
</template>

<script>
// @ is an alias to /src
import Streaming from '@/components/StreamVideo.vue'

export default {
  name: 'StreamingView',
  components: {
    Streaming
  }
}
</script>
