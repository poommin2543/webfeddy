<template>
  <div class="map-section">
    <button type="button" class="btn btn-primary" @click="noom">Go</button>
    <div id="app">
    <button type="button" class="btn btn-primary" v-gamepad:button-a="pressedA" v-gamepad:button-a.released="releasedA">{{ textA }}</button>
    <button type="button" class="btn btn-error" v-gamepad:button-x="pressedX" v-gamepad:button-x.released="releasedX">{{ textX }}</button>
    <button type="button" class="btn btn-primary" v-gamepad:button-y="pressedY" v-gamepad:button-y.released="releasedY">{{ textY }}</button>
    <button type="button" class="btn btn-errror" v-gamepad:button-b="pressedB" v-gamepad:button-b.released="releasedB">{{ textB }}</button>
    <button type="button" class="btn btn-primary" v-gamepad:shoulder-left="pressedReset" v-gamepad:shoulder-left.released="releasedReset" v-on:click="pressedReset" >{{ textLB }}</button>
  </div> 
    <!-- <gmap-map
      :center="center"
      :zoom="16.5"
      style="width: 100%; height: 100%"
      :options="{
          zoomControl: false,
          scaleControl: true,
          mapTypeControl: true,
          fullscreenControl: true,
          streetViewControl: false,
          disableDefaultUi: false
        }">
      <gmap-marker
        v-for="(item, key) in coordinates"
        :key="key"
        :position="getPosition(item)"
        :clickable="true"
        :icon="getMarkers1(key)"
        @click="toggleInfo(item, key)"
      ></gmap-marker>
    </gmap-map> -->
    
  </div>
</template>
 
<script>


