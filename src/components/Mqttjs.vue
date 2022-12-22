<template>
  <div>
    <p>NoomMqtt</p>
    <p>{{text}}</p>
  </div>
</template>

<script>
import mqtt from 'mqtt/dist/mqtt'
// var lastVisit = new Date(getLastVisit());

// var thirtyMinutes = 30 * 60000; // 60000 being the number of milliseconds in a minute
// var now = new Date();
// var thirtyMinutesAgo = new Date(now - thirtyMinutes);
// console.log(lastVisit,thirtyMinutesAgo)
// One day Time in s (seconds)
var one_day =  60 * 60 * 24
const today = new Date();
// const date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
// const time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
// const dateTime = date +' '+ time;
console.log(today/one_day)

export default {
  name: 'MqttController',

  data() {
    return {
      text:"NNnnnnnnnnnnnnnnnnnnnNN",
      timeone:0,
      timemqtt:0,
      connection: {
        protocol: 'ws',
        host: '34.143.225.243',
        // ws: 8083; wss: 8084
        port: 9001,
        endpoint: '/mqtt',
        // for more options, please refer to https://github.com/mqttjs/MQTT.js#mqttclientstreambuilder-options
        clean: true,
        connectTimeout: 30 * 1000, // ms
        reconnectPeriod: 4000, // ms
        clientId:
          'emqx_vue_' +
          Math.random()
            .toString(16)
            .substring(2, 8),
        // auth
        username: 'test',
        password: 'Test123',
      },
      subscription: {
        topic: 'rover1/status',
        qos: 0,
      },
      publish: {
        topic: 'rover1/status',
        qos: 0,
        payload: 'Hi',
      },
      receiveNews: '',
      qosList: [0, 1, 2],
      client: {
        connected: false,
      },
      subscribeSuccess: false,
      connecting: false,
      retryTimes: 0,
    }
  },
  mounted() {
    this.createConnection()
    // this.yourFunction()
    this.doSubscribe()
    // this.timenow()
    this.interval = setInterval(() => this.Checkonline(), 3000);
    
  },
  methods: {

    Checkonline(){
      
      if((this.timenow()-this.timemqtt)>0.1){
        console.log("Offline",(this.timenow()-this.timemqtt)*60)
        this.text = "offline"
      }
      
    },
    timenow(){
      
      var one_day =  60 * 60 * 24
      const today = new Date();
      // this.timeone=today/one_day
      return today/one_day
      // console.log(this.timeone)
},
    initData() {
      this.client = {
        connected: false,
      }
      this.retryTimes = 0
      this.connecting = false
      this.subscribeSuccess = false
    },
    handleOnReConnect() {
      this.retryTimes += 1
      if (this.retryTimes > 5) {
        try {
          this.client.end()
          this.initData()
          this.$message.error('Connection maxReconnectTimes limit, stop retry')
        } catch (error) {
          this.$message.error(error.toString())
        }
      }
    },
    createConnection() {
      try {
        this.connecting = true
        const { protocol, host, port, endpoint, ...options } = this.connection
        const connectUrl = `${protocol}://${host}:${port}${endpoint}`
        this.client = mqtt.connect(connectUrl, options)
        if (this.client.on) {
          this.client.on('connect', () => {
            this.connecting = false
            console.log('Connection succeeded!')
          })
          this.client.on('reconnect', this.handleOnReConnect)
          this.client.on('error', error => {
            console.log('Connection failed', error)
          })
          this.client.on('message', (topic, message) => {
            this.receiveNews = this.receiveNews.concat(message)
            console.log(`Received message ${message} from topic ${topic}`)
            // console.log(message)
            this.text = message
            // this.text = "OFF"
            this.timemqtt = this.timenow()
          })
         
        }
      } catch (error) {
        this.connecting = false
        console.log('mqtt.connect error', error)
      }
    },
    // subscribe topic
    // https://github.com/mqttjs/MQTT.js#mqttclientsubscribetopictopic-arraytopic-object-options-callback
    doSubscribe() {
      const { topic, qos } = this.subscription
      this.client.subscribe(topic, { qos }, (error, res) => {
        if (error) {
          console.log('Subscribe to topics error', error)
          return
        }
        this.subscribeSuccess = true
        console.log('Subscribe to topics res', res)
      })
    },
    // unsubscribe topic
    // https://github.com/mqttjs/MQTT.js#mqttclientunsubscribetopictopic-array-options-callback
    doUnSubscribe() {
      const { topic } = this.subscription
      this.client.unsubscribe(topic, error => {
        if (error) {
          console.log('Unsubscribe error', error)
        }
      })
    },
    // publish message
    // https://github.com/mqttjs/MQTT.js#mqttclientpublishtopic-message-options-callback
    doPublish() {
      const { topic, qos, payload } = this.publish
      this.client.publish(topic, payload, { qos }, error => {
        if (error) {
          console.log('Publish error', error)
        }
      })
    },
    // disconnect
    // https://github.com/mqttjs/MQTT.js#mqttclientendforce-options-callback
    destroyConnection() {
      if (this.client.connected) {
        try {
          this.client.end(false, () => {
            this.initData()
            console.log('Successfully disconnected!')
          })
        } catch (error) {
          console.log('Disconnect failed', error.toString())
        }
      }
    },
    handleProtocolChange(value) {
      this.connection.port = value === 'wss' ? '8084' : '8083'
    },
  },
  
}
</script>
