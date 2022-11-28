<template>
  <div id="app">
   
    <!-- <h1> WebRTC Studio</h1>
    <h3>Using Janus webRTC server.</h3> -->
    <div class="select-ctn">
      <select v-model="streamList.selected" :disabled="stream">
        <option v-for="option in streamList.options" :key="option.id" :value="option.id">
          {{ option.description }}
        </option>
      </select>
      <div>{{ stream == null ? "null" : notNull }}</div>
      <!-- <button @click.prevent="start" :disabled="stream">Start</button> -->
      <button type="button" class="btn btn-primary" @click.prevent="start" :disabled="stream">Start</button>
      <!-- <button @click.prevent="stop" :disabled="!stream">Stop</button> -->
      <button type="button" class="btn btn-secondary" @click.prevent="stop" :disabled="!stream">Stop</button>
      <!-- <button onClick="connect(http://34.143.225.243:8088/janus)">connect</button> -->

    </div>
    <div class="md-layout">
    <div class="md-layout-item">
      <h3 v-if="status == 'starting'"> Loading video stream ...  </h3>
      <div class="video-vtn">
      <video autoplay="autoplay" :srcObject.prop="stream" ref="videoStream" playsinline width="640px" height="480px"></video>
    </div>
    </div>
    <!-- <div class="md-layout-item"></div> -->
    <div class="md-layout-item">
      <div class="map-section">
      <gmap-map
        :center="center"
        :zoom="15"
        style="width: 80%; height: 50%"
        :options="{
            zoomControl: false,
            scaleControl: false,
            mapTypeControl: false,
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
      </gmap-map>
    </div>

    </div>
    </div>
    
    

    <div class="md-layout">
    <div class="md-layout-item">
      <div v-if="!stream">No Stream</div>
      <div>Status: {{ status ? status : "No video stream" }}</div>
      <div v-if="error">{{ error }}</div>

    </div>
    <div class="md-layout-item"></div>
    <div class="md-layout-item"></div>
  </div>
  </div>
</template>

<script>
// import { Janus } from 'janus-gateway'
import { Janus } from 'janus-gateway'
import firebaseApp from './firebase'
var la = 14.875811571268388;
var long = 102.01502828868293;
var la_User = 14.875811571268388;
var long_User = 102.01502828868293;
let iconCar ="https://i.postimg.cc/3N0bcm0F/Picture-Car.png";
let iconUser = "https://i.postimg.cc/bNC9tsGz/icons8-iphone-se-80.png";
// const JANUS_URL = 'http://127.0.0.1:8088/janus'
//const JANUS_URL = 'http://34.87.84.21:8088/janus'
let JANUS_URL = 'https://34.143.225.243:8089/janus'
if(window.location.protocol === 'http:'){
  // console.log(JANUS_URL)
  JANUS_URL = 'http://34.143.225.243:8088/janus'
  console.log(JANUS_URL)
}


