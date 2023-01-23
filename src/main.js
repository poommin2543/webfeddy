import Vue from 'vue'
import App from './App.vue'
import router from './router'
import * as VueGoogleMaps from "vue2-google-maps"
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'
import VueGamepad from 'vue-gamepad';
import VueSidebarMenuAkahon from "vue-sidebar-menu-akahon";

Vue.component('vue-sidebar-menu-akahon', VueSidebarMenuAkahon);
Vue.use(VueGamepad);
Vue.use(VueMaterial)
Vue.config.productionTip = false
Vue.use(VueGoogleMaps, {
  load: {
    key: "AIzaSyD553x-on9CsDmxWaD3rfKg2l3MX48kov8",
    // libraries: "places"
    libraries: "places,drawing,visualization"
  }
});
new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
