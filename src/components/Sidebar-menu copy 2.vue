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
                <!-- <i v-if="isExitButton" class="bx bx-log-out" id="log_out" @click.stop="$emit('button-exit-clicked')" /> -->
            </div>

            <div>
                <p class="titleheader"> Rover list</p>
                <div class="cardframe blackcardframe">
                    <v-list>
                        <div class="center">
                            <!-- <v-subheader>REPORTS</v-subheader> -->
                            <v-list-item-group v-model="selectedItem" color="primary">
                                <v-list-item v-for="(item, i) in items" :key="i" @click="updateSelected(item)">
                                    <v-list-item-content>
                                        <v-list-item-title v-text="item.text"></v-list-item-title>
                                    </v-list-item-content>
                                </v-list-item>
                            </v-list-item-group>
                        </div>
                    </v-list>
                    <!-- <p class="title">Rover No.001</p> -->


                </div>
                <div>
                    <div class="cardframe blackcardframe">
                        <p>Rover status</p>
                        <div class="cardframemini Trancardframe">
                            <p>Noom</p>
                            <div class="title">
                                <p>Noom</p>
                            </div>
                        </div>
                        <p>Order tatus</p>
                        <div class="cardframeminize Trancardframe">

                        </div>

                    </div>

                </div>
                <div class="cardbutton">
                    <button type="button" class="buttondrive" :class="isOpened ? 'buttondrive' : 'buttondriveclose'"
                        @click="isActive = !isActive">Auto</button>
                    <div v-if="isActive">
                        <button type="button" class="buttondrive" @click="clicked">Light</button>
                    </div>
                </div>

            </div>


        </div>
    </div>
</template>

<script>
import firebaseApp from './firebase'
// import ComponentA from '../components/ListRover.vue'

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
            isActive: true,
            rover: "",
            selectedItem: 1,
            items: [
                // { text: 'Real-Time', icon: 'mdi-clock' },
                // { text: 'Audience', icon: 'mdi-account' },
                // { text: 'Conversions', icon: 'mdi-flag' },
            ],
            itemrover: {},


        }
    },
    mounted() {
        this.isOpened = this.isMenuOpen
        this.dbRef.on('value', ss => {
            // console.log(ss.val());
            this.items = []
            // this.items.remove()
            for (const [key] of Object.entries(ss.val())) {
                // console.log(`${key}: ${value}`);
                console.log(`${key}`);

                this.items.push({
                    text: key,
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
            console.log(totoal);
        }
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
        // สร้าง reference ไปยัง counter ซึ่งเป็น root node ของ reatime database
        this.dbRef = firebaseApp.database().ref('/')
        // this.dbRef1 = firebaseApp.database().ref('Rover1/location/user')

    },



    beforeDestroy() {
        // ยกเลิก subsciption เมื่อ component ถูกถอดจาก dom
        this.dbRef.off()
        // this.dbRef1.off()
    }
}
</script>

<style>
/* Google Font Link */






.sidebar {
    position: relative;
    display: flex;
    flex-direction: column;
    position: fixed;
    left: 0;
    top: 0;
    height: 100%;
    min-height: min-content;
    /* overflow-y: auto; */
    width: 78px;
    background: var(--bg-color);
    /* padding: 6px 14px 0 14px; */
    z-index: 99;
    transition: all 0.5s ease;
}

.sidebar.open {
    width: 250px;
}

.sidebar .logo-details {
    height: 60px;
    display: flex;
    align-items: center;
    position: relative;
}

.sidebar .logo-details .icon {
    opacity: 0;
    transition: all 0.5s ease;
}

.sidebar .logo-details .logo_name {
    color: var(--logo-title-color);
    font-size: 20px;
    font-weight: 600;
    opacity: 0;
    transition: all 0.5s ease;
}

.sidebar.open .logo-details .icon,
.sidebar.open .logo-details .logo_name {
    opacity: 1;
}

.sidebar .logo-details #btn {
    position: absolute;
    top: 50%;
    right: 0;
    transform: translateY(-50%);
    font-size: 22px;
    transition: all 0.4s ease;
    font-size: 23px;
    text-align: center;
    cursor: pointer;
    transition: all 0.5s ease;
}

.sidebar.open .logo-details #btn {
    text-align: right;
}

.sidebar i {
    color: var(--icons-color);
    height: 60px;
    min-width: 50px;
    font-size: 28px;
    text-align: center;
    line-height: 60px;
}

.sidebar .nav-list {
    margin-top: 20px;
    /* margin-bottom: 60px; */
    /* height: 100%; */
    /* min-height: min-content; */
}

.sidebar li {
    position: relative;
    margin: 8px 0;
    list-style: none;
}

.sidebar li .tooltip {
    position: absolute;
    top: -20px;
    left: calc(100% + 15px);
    z-index: 3;
    background: var(--items-tooltip-color);
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.3);
    padding: 6px 12px;
    border-radius: 4px;
    font-size: 15px;
    font-weight: 400;
    opacity: 0;
    white-space: nowrap;
    pointer-events: none;
    transition: 0s;
}

