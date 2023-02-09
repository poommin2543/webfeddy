<template>

    <div class="sidebar" :class="isOpened ? 'open' : ''" :style="cssVars">

        <div class="logo-details" style="margin: 6px 14px 0 14px;">

            <!-- <img v-if="menuLogo" :src="menuLogo" alt="menu-logo" class="menu-logo icon">
            <i v-else class="bx icon" :class="menuIcon" />
            <div class="logo_name">
                {{ menuTitle }}
            </div> -->
            <i class="bx" :class="isOpened ? 'bx-menu-alt-right' : 'bx-menu'" id="btn" @click="isOpened = !isOpened" />
        </div>

        <div
            style="display: flex ; flex-direction:column; justify-content: space-between; flex-grow: 1; max-height: calc(100% - 60px); ">
            <div v-if="isLoggedIn" class="profile">
                <div class="profile-details">
                    <img v-if="profileImg" :src="profileImg" alt="profileImg">
                    <i v-else class="bx bxs-user-rectangle" />
                    <div class="name_job">
                        <div class="name">
                            {{ profileName }}
                        </div>
                        <div class="job">
                            {{ profileRole }}
                        </div>
                    </div>
                </div>
                <i v-if="isExitButton" class="bx bx-log-out" id="log_out" @click.stop="$emit('button-exit-clicked')" />
            </div>

            <div>
                <p class="titleheader"> Rover list</p>
                <div class="cardframe blackcardframe">
                    <v-list>
                        <div class="center">
                            <!-- <v-subheader></v-subheader> -->
                            <v-list-item-group v-model="selectedItem" color="primary">
                                <v-list-item v-for="(item, i) in items" :key="i" @click="updateSelected(item)">
                                    <v-list-item-content>
                                        <!-- <v-list-item-title v-text="item.text"></v-list-item-title> -->
                                        <p>{{ item.Name }}</p>
                                    </v-list-item-content>
                                </v-list-item>
                            </v-list-item-group>
                        </div>
                    </v-list>
                    <!-- <p class="title">Rover No.001</p> -->


                </div>
                <div>
                    <div class="cardframe blackcardframe">
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
                            <p>Location: </p>
                        </div>


                    </div>

                </div>
                <div class="cardbutton">
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
                        <button type="button" v-gamepad:button-a="pressedA"
                            v-gamepad:button-a.released="releasedA"></button>
                        <button type="button" v-gamepad:button-x="pressedX"
                            v-gamepad:button-x.released="releasedX"></button>
                        <button type="button" v-gamepad:button-y="pressedY"
                            v-gamepad:button-y.released="releasedY"></button>
                        <button type="button" v-gamepad:button-b="pressedB"
                            v-gamepad:button-b.released="releasedB"></button>
                        <button type="button" v-gamepad:shoulder-left="pressedReset"
                            v-gamepad:shoulder-left.released="releasedReset" v-on:click="pressedReset"></button>
                    </div>
                </div>

            </div>
            <div class="center">

                <!-- <img  v-if="profileImg" :src="profileImg" alt="profileImg"> -->

            </div>
        </div>
    </div>
</template>

<script>
import firebaseApp from './firebase'
// import ComponentA from '../components/ListRover.vue'
import mqtt from 'mqtt/dist/mqtt'

