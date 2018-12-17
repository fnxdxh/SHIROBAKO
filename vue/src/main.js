import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App.vue'
import VueRouter from 'vue-router'
import router from './router.js'
import VueResource from 'vue-resource'
import Vuex from 'vuex'

Vue.use(ElementUI)
Vue.use(VueRouter)
Vue.use(VueResource)
Vue.use(Vuex)

var store = new Vuex.Store({
  state: {
    islogin: false,
    users: [{
      username: 'admin',
      pwd: 'admin'
    }],
    matches: [

    ]
  },
  mutations: {
    login(state, logininfo) {
      //先假定没有登录
      var flag = false
      state.users.some(user => {
        if (user.username === logininfo.username) {
          if (user.pwd === logininfo.pwd) {
            state.islogin = true
            flag = true
            router.push({
              path: '/usercenter'
            })
            alert("登录成功")
            return true
          } else {
            flag = true
            alert("密码错误，请重试")
            return true
          }
        }
      })

      if (!flag) {
        alert("没有注册，请先注册")
      }
    },
    logout(state) {
      state.islogin = false
    },
    register(state, reginfo) {
      //用flag来标志该用户名是否已被注册
      var flag = true
      state.users.every(user => {
        if (user.username === reginfo.username) {
          alert("该用户名已被注册")
          flag = false
          return false
        }
      })

      if (flag) {
        state.users.push(reginfo)
        alert('注册成功，请重新登录')
        router.push({path: '/login'})
      }
    }
  }
})

new Vue({
  el: '#app',
  render: h => h(App),
  router,
  store
})