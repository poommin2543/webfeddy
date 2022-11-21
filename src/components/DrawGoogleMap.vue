<template>
    <div class="map-section">
      <!-- <h2>Vue Js Google Maps with Multiple Markers </h2> -->
      <!-- <p>Latitude: {{ latitude }},Longitude:{{longitude}}</p> -->
      <!-- <GmapAutocomplete
        @place_changed='setPlace'
      /> -->
      <!-- <button @click="getMarkers(key)">Refresh</button> -->
      <gmap-map
        :center="center"
        :zoom="16.5"
        style="width: 100%; height: 100%"
        :options="{
            zoomControl: false,
            scaleControl: false,
            mapTypeControl: false,
            fullscreenControl: false,
            streetViewControl: false,
            disableDefaultUi: false
          }">
        <!-- <gmap-marker
          :key="index"
          v-for="(gmp, index) in locations"
          :position="gmp"
          :icon="getMarkers(key)"
          @click="center=gmp"
          
        ></gmap-marker> -->
        <gmap-marker
          v-for="(item, key) in coordinates"
          :key="key"
          :position="getPosition(item)"
          :clickable="true"
          :icon="getMarkers1(key)"
          @click="toggleInfo(item, key)"
        ></gmap-marker>
        <!-- <gmap-marker v-on:change="updateCoordinates()" :position="center" :draggable="true" @closeclick="updateCoordinates()"/> -->
      </gmap-map>
      <!-- <transition name="map-info-window-slide">
        <div
          class="map-info-window"
          :opened="infoOpened"
          :position="infoPosition"
          v-if="infoOpened"
        >
          <div class="city-info" v-if="selectedMarker">
            <div class="city-location">{{ selectedMarker.lat }} , {{ selectedMarker.lng }}</div>
            <button class="btn btn-full-width btn-main">Update</button>
            <div class="map-btn-close-holder">
              <button class="map-btn-close" @click="closeInfoWindow()">close</button>
            </div>
          </div>
          
        </div>
      </transition> -->
      <!-- <p>Latitude: {{ latitude }},Longitude:{{longitude}}</p>
      <button @click="noom">Refresh</button> -->
    </div>
  </template>
   
  <script>


import firebaseApp from './firebase'

  // var nnn = 14.875811571268388;
  var la = 14.875811571268388;
  var long = 102.01502828868293;
  var la_User = 14.875811571268388;
  var long_User = 102.01502828868293;
  export default {
    name: "DrawGoogleMap",
    data: function() {
      // let mapMarker ="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjMiIGhlaWdodD0iMjkiIHZpZXdCb3g9IjAgMCAyMyAyOSIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4NCjxwYXRoIGQ9Ik0yMyAxMS41QzIzIDIxLjUgMTEuNSAyOC41IDExLjUgMjguNUMxMS41IDI4LjUgMCAyMS41IDAgMTEuNUMwIDUuMTQ4NzMgNS4xNDg3MyAwIDExLjUgMEMxNy44NTEzIDAgMjMgNS4xNDg3MyAyMyAxMS41WiIgZmlsbD0iI0M3MDYyOSIvPg0KPGNpcmNsZSBjeD0iMTEuNSIgY3k9IjExLjUiIHI9IjUuNSIgZmlsbD0iIzgxMDAxNyIvPg0KPC9zdmc+DQo=";
      // let iconCar ="http://maps.google.com/mapfiles/kml/shapes/cabs.png";
      let iconCar ="https://i.postimg.cc/3N0bcm0F/Picture-Car.png";
      // let mapMarkerActive = "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjMiIGhlaWdodD0iMjkiIHZpZXdCb3g9IjAgMCAyMyAyOSIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4NCjxwYXRoIGQ9Ik0yMyAxMS41QzIzIDIxLjUgMTEuNSAyOC41IDExLjUgMjguNUMxMS41IDI4LjUgMCAyMS41IDAgMTEuNUMwIDUuMTQ4NzMgNS4xNDg3MyAwIDExLjUgMEMxNy44NTEzIDAgMjMgNS4xNDg3MyAyMyAxMS41WiIgZmlsbD0iIzMzMzMzMyIvPg0KPGNpcmNsZSBjeD0iMTEuNSIgY3k9IjExLjUiIHI9IjUuNSIgZmlsbD0iYmxhY2siLz4NCjwvc3ZnPg0K";
      let mapMarkerActive = "http://maps.google.com/mapfiles/kml/pushpin/red-pushpin.png";
      let iconUser = "https://i.postimg.cc/bNC9tsGz/icons8-iphone-se-80.png";
      // var iconBase = 'https://maps.google.com/mapfiles/kml/shapes/';
      // var iconBase = 'https://maps.google.com/mapfiles/kml/shapes/';
      // var iconUser = 'http://maps.google.com/mapfiles/kml/shapes/parking_lot_maps.png';
      // var iconUser = 'http://maps.google.com/mapfiles/kml/shapes/info-i_maps.png';

      // var icons = {
      //   parking: {
      //     icon: iconBase + 'parking_lot_maps.png'
      //   },
      //   library: {
      //     icon: iconBase + 'library_maps.png'
      //   },
      //   info: {
      //     icon: iconBase + 'info-i_maps.png'
      //   }
      // };
      return {
        // mapMarker,
        mapMarkerActive,
        iconCar,
        iconUser,
        latitude: 0,
        longitude: 0,
        center: { 
            lat: la, 
            lng: long
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
      this.dbRef.on('value', ss => {
            // console.log(ss.val());
            
            for (const [key, value] of Object.entries(ss.val())) {
              if (key == "latitude"){
                this.latitude = value
                console.log(`${key}: ${value}`);
                // this.latitude;
                la = value;
              //   this.coordinates = {
              //   0: {
              //     lat: value.toString(),
              //   },
              // }
              // this.center = { 
              //     lat: value, 
              //     // lng: long
              //   }

              }
              if (key == "longitude"){
                this.longitude = value
                console.log(`${key}: ${value}`);
                long = value;
              //   this.coordinates = {
              //   0: {
              //     lng: value.toString()
              //   },
              // }
              // this.center = {  
              //     lng: value
              //   }
              }
              this.center = { 
                  lat: la, 
                  lng: long
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
      noom(){
          console.log("Hi!!")
          console.log(this.aDouble)
          // console.log(coordinates)
      },
      // updateCoordinates() {
      //       this.coordinates = {
      //           lat: la,
      //           lng: long,
      //       };
      //   },
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
      // if (this.selectedKey === key) return this.mapMarker;
      // return this.mapMarkerActive;
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
   
          // this.locations = [
          //   {
          //       lat: la,
          //       lng: long,
          //       label: 'user location'
          //   },
            // {
            //     lat: 14.874727933912586,
            //     lng: 102.0155504911628,
            //     label: 'Car'
            // },
            // {
            //     lat: 41.3828939,
            //     lng: 2.1774322,
            //     label: 'Barcelona'
            // },
            // {
            //     lat: -10.3333333,
            //     lng: -53.2,
            //     label: 'Brazil'
            // }
        // ];
   
      }
    
    },
    
    created() {
        // สร้าง reference ไปยัง counter ซึ่งเป็น root node ของ reatime database
        this.dbRef = firebaseApp.database().ref('locationCar')
        this.dbRef1 = firebaseApp.database().ref('location')

    },

    

    beforeDestroy() {
        // ยกเลิก subsciption เมื่อ component ถูกถอดจาก dom
        this.dbRef.off()
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