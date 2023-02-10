<template>
  <div id="app">
    <!-- <button type="button" class="btn btn-primary" @click="noom">Go</button> -->

    <!-- <select v-model="streamList.selected" :disabled="stream">
      <option v-for="option in streamList.options" :key="option.id" :value="option.id">
        {{ option.description }}
      </option>
    </select>
    <div>{{ stream == null ? "null" : notNull }}</div>
    <button type="button" class="btn btn-primary" @click.prevent="start" :disabled="stream">Start</button>
    <button type="button" class="btn btn-secondary" @click.prevent="stop" :disabled="!stream">Stop</button> -->

    <div class="md-layout">
      <div class="md-layout-item">
        <select v-model="streamList.selected" :disabled="stream">
          <option v-for="option in streamList.options" :key="option.id" :value="option.id">
            {{ option.description }}
          </option>
        </select>
        <div>{{ stream == null ? "null" : notNull }}</div>
        <button type="button" class="btn btn-primary" @click.prevent="start" :disabled="stream">Start</button>
        <button type="button" class="btn btn-secondary" @click.prevent="stop" :disabled="!stream">Stop</button>
      </div>
      <div class="md-layout-item">
        <select v-model="streamList1.selected" :disabled="stream1">
          <option v-for="option in streamList1.options" :key="option.id" :value="option.id">
            {{ option.description }}
          </option>
        </select>
        <div>{{ stream1 == null ? "null" : notNull }}</div>
        <button type="button" class="btn btn-primary" @click.prevent="start1" :disabled="stream1">Star</button>
        <button type="button" class="btn btn-secondary" @click.prevent="stop1" :disabled="!stream1">Stop</button>
      </div>
      <div class="md-layout-item">

      </div>
    </div>

    <h3 v-if="status == 'starting'"> Loading video stream ... </h3>
    <div class="md-layout">
      <div class="md-layout-item">
        <div class="video-vtn">
          <video autoplay="autoplay" :srcObject.prop="stream" ref="videoStream" playsinline width="640px"
            height="480px"></video>
          <div v-if="!stream">No Stream</div>
          <div>Status: {{ status ? status : "No video stream" }}</div>
          <div v-if="error1">{{ error }}</div>
        </div>
      </div>
      <div class="md-layout-item">
        <div class="video-vtn">
          <video autoplay="autoplay" :srcObject.prop="stream1" ref="videoStream1" playsinline width="640px"
            height="480px"></video>

          <div v-if="!stream1">No Stream</div>
          <div>Status: {{ status1 ? status1 : "No video stream" }}</div>
          <div v-if="error1">{{ error1 }}</div>
        </div>
      </div>
      <div class="md-layout-item">
        <div class="video-vtn">
          <!-- <video autoplay="autoplay" :srcObject.prop="stream" ref="videoStream" playsinline width="640px"
            height="480px"></video> -->
          <!-- <div v-if="!stream">No Stream</div>
          <div>Status: {{ status ? status : "No video stream" }}</div>
          <div v-if="error">{{ error }}</div> -->
        </div>
      </div>
    </div>

  </div>
</template>
 
<script>
import { Janus } from 'janus-gateway'
let JANUS_URL = 'https://34.143.225.243:8089/janus'
if (window.location.protocol === 'http:') {
  // console.log(JANUS_URL)
  JANUS_URL = 'http://34.143.225.243:8088/janus'
  console.log(JANUS_URL)
}
export default {
  name: "MulticameraView",

  data() {
    return {
      janus: null,
      janus1: null,
      janus2: null,
      janus3: null,
      plugin1: null,
      plugin2: null,
      plugin3: null,
      status1: null,
      status2: null,
      status3: null,
      stream1: null,
      stream2: null,
      stream3: null,
      remoteTracks1: {},
      remoteTracks2: {},
      remoteTracks3: {},
      remoteVideos1: 0,
      remoteVideos2: 0,
      remoteVideos3: 0,
      error: null,
      plugin: null,
      status: null,
      stream: null,
      // stream1: null,
      // stream2: null,
      streamList: {
        selected: null,
        options: []
      },
      streamList1: {
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
    //Start
    this.nnn()
    Janus.init({
      debug: true,
      dependencies: Janus.useDefaultDependencies(),
      callback: () => {
        console.log("Connecting to Janus api with server ", JANUS_URL)
        this.connect(JANUS_URL)
        this.connect1(JANUS_URL)
      }
    })
  },




  methods: {
    //function
    async nnn() {
      console.log("++++++++++++++++++++++++++++++++++++");
    },
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
    connect1(server) {
      this.janus1 = new Janus({
        server,
        // Call success callback
        success: () => {
          console.log("Connected")
          this.attachPlugin1()
        },
        // Call error callback 
        error: (error) => {
          console.log("Error Connect Janus1")
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
    attachPlugin1() {
      this.janus1.attach({
        plugin: "janus.plugin.streaming",
        opaqueId: 'thisisopaqueid',
        success: (pluginHandle) => {
          this.plugin1 = pluginHandle
          console.log("getBitrate plugin1 : ", this.plugin1.getBitrate())
          this.updateStreamsList1()
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
              this.status1 = result.status
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
            this.remoteVideos1++
            this.stream1 = new MediaStream()
            this.stream1.addTrack(track.clone())
            this.remoteTracks1.mid = this.stream1
            Janus.log("Created remote audio stream:", this.stream1)
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
          // console.log(streamList)
          if (result.list.length) {
            this.streamList.selected = this.streamList.options[0].id
          }
        }
      })

    },
    updateStreamsList1() {
      this.plugin1.send({
        message: { request: "list" },
        success: (result) => {
          if (!result) {
            this.onError("Got no response to our query for available streams.")
          }
          console.log("Updating StreamList stream1....", result)
          this.streamList1.options = result.list
          // console.log(streamList)
          if (result.list.length) {
            this.streamList1.selected = this.streamList1.options[0].id
          }
        }
      })
    },
    start() {
      this.plugin.send({ message: { request: "watch", id: this.streamList.selected } })
    },
    start1() {
      this.plugin1.send({ message: { request: "watch", id: this.streamList1.selected } })
    },
    stop() {
      this.plugin.send({ message: { request: "stop" } })
      this.plugin.hangup()
    },
    stop1() {
      this.plugin1.send({ message: { request: "stop" } })
      this.plugin1.hangup()
    },
    // Reset data.params to null 
    onCleanup() {
      Janus.log(" ::: Got a cleanup notification :::");
      this.stream = null
      this.status = null
      this.remoteTracks = {}
      this.remoteVideos = 0
      this.error = null
      Janus.log(" ::: Got a cleanup notification :::");
      this.stream1 = null
      this.status1 = null
      this.remoteTracks1 = {}
      this.remoteVideos1 = 0
      this.error1 = null
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


  created() {
    // สร้าง reference ไปยัง counter ซึ่งเป็น root node ของ reatime database

  },
  beforeDestroy() {
    // ยกเลิก subsciption เมื่อ component ถูกถอดจาก dom

  }
};
</script>
<style scoped>
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