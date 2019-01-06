import Vue from 'vue'
import Vuex from 'vuex'
import router from './router.js'

Vue.use(Vuex)

var store = new Vuex.Store({
    state: {
      islogin: false,
      identify: 0, //0表示未登录，1表示参赛者，2是主办方，3是评委
      items:{username: ""},
      list: []
    },
    mutations: {
      login(state, identify) {
        state.identify = identify;
        sessionStorage.setItem("identify",identify);
        state.islogin = true;
      },
      logout(state) {
        state.identify = 0;
        sessionStorage.setItem("identify",0);
        state.islogin = false;
      },
      setSession(username){
        sessionStorage.setItem("username", username);
      },
      writelist(state, data) {
        state.list = data;
      }
    }
  })

export default store