export default {
    name: 'SidebarMenuAkahon',
    return: {
        //         components: {
        //             ComponentA: ComponentA
        //   }
    },
    props: {
        //! Menu settings

        isMenuOpen: {
            type: Boolean,
            default: true,
        },

        isBottonAuto: {
            type: Boolean,
            default: false,
        },

        isPaddingLeft: {
            type: Boolean,
            default: true,
        },
        menuOpenedPaddingLeftBody: {
            type: String,
            default: '250px'
        },
        menuClosedPaddingLeftBody: {
            type: String,
            default: '78px'
        },

        //! Menu items


        //! Search


        //! Profile detailes
        profileImg: {
            type: String,
            default: require('../assets/img/poommin.jpg'),
        },
        LogoImg: {
            type: String,
            default: require('../assets/img/poommin.jpg'),
        },
        profileName: {
            type: String,
            default: 'Poommin PhinPhimai',
        },
        profileRole: {
            type: String,
            default: 'Frontend developer',
        },
        isExitButton: {
            type: Boolean,
            default: true,
        },
        isLoggedIn: {
            type: Boolean,
            default: true,
        },

        //! Styles
        bgColor: {
            type: String,
            default: '#11101d',
        },
        secondaryColor: {
            type: String,
            default: '#1d1b31',
        },
        homeSectionColor: {
            type: String,
            default: '#e4e9f7',
        },
        logoTitleColor: {
            type: String,
            default: '#fff',
        },
        iconsColor: {
            type: String,
            default: '#fff',
        },
        itemsTooltipColor: {
            type: String,
            default: '#e4e9f7',
        },
        searchInputTextColor: {
            type: String,
            default: '#fff',
        },
        menuItemsHoverColor: {
            type: String,
            default: '#fff',
        },
        menuItemsTextColor: {
            type: String,
            default: '#fff',
        },
        menuFooterTextColor: {
            type: String,
            default: '#fff',
        },

    },
    data() {
        return {
            isOpened: true,
            isActive: false,
            isActiveJoy: false,
            rover: "",
            selectedItem: 1,
            items: [
                // { text: 'Real-Time', icon: 'mdi-clock' },
                // { text: 'Audience', icon: 'mdi-account' },
                // { text: 'Conversions', icon: 'mdi-flag' },
            ],
            itemrover: {},
            namerover: "N/a",
            StatusRover: "N/a",
            Battery: "N/a",
            Velocity: "N/a",
            timeone: 0,
            timemqtt: 0,
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
                qos: 0,
                topic: 'rover1/status',
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
            refBattery: false,
            refJoystick: false,
            // Joy,
            textA: "A",
            textB: "B",
            textX: "X",
            textY: "Y",
            textLB: "Reset",

        }
    },
    mounted() {
        this.createConnection()

        // this.doSubscribe()
        this.interval = setInterval(() => this.Checkonline(), 3000);
        this.isOpened = this.isMenuOpen
        this.dbRef.on('value', ss => {
            // console.log(ss.val());
            this.items = []
            // this.items.remove()
            for (const [key] of Object.entries(ss.val())) {
                // console.log(`${key}: ${value}`);
                // console.log(`${key}`);

                this.items.push({
                    Name: key,
                });
            }
        })
    },
    methods: {
        toggle() {
            if (!this.isBottonAuto) {
                this.isBottonAuto == true;
            } else {
                this.isBottonAuto == false;
            }
        },
        clicked() {
            if (!this.isActive) {
                this.isActive = true;
            } else {
                this.isActive = false;
            }
            console.log(this.isActive);
            // this.isActive = this.isActive ? false : true;
        },
        updateSelected(totoal) {
            console.log(totoal)
            this.doUnSubscribe()
            if (this.refBattery == true) {
                this.dbRefBattery.off()
                this.refBattery = false;
            }
            if (this.refJoystick == true) {
                this.dbRefJoystick.off()
                this.refJoystick = false;
            }
            var refStatus = "";
            // this.yourFunction()
            for (const [key, value] of Object.entries(totoal)) {
                if (key === 'Name') {
                    // var decodedStringBtoA = value;

                    // Encode the String
                    var encodedStringBtoA = btoa(value);
                    localStorage.setItem("name-Rover", encodedStringBtoA);
                    this.namerover = value;
                    this.subscription = [];
                    // this.subscription.push({
                    //     // topic: value.toLowerCase() + '/status',
                    //     topic:  '/status',
                    //     qos: 0,
                    // })
                    this.subscription = {
                        qos: 0,
                        topic: value.toLowerCase() + '/status'
                    }
                    this.doSubscribe();
                    refStatus = "/" + value + '/status'
                    this.dbRefBattery = firebaseApp.database().ref(refStatus)

                    this.refBattery = true;
                    this.dbRefBattery.on('value', ss => {
                        for (const [key, value] of Object.entries(ss.val())) {
                            // console.log(`${key}: ${value}`);
                            if (key == 'Battery') {

                                // console.log(`${key}: ${value}`);
                                this.Battery = value + ' %'
                            }
                            if (key == 'velocity') {

                                // console.log(`${key}: ${value}`);
                                this.Velocity = value + ' m/s'
                            }

                        }
                    })
                }
                // if (this.subscribeSuccess === false) {
                //     this.doSubscribe();
                //     console.log(this.subscribeSuccess)
                // }
                // else {
                //     this.doUnSubscribe();
                //     console.log(this.subscribeSuccess)
                // }

            }

        },
        Checkonline() {

            if ((this.timenow() - this.timemqtt) > 0.1) {
                // console.log("Offline", (this.timenow() - this.timemqtt) * 60)
                this.StatusRover = "offline"
            }

        },
        timenow() {

            var one_day = 60 * 60 * 24
            const today = new Date();
            // this.timeone=today/one_day
            return today / one_day
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
                        this.StatusRover = message
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
            const { topic, qos } = this.
                subscription
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
        joystick() {
            this.isActiveJoy = !this.isActiveJoy
            if (this.isActiveJoy == true) {
                console.log("/" + this.namerover + '/control')
                this.dbRefJoystick = firebaseApp.database().ref("/" + this.namerover + '/control')
                this.refJoystick == true
            }
        },
        pressedA(e) {
            this.textA = "Click";
            console.log(`pressA`, e);
            this.dbRefJoystick.set({
                forword: 0,
                backword: 1,
                right: 0,
                left: 0
            });
        },
        releasedA() {
            this.textA = "A";
            this.dbRefJoystick.set({
                forword: 0,
                backword: 0,
                right: 0,
                left: 0
            });
        },
        pressedX(e) {
            this.textX = "Click";
            console.log(`pressX`, e);
            this.dbRefJoystick.set({
                forword: 0,
                backword: 0,
                right: 0,
                left: 1
            });

        },
        releasedX() {
            this.textX = "X";
            this.dbRefJoystick.set({
                forword: 0,
                backword: 0,
                right: 0,
                left: 0
            });
        },
        pressedY(e) {
            this.textY = "Click";
            console.log(`pressY`, e);
            this.dbRefJoystick.set({
                forword: 1,
                backword: 0,
                right: 0,
                left: 0
            });
        },
        releasedY() {
            this.textY = "Y";
            this.dbRefJoystick.set({
                forword: 0,
                backword: 0,
                right: 0,
                left: 0
            });
        },
        pressedB(e) {
            this.textB = "Click";
            console.log(`pressB`, e);
            this.dbRefJoystick.set({
                forword: 0,
                backword: 0,
                right: 1,
                left: 0
            });
        },
        releasedB() {
            this.textB = "B";
            this.dbRefJoystick.set({
                forword: 0,
                backword: 0,
                right: 0,
                left: 0
            });
        },
        pressedReset(e) {
            this.textLB = "Click";
            console.log(`pressLB`, e);
            this.dbRefJoystick.set({
                forword: 0,
                backword: 0,
                right: 0,
                left: 0
            });
        },
        releasedReset() {
            this.textLB = "Reset";
            this.dbRefJoystick.set({
                forword: 0,
                backword: 0,
                right: 0,
                left: 0
            });
        },
    },
    computed: {
        cssVars() {
            return {
                // '--padding-left-body': this.isOpened ? this.menuOpenedPaddingLeftBody : this.menuClosedPaddingLeftBody,
                '--bg-color': this.bgColor,
                '--secondary-color': this.secondaryColor,
                '--home-section-color': this.homeSectionColor,
                '--logo-title-color': this.logoTitleColor,
                '--icons-color': this.iconsColor,
                '--items-tooltip-color': this.itemsTooltipColor,
                '--serach-input-text-color': this.searchInputTextColor,
                '--menu-items-hover-color': this.menuItemsHoverColor,
                '--menu-items-text-color': this.menuItemsTextColor,
                '--menu-footer-text-color': this.menuFooterTextColor,
            }
        },
    },
    watch: {
        isOpened() {
            window.document.body.style.paddingLeft = this.isOpened && this.isPaddingLeft ? this.menuOpenedPaddingLeftBody : this.menuClosedPaddingLeftBody
        }
    },
    created() {
        console.log("created()");
        // สร้าง reference ไปยัง counter ซึ่งเป็น root node ของ reatime database
        this.dbRef = firebaseApp.database().ref('/')
        // this.dbRefBattery = firebaseApp.database().ref('/Rover1/status')
        // this.dbRef1 = firebaseApp.database().ref('Rover1/location/user')

    },



    beforeDestroy() {
        console.log("beforeDestroy()");
        // ยกเลิก subsciption เมื่อ component ถูกถอดจาก dom
        this.dbRef.off()
        this.dbRefBattery.off()
        // this.dbRef1.off()
    }
}
</script>

<style scoped src="@/assets/styles/styles-Sidebar.css">
</style>