.sidebar li:hover .tooltip {
    opacity: 1;
    pointer-events: auto;
    transition: all 0.4s ease;
    top: 50%;
    transform: translateY(-50%);
}

.sidebar.open li .tooltip {
    display: none;
}

.sidebar input {
    font-size: 15px;
    color: var(--serach-input-text-color);
    font-weight: 400;
    outline: none;
    height: 50px;
    width: 100%;
    width: 50px;
    border: none;
    border-radius: 12px;
    transition: all 0.5s ease;
    background: var(--secondary-color);
}

.sidebar.open input {
    padding: 0 20px 0 50px;
    width: 100%;
}

.sidebar .bx-search {
    position: absolute;
    top: 50%;
    left: 0;
    transform: translateY(-50%);
    font-size: 22px;
    background: var(--secondary-color);
    color: var(--icons-color);
}

.sidebar.open .bx-search:hover {
    background: var(--secondary-color);
    color: var(--icons-color);
}

.sidebar .bx-search:hover {
    background: var(--menu-items-hover-color);
    color: var(--bg-color);
}

.sidebar li a {
    display: flex;
    height: 100%;
    width: 100%;
    border-radius: 12px;
    align-items: center;
    text-decoration: none;
    transition: all 0.4s ease;
    background: var(--bg-color);
}

.sidebar li a:hover {
    background: var(--menu-items-hover-color);
}

.sidebar li a .links_name {
    color: var(--menu-items-text-color);
    font-size: 15px;
    font-weight: 400;
    white-space: nowrap;
    opacity: 0;
    pointer-events: none;
    transition: 0.4s;
}

.sidebar.open li a .links_name {
    opacity: 1;
    pointer-events: auto;
}

.sidebar li a:hover .links_name,
.sidebar li a:hover i {
    transition: all 0.5s ease;
    color: var(--bg-color);
}

.sidebar li i {
    height: 50px;
    line-height: 50px;
    font-size: 18px;
    border-radius: 12px;
}

.sidebar div.profile {
    position: relative;
    height: 60px;
    width: 78px;
    /* left: 0;
    bottom: 0; */
    padding: 10px 14px;
    background: var(--secondary-color);
    transition: all 0.5s ease;
    overflow: hidden;
}

.sidebar.open div.profile {
    width: 250px;
}

.sidebar div .profile-details {
    display: flex;
    align-items: center;
    flex-wrap: nowrap;
}

.sidebar div img {
    height: 45px;
    width: 45px;
    object-fit: cover;
    border-radius: 6px;
    margin-right: 10px;
}

.sidebar div.profile .name,
.sidebar div.profile .job {
    font-size: 15px;
    font-weight: 400;
    color: var(--menu-footer-text-color);
    white-space: nowrap;
}

.sidebar div.profile .job {
    font-size: 12px;
}

.sidebar .profile #log_out {
    position: absolute;
    top: 50%;
    right: 0;
    transform: translateY(-50%);
    background: var(--secondary-color);
    width: 100%;
    height: 60px;
    line-height: 60px;
    border-radius: 0px;
    transition: all 0.5s ease;
}

.sidebar.open .profile #log_out {
    width: 50px;
    background: var(--secondary-color);
    opacity: 0;
}

.sidebar.open .profile:hover #log_out {
    opacity: 1;
}

