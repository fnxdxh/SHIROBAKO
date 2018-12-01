import VueRouter from 'vue-router'

import homepage from './components/pages/Home.vue'
import loginpage from './components/pages/Login.vue'
import registerpage from './components/pages/Register.vue'
import usercenterpage from './components/pages/UserCenter.vue'
import creatematch from './components/pages/CreateMatch.vue'

import createdmatch from './components/usercenter/CreatedMatch.vue'
import joinedmatch from './components/usercenter/JoinedMatch.vue'
import judgedmatch from './components/usercenter/JudgedMatch.vue'
import staredmatch from './components/usercenter/StaredMatch.vue'
import userinfo from './components/usercenter/UserInfo.vue'

var router = new VueRouter({
  routes: [
    { path: '/', redirect: '/home' },
    { path: '/home', component: homepage },
    { path: '/login', component: loginpage },
    { path: '/register', component: registerpage },
    {
      path: '/usercenter',
      component: usercenterpage,
      children: [
        { path: '', redirect: 'joined' },
        { path: 'created', component: createdmatch },
        { path: 'joined', component: joinedmatch },
        { path: 'judged', component: judgedmatch },
        { path: 'stared', component: staredmatch },
        { path: 'userinfo', component: userinfo }
      ]
    },
    { path: '/creatematch', component: creatematch }
  ]
})

export default router