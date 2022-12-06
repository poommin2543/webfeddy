<template>
  <div>
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <pushdata />
  </div>
</template>

<script>
// @ is an alias to /src
import pushdata from '@/components/Testpushdata.vue'

export default {
  name: 'PushdataView',
  components: {
    pushdata
  }
}
</script>
