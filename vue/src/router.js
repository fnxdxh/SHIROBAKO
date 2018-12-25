import VueRouter from 'vue-router'

import homepage from './components/pages/Home.vue'
import matchlistpage from './components/pages/MatchList.vue'
import loginpage from './components/pages/Login.vue'
import registerpage from './components/pages/Register.vue'
import usercenterpage from './components/pages/UserCenter.vue'
import creatematch from './components/pages/CreateMatch.vue'
import listpage from './components/pages/List.vue'

import competitor_register from './components/dialog/register_competitor.vue'
import organizer_register from './components/dialog/register_organizer.vue'
import jury_register from './components/dialog/register_jury.vue'
import competitor_login from './components/dialog/login_competitor.vue'
import organizer_login from './components/dialog/login_organizer.vue'
import jury_login from './components/dialog/login_jury.vue'

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
    { path: '/login', component: loginpage,
      children: [
        {path: '', redirect: 'competitor'},
        {path: 'competitor', component: competitor_login},
        {path: 'organizer', component: organizer_login},
        {path: 'jury', component: jury_login}
      ]
    },
    { path: '/register', component: registerpage,
      children: [
        {path: '', redirect: 'competitor'},
        {path: 'competitor', component: competitor_register},
        {path: 'organizer', component: organizer_register},
        {path: 'jury', component: jury_register}
      ]
    },
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