export default {
  name: 'App',
  data(){
    return {
      janus: null,
      error: null,
      plugin: null,
      status: null,
      stream: null,
      streamList: {
        selected: null,
        options: []
      },
      remoteTracks : {},
      remoteVideos : 0,
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
    }
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
                  lat: (la+la_User)/2, 
                  lng: (long+long_User)/2
                  // lat: la_User, 
                  // lng:long_User
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
                  // lat: la_User, 
                  // lng:long_User
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
      Janus.init({
      debug: true,
      dependencies: Janus.useDefaultDependencies(),
      callback: ()=>{
        console.log("Connecting to Janus api with server ",JANUS_URL)
        this.connect(JANUS_URL)
      }
    })
  },
  methods:{
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
   
      },
    connect(server){
      this.janus = new Janus({server,
        // Call success callback
        success: ()=>{
          console.log("Connected")
          this.attachPlugin()
        },
        // Call error callback 
        error: (error)=>{
          console.log("Error")
          this.onError('Failed to connect janus server',error)
        },
        // Call destroyed callback
        destroyed: ()=>{
          console.log("Destroyed")
          window.location.reload()
        }
      })
    },

    attachPlugin() {
      this.janus.attach({
        plugin: "janus.plugin.streaming",
        opaqueId: 'thisisopaqueid',
        success: (pluginHandle) => {
          this.plugin = pluginHandle
          console.log("getBitrate : ",this.plugin.getBitrate())
          this.updateStreamsList()
        },
        error: (error) => {
          this.onError('Error attaching plugin... ', error)
        },
        iceState: (state) => {
          console.log("ICE state changed to ",state)
        },
        webrtcState: (on) => {
          console.log("Janus says our WebRTC PeerConnection is " + (on ? "up" : "down") + " now")
        },
        slowLink: (uplink, lost, mid) => {
          console.log("Janus reports problems " + (uplink ? "sending" : "receiving") +
										" packets on mid " + mid + " (" + lost + " lost packets)")
        },
        onmessage: (msg, jsep) => {
          // Receive status of plugin streaming 
          console.log(" ::: Got a message :::", msg)
          let result = msg.result
          if(result){
            if(result.status){
              this.status = result.status
            }
          }
          // Handle msg error status 
          else if (msg.error) {
            this.onError(msg.error)
            this.stop()
            return ;
          }
          if(jsep) {
            Janus.debug("Handling SDP as Well... ", jsep)
            let stereo = (jsep.sdp.indexOf("stereo=1") !== -1 )
            this.plugin.createAnswer({
              jsep: jsep,
              media: {
                audioSend: false,
                videoSend: false,
                data: true
              },
              customizeSdp: (jsep) => {
                if(stereo && jsep.sdp.indexOf("stereo=1") == -1 ) {
                  jsep.sdp = jsep.sdp.replace("useinbandfec=1", "useinbandfec=1;stereo=1")
                }
              },
              success: (jsep) => {
                Janus.debug("Got SDP!", jsep)
                let body = { request: "start"}
                this.plugin.send({
                  message: body,
                  jsep: jsep
                })
              },
              error: (error) => {
                this.onError("WebRTC Error: ",error)
                alert("WebRTC error... " , error)
              }
            })
          }
        },
        onremotetrack: (track , mid, on) => {
          Janus.debug("Remote track (mid=" + mid + ") " + (on ? "added" : "removed") + ":", track)
          // New track was added 
          if(track.kind === "video") {
            this.remoteVideos++ 
            this.stream = new MediaStream()
            this.stream.addTrack(track.clone())
            this.remoteTracks.mid = this.stream
            Janus.log("Created remote audio stream:", this.stream)
          }
        },
        
        oncleanup: () => {
          this.onCleanup()
        }
      })
    },
    updateStreamsList() {
      this.plugin.send ({
        message: { request: "list"},
        success: (result) => {
          if(!result) {
            this.onError("Got no response to our query for available streams.")
          }
          console.log("Updating StreamList....",result)
          this.streamList.options = result.list
          if (result.list.length) {
            this.streamList.selected = this.streamList.options[0].id
          }
        }
      })
    },
    start() {
      this.plugin.send({ message: { request: "watch", id: this.streamList.selected } })
    },
    stop() {
      this.plugin.send({ message: { request: "stop" } } )
      this.plugin.hangup()
    },
    // Reset data.params to null 
    onCleanup() {
      Janus.log(" ::: Got a cleanup notification :::");
      this.stream = null
      this.status = null 
      this.remoteTracks = {}
      this.remoteVideos = 0
      this.error = null 
    },
    // Handle on error event occur
    onError(message, error='') {
      Janus.error(message, error)
      this.error = message + error
      alert(this.error, function() {
        window.location.reload()
      })
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
}
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
    width: 50%;
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

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #48627c;
  margin-top: 60px;
}
div {
  margin-bottom: 1.5rem;
}
button {
  padding: .5rem .7rem;
  margin: 0 .5rem 0 .5rem;
}
video {
  width: 80%;
}
</style>
