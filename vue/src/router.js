import VueRouter from 'vue-router'

import homepage from './components/pages/Home.vue'
import matchlistpage from './components/pages/MatchList.vue'
import loginpage from './components/pages/Login.vue'
import registerpage from './components/pages/Register.vue'
import usercenterpage from './components/pages/UserCenter.vue'
import creatematch from './components/pages/CreateMatch.vue'
import listpage from './components/pages/List.vue'


import createdmatch from './components/usercenter/CreatedMatch.vue'
import joinedmatch from './components/usercenter/JoinedMatch.vue'
import judgedmatch from './components/usercenter/JudgedMatch.vue'
import staredmatch from './components/usercenter/StaredMatch.vue'
import userinfo from './components/usercenter/UserInfo.vue'

import uploadbutton from './components/operation/Upload.vue'

var router = new VueRouter({
  routes: [
    { path: '/', redirect: '/home' },
    { path: '/home', component: homepage },
    { path: '/matchlist', component: matchlistpage },
    { path: '/login', component: loginpage },
    { path: '/register', component: registerpage },
    { path: '/list', component: listpage },

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
    { path: '/creatematch', component: creatematch },
    { path: '/upload', component: uploadbutton}
  ]
})

export default router