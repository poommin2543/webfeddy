<template>
    <div>
      <h2>Vue Js Google Maps with Multiple Markers </h2>
      <p>Latitude: {{ latitude }},Longitude:{{longitude}}</p>
      <GmapAutocomplete
        @place_changed='setPlace'
      />
      <button @click="addMarker">Refresh</button>
      <gmap-map
        :center="center"
        :zoom="18"
        style="width:100%;  height: 555px;">
        <gmap-marker
          :key="index"
          v-for="(gmp, index) in locations"
          :position="gmp"
          @click="center=gmp"
        ></gmap-marker>
        <!-- <gmap-marker v-on:change="updateCoordinates()" :position="center" :draggable="true" @closeclick="updateCoordinates()"/> -->
      </gmap-map>
   
    </div>
  </template>
   
  <script>


import firebaseApp from './firebase'

  // var nnn = 14.875811571268388;
  var la = 14.875811571268388;
  var long = 102.01502828868293;
  export default {
    name: "DrawGoogleMap",
    data() {
      return {
        latitude: 0,
        longitude: 0,
        center: { 
            lat: la, 
            lng: long
        },
        locations: [],
        currentLocation: null,
        coordinates: null,
      };
    },
   
    mounted() {
      this.setLocationLatLng();
      this.dbRef.on('value', ss => {
            console.log(ss.val());
            
            for (const [key, value] of Object.entries(ss.val())) {
              if (key == "latitude"){
                this.latitude = value
                console.log(`${key}: ${value}`);
                // this.latitude;
                la = value;

              }
              if (key == "longitude"){
                this.longitude = value
                console.log(`${key}: ${value}`);
                long = value;

              }
            }

        })

        // this.dbRef1.on('value', ss => {
        //     console.log(ss.val());
        //     for (const [key, value] of Object.entries(ss.val())) {
        //       if (key == "latitude"){
        //         this.latitude = value
        //         console.log(`${key}: ${value}`);
        //         // this.latitude;
        //         la = value;

        //       }
        //       if (key == "longitude"){
        //         this.longitude = value
        //         console.log(`${key}: ${value}`);
        //         long = value;

        //       }
        //     }

        // })

    },
   
    methods: {
      noom(){
          console.log("Hi!!")
      },
      updateCoordinates() {
            this.coordinates = {
                lat: la,
                lng: long,
            };
        },
      

      // addMarker(location) {

      //   let marker = new google.maps.Marker({
      //       position: location,
      //       map: this.map,
      //   });
      //   this.markersArray.push(marker);

      //   },
      setPlace(loc) {
        this.currentLocation = loc;
      },
      addMarker() {
      if (this.currentPlace) {
        
        const marker = {
          lat: this.currentPlace.geometry.location.lat(),
          lng: this.currentPlace.geometry.location.lng(),
        };
        // this.markers.push({ position: marker });
        // this.places.push(this.currentPlace);
        // this.center = marker;
        // this.currentPlace = null;
        console.log(marker);
      }
      else{
        console.log("Hi!!")
        const marker = {
          lat: 14.875811571268388,
          lng: 102.01502828868293,
        };
        console.log(marker);
        this.markers.push(marker);
        // this.places.push(this.currentPlace);
        this.center = marker;
        this.currentPlace = null;
      }
    },
    
      setLocationLatLng: function() {
          navigator.geolocation.getCurrentPosition(geolocation => {
            this.center = {
              lat: geolocation.coords.latitude,
              lng: geolocation.coords.longitude
            };
          });
   
          this.locations = [
            {
                lat: la,
                lng: long,
                label: 'user location'
            },
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
        ];
   
      }
    },
    
    created() {
        // สร้าง reference ไปยัง counter ซึ่งเป็น root node ของ reatime database
        this.dbRef = firebaseApp.database().ref('locationCar')
        // this.dbRef1 = firebaseApp.database().ref('location')

    },

    

    beforeDestroy() {
        // ยกเลิก subsciption เมื่อ component ถูกถอดจาก dom
        this.dbRef.off()
    }
  };
  </script>