<template>
  <div id="app">
    <div class="row ">
      <div class="col-lg-2">
        <div class="map-section">
          <select v-model="streamList.selected" :disabled="stream">
            <option v-for="option in streamList.options" :key="option.id" :value="option.id">
              {{ option.description }}
            </option>
          </select>
          <div>{{ stream == null ? "null" : notNull }}</div>
          <button type="button" class="btn btn-primary" @click.prevent="start" :disabled="stream">Start</button>
          <button type="button" class="btn btn-secondary" @click.prevent="stop" :disabled="!stream">Stop</button>
        <p>{{status}}</p>
        </div>
      </div>
      <div class="col-lg-10">
        <h3 v-if="status == 'starting'"> Loading video stream ... </h3>

        <div class="video-vtn">
          <video autoplay="autoplay" :srcObject.prop="stream" ref="videoStream" playsinline width="1280px"
            height="240px"></video>
        </div>
      </div>
    </div>
    <!-- <div class="md-layout">
      <div class="md-layout-item">
        
      </div>
      <div class="md-layout-item">
        
      </div>
    </div> -->
    <!-- <div class="md-layout">
      <div class="md-layout-item">
      </div>
      <div class="md-layout-item"></div>
      <div class="md-layout-item"></div>
    </div> -->
  </div>
</template>

<script>
import { Janus } from 'janus-gateway'

let JANUS_URL = 'https://34.143.225.243:8089/janus'
if (window.location.protocol === 'http:') {
  // console.log(JANUS_URL)
  JANUS_URL = 'http://103.82.249.178:8088/janus'
  console.log(JANUS_URL)
}


export default {
  name: 'App',
  data() {
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
      remoteTracks: {},
      remoteVideos: 0,


    }
  },
  computed: {
    // readonly
    aDouble() {
      return this.center
    },
  },
  mounted() {
    Janus.init({
      debug: true,
      dependencies: Janus.useDefaultDependencies(),
      callback: () => {
        console.log("Connecting to Janus api with server ", JANUS_URL)
        this.connect(JANUS_URL)
      }
    })
  },
  methods: {
    connect(server) {
      this.janus = new Janus({
        server,
        // Call success callback
        success: () => {
          console.log("Connected")
          this.attachPlugin()
        },
        // Call error callback 
        error: (error) => {
          console.log("Error")
          this.onError('Failed to connect janus server', error)
        },
        // Call destroyed callback
        destroyed: () => {
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
          console.log("getBitrate : ", this.plugin.getBitrate())
          this.updateStreamsList()
        },
        error: (error) => {
          this.onError('Error attaching plugin... ', error)
        },
        iceState: (state) => {
          console.log("ICE state changed to ", state)
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
          if (result) {
            if (result.status) {
              this.status = result.status
            }
          }
          // Handle msg error status 
          else if (msg.error) {
            this.onError(msg.error)
            this.stop()
            return;
          }
          if (jsep) {
            Janus.debug("Handling SDP as Well... ", jsep)
            let stereo = (jsep.sdp.indexOf("stereo=1") !== -1)
            this.plugin.createAnswer({
              jsep: jsep,
              media: {
                audioSend: false,
                videoSend: false,
                data: true
              },
              customizeSdp: (jsep) => {
                if (stereo && jsep.sdp.indexOf("stereo=1") == -1) {
                  jsep.sdp = jsep.sdp.replace("useinbandfec=1", "useinbandfec=1;stereo=1")
                }
              },
              success: (jsep) => {
                Janus.debug("Got SDP!", jsep)
                let body = { request: "start" }
                this.plugin.send({
                  message: body,
                  jsep: jsep
                })
              },
              error: (error) => {
                this.onError("WebRTC Error: ", error)
                alert("WebRTC error... ", error)
              }
            })
          }
        },
        onremotetrack: (track, mid, on) => {
          Janus.debug("Remote track (mid=" + mid + ") " + (on ? "added" : "removed") + ":", track)
          // New track was added 
          if (track.kind === "video") {
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
      this.plugin.send({
        message: { request: "list" },
        success: (result) => {
          if (!result) {
            this.onError("Got no response to our query for available streams.")
          }
          console.log("Updating StreamList....", result)
          this.streamList.options = result.list
          if (result.list.length) {
            this.streamList.selected = this.streamList.options[0].id
          }
        }
      })
    },
    start() {
      // this.plugin.send({ message: { request: "watch", id: this.streamList.selected } })
      this.plugin.send({ message: { request: "watch", id: 11 } })
    },
    stop() {
      this.plugin.send({ message: { request: "stop" } })
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
    onError(message, error = '') {
      Janus.error(message, error)
      this.error = message + error
      alert(this.error, function () {
        window.location.reload()
      })
    }
  },

}
</script>

<style scoped src="@/assets/styles/stylesViewControl.css">
.p{
  background-color: #ffffff;
}

 /* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #48627c;
  margin-top: 60px;
} */
/*
div {
  margin-bottom: 1.5rem;
}

button {
  padding: .5rem .7rem;
  margin: 0 .5rem 0 .5rem;
}

video {
  width: 80%;
} */
</style>
