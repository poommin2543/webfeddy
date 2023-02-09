<template>
  <div class="container-max-widths text-center grid-logo">
    <div class="row grid-color-red">
      <div class="col-lg-2">
        <div class="row grid-color-blue">
          <div class="col-lg-12">
            <p>Poommin Phinphimai</p>
          </div>
        </div>
        <div class="row grid-color-red">
          <div class="col-lg-12">
            <p class="titleheader"> Rover list</p>
            <div class="cardframe blackcardframe"></div>
          </div>
        </div>
        <div class="row grid-color-blue">
          <div class="col-lg-12">
            <p>Noom</p>
          </div>
        </div>
        <div class="row grid-color-red">
          <div class="col-lg-12">
            <div class="cardframe blackcardframe">
              <p class="titleheader"> Rover list</p>
              <!-- <p>Rover status</p> -->
              <div class="cardframemini Trancardframe">

                <p>Rover : {{ namerover }}</p>
                <p>Status : {{ StatusRover }}</p>
                <p>Battery : {{ Battery }}</p>
                <p>Velocity: {{ Velocity }}</p>
                <p></p>


              </div>
              <!-- <p>Order tatus</p> -->
              <div class="cardframeminize Trancardframe">
                <p>Order No. : </p>
                <p>Status : </p>
                <p>Time Estima : </p>
              </div>


            </div>

          </div>
        </div>
        <div class="row grid-color-blue">
          <div class="col-lg-12">
            <div v-if="isActive === true">
              <button type="button" class="buttondrive" :class="isActive ? 'buttondriveclose' : 'buttondrive'"
                @click="isActive = !isActive">Manual</button>
            </div>
            <div v-if="isActive === false">
              <button type="button" class="buttondrive" :class="isActive ? 'buttondriveclose' : 'buttondrive'"
                @click="isActive = !isActive">Auto</button>
            </div>

            <div v-if="isActive">
              <button type="button" class="buttondrive" @click="joystick()">Joy</button>
            </div>
            <div v-if="isActiveJoy && isActive">
              <button type="button" v-gamepad:button-a="pressedA" v-gamepad:button-a.released="releasedA"></button>
              <button type="button" v-gamepad:button-x="pressedX" v-gamepad:button-x.released="releasedX"></button>
              <button type="button" v-gamepad:button-y="pressedY" v-gamepad:button-y.released="releasedY"></button>
              <button type="button" v-gamepad:button-b="pressedB" v-gamepad:button-b.released="releasedB"></button>
              <button type="button" v-gamepad:shoulder-left="pressedReset"
                v-gamepad:shoulder-left.released="releasedReset" v-on:click="pressedReset"></button>
            </div>
          </div>
        </div>
        <div class="row grid-color-red">
          <div class="col-lg-12">
            <p>Noom</p>
          </div>
        </div>

      </div>

      <div class="col-lg-10">
        noom
        <div class="row grid-container">
          <div class="col-lg-12">
            <Map></Map>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import Map from "@/components/Map.vue"
export default {
  components: {
    Map,
  },
  data() {
    return {
      isOpened: true,
      isActive: false,
      isActiveJoy: false,
    }
  }
}
</script>
<style scoped src="@/assets/styles/stylesViewControl.css">

</style>