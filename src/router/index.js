import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
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