.sidebar.open .profile #log_out:hover {
    opacity: 1;
    color: red;
}

.sidebar .profile #log_out:hover {
    color: red;
}

.home-section {
    position: relative;
    background: var(--home-section-color);
    min-height: 100vh;
    top: 0;
    left: 78px;
    width: calc(100% - 78px);
    transition: all 0.5s ease;
    z-index: 2;
}

.sidebar.open~.home-section {
    left: 250px;
    width: calc(100% - 250px);
}

.home-section .text {
    display: inline-block;
    color: var(--bg-color);
    font-size: 25px;
    font-weight: 500;
    margin: 18px;
}

.my-scroll-active {
    overflow-y: auto;
}

#my-scroll {
    overflow-y: auto;
    height: calc(100% - 60px);
}

#my-scroll::-webkit-scrollbar {
    display: none;
    /* background-color: rgba(255, 255, 255, 0.2); 
    width: 10px;
    border-radius:5px  */
}

.card {
    border-radius: 70px;
    box-shadow: 0 4px 80px 10 rgba(255, 255, 255, 0.2);
    max-width: 200px;
    margin: auto;
    text-align: center;
    opacity: 1;
}

.cardframe {
    height: 250px;
    max-width: 200px;
    border-radius: 25px;
    text-align: center;
    margin: auto;
}

.cardframemini {
    height: 150px;
    max-width: 180px;
    border-radius: 25px;
    text-align: center;
    margin: auto;
}

.cardframeminize {
    height: 100px;
    max-width: 180px;
    border-radius: 25px;
    text-align: center;
    margin: auto;
}

.blackcardframe {
    background: #ffffff;
}

.Trancardframe {
    border: 2px solid #50504e;
}

.title {
    color: rgb(14, 13, 13);
    font-size: 18px;
}

.titleheader {
    color: rgb(255, 255, 255);
    font-size: 25px;
}

.buttondrive {
    background: linear-gradient(to bottom, #ffffff 5%, #ffffff 100%);
    background-color: #ffffff;
    border-radius: 18px;
    /* cursor: pointer; */
    color: #404040;
    font-family: Arial;
    font-size: 28px;
    font-weight: bold;
    /* padding: 16px 31px; */
    max-width: 200px;
    width: 100px;
    height: 50px;
    /* display: flex; */
    /* align-items: center; */
    /* flex-wrap: nowrap; */
    margin: auto;
}

.buttondriveclose {
    background: linear-gradient(to bottom, #ffffff 5%, #ffffff 100%);
    background-color: #ffffff;
    border-radius: 18px;
    /* cursor: pointer; */
    color: #404040;
    font-family: Arial;
    font-size: 28px;
    font-weight: bold;
    /* padding: 16px 31px; */
    max-width: 200px;
    height: 50px;
    /* display: flex; */
    /* align-items: center; */
    /* flex-wrap: nowrap; */
    margin: auto;
}

.cardbutton {
    height: 150px;
    max-width: 200px;
    border-radius: 25px;
    text-align: center;
    margin: auto;
}

.buttondrive #log_out {
    position: absolute;
    top: 50%;
    right: 0;
    transform: translateY(-50%);
    background: var(--secondary-color);
    width: 100%;
    height: 60px;
    line-height: 60px;
    border-radius: 0px;
    transition: all 0.5s ease;
}


.buttondrive:hover {
    background: linear-gradient(to bottom, #ffffff 5%, #ffffff 100%);
    background-color: #ffffff;
}

.buttondrive:active {
    position: relative;
    top: 1px;
}

a {
    text-decoration: none;
    font-size: 22px;
    color: black;
}

button:hover,
a:hover {
    opacity: 1.5;
}

.v-list {
    height: 200px;
    /* or any height you want */
    overflow-y: auto;
    /* border-radius: 25px; */
    /* margin-left: auto;
    margin-right: auto; */
}

.center {
    /* margin: 0; */
    /* position: absolute; */
    align-items: center;
    top: 50%;
    left: 50%;
    /* display: block; */
    margin: auto;
    /* width: auto; */
    /* -ms-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%); */
    transform: translatey(10%);
}
</style>
