import Vue from 'vue'
import Vuex from 'vuex'
import router from './router.js'

Vue.use(Vuex)

var store = new Vuex.Store({
    state: {
      islogin: false,
      identify: 0, //0表示未登录，1表示参赛者，2是主办方，3是评委
    },
    mutations: {
      login(state, identify) {
        state.identify = identify;
        state.islogin = true;
      }
      
    }
  })

export default store