import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App.vue'
import VueRouter from 'vue-router'
import router from './router.js'
import VueResource from 'vue-resource'
import Vuex from 'vuex'
import store from './store.js'

Vue.use(ElementUI)
Vue.use(VueRouter)
Vue.use(VueResource)
Vue.use(Vuex)



new Vue({
  el: '#app',
  render: h => h(App),
  router,
  store
})