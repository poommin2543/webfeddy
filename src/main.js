import Vue from 'vue'
import App from './App.vue'
import * as VueGoogleMaps from "vue2-google-maps" // Import package
import router from './router'
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