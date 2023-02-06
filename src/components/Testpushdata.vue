<template>
  <div class="map-section">
    <button type="button" class="btn btn-primary" @click="noom">Go</button>
    <div id="app">
      <button type="button" class="btn btn-primary" v-gamepad:button-a="pressedA"
        v-gamepad:button-a.released="releasedA">{{ textA }}</button>
        <!-- <button type="button"  v-gamepad:button-a="pressedA"
        v-gamepad:button-a.released="releasedA"></button> -->
      <button type="button" class="btn btn-error" v-gamepad:button-x="pressedX"
        v-gamepad:button-x.released="releasedX">{{ textX }}</button>
      <button type="button" class="btn btn-primary" v-gamepad:button-y="pressedY"
        v-gamepad:button-y.released="releasedY">{{ textY }}</button>
      <button type="button" class="btn btn-errror" v-gamepad:button-b="pressedB"
        v-gamepad:button-b.released="releasedB">{{ textB }}</button>
      <button type="button" class="btn btn-primary" v-gamepad:shoulder-left="pressedReset"
        v-gamepad:shoulder-left.released="releasedReset" v-on:click="pressedReset">{{ textLB }}</button>
    </div>
  </div>
</template>
<script>


import firebaseApp from './firebase'
// var db = firebaseApp.database();
export default {
  name: "DrawGoogleMap",
  // firebase: {
  //   control: db.ref("Rover1/control"),
  // },
  data: function () {
    return {
      // mapMarker,
      textA: "A",
      textB: "B",
      textX: "X",
      textY: "Y",
      textLB: "Reset",

    };
  },
  computed: {
    // readonly
    aDouble() {
      return this.center
    },
  },
  mounted() {
    this.dbRefjoy.on('value', ss => {
      for (const [key, value] of Object.entries(ss.val())) {
        console.log(`${key}: ${value}`);
      }

    })
  },

  methods: {
    pressedA(e) {
      this.textA = "Click";
      console.log(`pressA`, e);
      this.dbRefjoy.set({
        forword: 0,
        backword: 1,
        right: 0,
        left: 0
      });
    },
    releasedA() {
      this.textA = "A";
      this.dbRefjoy.set({
        forword: 0,
        backword: 0,
        right: 0,
        left: 0
      });
    },
    pressedX(e) {
      this.textX = "Click";
      console.log(`pressX`, e);
      this.dbRefjoy.set({
        forword: 0,
        backword: 0,
        right: 0,
        left: 1
      });

    },
    releasedX() {
      this.textX = "X";
      this.dbRefjoy.set({
        forword: 0,
        backword: 0,
        right: 0,
        left: 0
      });
    },
    pressedY(e) {
      this.textY = "Click";
      console.log(`pressY`, e);
      this.dbRefjoy.set({
        forword: 1,
        backword: 0,
        right: 0,
        left: 0
      });
    },
    releasedY() {
      this.textY = "Y";
      this.dbRefjoy.set({
        forword: 0,
        backword: 0,
        right: 0,
        left: 0
      });
    },
    pressedB(e) {
      this.textB = "Click";
      console.log(`pressB`, e);
      this.dbRefjoy.set({
        forword: 0,
        backword: 0,
        right: 1,
        left: 0
      });
    },
    releasedB() {
      this.textB = "B";
      this.dbRefjoy.set({
        forword: 0,
        backword: 0,
        right: 0,
        left: 0
      });
    },
    pressedReset(e) {
      this.textLB = "Click";
      console.log(`pressLB`, e);
      this.dbRefjoy.set({
        forword: 0,
        backword: 0,
        right: 0,
        left: 0
      });
    },
    releasedReset() {
      this.textLB = "Reset";
      this.dbRefjoy.set({
        forword: 0,
        backword: 0,
        right: 0,
        left: 0
      });
    },
    // noom() {
    //   console.log("Hi!!")
    //   console.log(this.aDouble)
    //   this.dbRefjoy.push({
    //     backword: 1
    //   });
    //   console.log(coordinates)
    // },
    noss() {
      console.log("Hi!!")
      // console.log(this.aDouble)
      // console.log(coordinates)
    },


  },
  created() {
    // สร้าง reference ไปยัง counter ซึ่งเป็น root node ของ reatime database

    this.dbRefjoy = firebaseApp.database().ref('Rover1/control')
  },
  beforeDestroy() {
    // ยกเลิก subsciption เมื่อ component ถูกถอดจาก dom

    this.dbRefjoy.off()
  }
};
</script>
<style scoped>
.map-section {
  height: 95vh;
  position: relative;
  overflow: hidden;
}

.map-info-window {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  background: #fff;
  padding: 15px 20px 10px;
}

.map-info-window-slide-leave-active,
.map-info-window-slide-enter-active {
  transition: 0.5s;
}

.map-info-window-slide-enter {
  transform: translate(0, -100%);
}

.map-info-window-slide-leave-to {
  transform: translate(0, -100%);
}

.city-info>div {
  margin-bottom: 10px;
}

.map-btn-close-holder {
  margin-top: 10px;
}
</style>