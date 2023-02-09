import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ControlView from '../views/ControlView.vue'
// import HomehomeView from '../views/HomehomeView.vue'
import { BootstrapVue } from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
// import VueSidebarMenu from "vue-sidebar-menu";
// import "vue-sidebar-menu/dist/vue-sidebar-menu.css";
// import VueSidebarMenu from 'vue-sidebar-menu'
// import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'
// Vue.use(VueSidebarMenu)

Vue.use(BootstrapVue);
// Vue.use(VueSidebarMenu);
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'ControlView',
    component: ControlView
  },
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  {
    path: '/Streaming',
    name: 'Streaming',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/StreamingView.vue')
  },
  {
    path: '/Test',
    name: 'Test',
    component: () => import('../views/PushdataView.vue')
  },
  {
    path: '/MultiCamera',
    name: 'MultiCamera',
    component: () => import('../components/Muticamera.vue')
  },
  {
    path: '/Login',
    name: 'Login',
    component: () => import('../views/LoginView.vue')
  },
  {
    path: '/Mqtt',
    name: 'Mqtt',
    component: () => import('../components/Mqttjs.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