import firebaseApp from './firebase'
// var nnn = 14.875811571268388;
var la = 14.875811571268388;
var long = 102.01502828868293;
var la_User = 14.875811571268388;
var long_User = 102.01502828868293;
var db = firebaseApp.database();
export default {
  name: "DrawGoogleMap",
  firebase: {
    control: db.ref("Rover1/control"),
  },
  data: function() {
    // let mapMarker ="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjMiIGhlaWdodD0iMjkiIHZpZXdCb3g9IjAgMCAyMyAyOSIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4NCjxwYXRoIGQ9Ik0yMyAxMS41QzIzIDIxLjUgMTEuNSAyOC41IDExLjUgMjguNUMxMS41IDI4LjUgMCAyMS41IDAgMTEuNUMwIDUuMTQ4NzMgNS4xNDg3MyAwIDExLjUgMEMxNy44NTEzIDAgMjMgNS4xNDg3MyAyMyAxMS41WiIgZmlsbD0iI0M3MDYyOSIvPg0KPGNpcmNsZSBjeD0iMTEuNSIgY3k9IjExLjUiIHI9IjUuNSIgZmlsbD0iIzgxMDAxNyIvPg0KPC9zdmc+DQo=";
    // let iconCar ="http://maps.google.com/mapfiles/kml/shapes/cabs.png";
    let iconCar ="https://i.postimg.cc/3N0bcm0F/Picture-Car.png";
    // let mapMarkerActive = "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjMiIGhlaWdodD0iMjkiIHZpZXdCb3g9IjAgMCAyMyAyOSIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4NCjxwYXRoIGQ9Ik0yMyAxMS41QzIzIDIxLjUgMTEuNSAyOC41IDExLjUgMjguNUMxMS41IDI4LjUgMCAyMS41IDAgMTEuNUMwIDUuMTQ4NzMgNS4xNDg3MyAwIDExLjUgMEMxNy44NTEzIDAgMjMgNS4xNDg3MyAyMyAxMS41WiIgZmlsbD0iIzMzMzMzMyIvPg0KPGNpcmNsZSBjeD0iMTEuNSIgY3k9IjExLjUiIHI9IjUuNSIgZmlsbD0iYmxhY2siLz4NCjwvc3ZnPg0K";
    let mapMarkerActive = "http://maps.google.com/mapfiles/kml/pushpin/red-pushpin.png";
    let iconUser = "https://i.postimg.cc/bNC9tsGz/icons8-iphone-se-80.png";
    
    return {
      // mapMarker,
      textA: "A",
      textB: "B",
      textX: "X",
      textY: "Y",
      textLB: "Reset",
      mapMarkerActive,
      iconCar,
      iconUser,
      latitude: 0,
      longitude: 0,
      center: { 
          lat: 0, 
          lng: 0
      },
      locations: [],
      currentLocation: null,
      selectedKey: null,
      selectedMarker: null,
      coordinates: {
      0: {
        lat: la.toString(),
        lng: long.toString()
      },
      1: {
        lat: la_User.toString(),
        lng: long_User.toString()
      },
    }
    };
  },
  computed: {
  // readonly
      aDouble() {
        return this.center
  },
},
  mounted() {
    this.setLocationLatLng();
    // this.dbRefjoy.set({
    //   backword: 1
    // });
    this.dbRefjoy.on('value', ss => {
          for (const [key, value] of Object.entries(ss.val())) {
            console.log(`${key}: ${value}`);
          }

      })

    this.dbRef.on('value', ss => {
          for (const [key, value] of Object.entries(ss.val())) {
            if (key == "latitude"){
              this.latitude = value
              console.log(`${key}: ${value}`);
              la = value;
            }
            if (key == "longitude"){
              this.longitude = value
              console.log(`${key}: ${value}`);
              long = value;
            }
            this.center = { 
                lat: (la+la_User)/2, 
                lng: (long+long_User)/2
              }
            this.coordinates = {
            0: {
              lat: la.toString(),
              lng: long.toString()
            },
            1: {
              lat: la_User.toString(),
              lng: long_User.toString()
            },
    }
          }

      })

      this.dbRef1.on('value', ss => {
          console.log(ss.val());
          for (const [key, value] of Object.entries(ss.val())) {
            if (key == "latitude"){
              this.latitude = value
              console.log(`${key}: ${value}`);
              // this.latitude;
              la_User = value;

            }
            if (key == "longitude"){
              this.longitude = value
              console.log(`${key}: ${value}`);
              long_User = value;

            }
            this.center = { 
                lat: (la+la_User)/2, 
                lng: (long+long_User)/2
              }
            this.coordinates = {
            0: {
              lat: la.toString(),
              lng: long.toString()
            },
            1: {
              lat: la_User.toString(),
              lng: long_User.toString()
            },
    }
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
    noom(){
        console.log("Hi!!")
        console.log(this.aDouble)
        this.dbRefjoy.push({
         backword: 1
         });
        // console.log(coordinates)
    },
    noss(){
        console.log("Hi!!")
        // console.log(this.aDouble)
        // console.log(coordinates)
    },
   getMarkers(key) {
    if (this.selectedKey === key) return this.mapMarkerActive;
    return this.mapMarker;
  },
  getMarkers1(key) {
    console.log(key)
    if(key == 0){
      return this.iconCar;
    }
    if(key == 1){
      return this.iconUser;
    }
  },
  getPosition: function(marker) {
    return {
      lat: parseFloat(marker.lat),
      lng: parseFloat(marker.lng)
    };
  },
  toggleInfo: function(marker, key) {
    this.infoPosition = this.getPosition(marker);
    this.selectedMarker = marker;
    this.selectedKey = key;
    this.infoOpened = !this.infoOpened;
  },
  closeInfoWindow: function() {
    this.infoOpened = false;
    this.markerOptions = this.mapMarker;
  },
    setPlace(loc) {
      this.currentLocation = loc;
    },
  
  
    setLocationLatLng: function() {
        navigator.geolocation.getCurrentPosition(geolocation => {
          this.center = {
            lat: geolocation.coords.latitude,
            lng: geolocation.coords.longitude
          };
        });
    }
  
  },
  created() {
      // ??????????????? reference ??????????????? counter ???????????????????????? root node ????????? reatime database
      this.dbRef = firebaseApp.database().ref('locationCar')
      this.dbRef1 = firebaseApp.database().ref('location')
      this.dbRefjoy = firebaseApp.database().ref('Rover1/control')
  },
  beforeDestroy() {
      // ?????????????????? subsciption ??????????????? component ??????????????????????????? dom
      this.dbRef.off()
      this.dbRef1.off()
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
.city-info > div {
  margin-bottom: 10px;
}
.map-btn-close-holder {
  margin-top: 10px;
}
</style>