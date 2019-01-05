import VueRouter from 'vue-router'

import homepage from './components/pages/Home.vue'
import matchlistpage from './components/pages/MatchList.vue'
import loginpage from './components/pages/Login.vue'
import registerpage from './components/pages/Register.vue'
import usercenterpage_competitor from './components/pages/UserCenter_competitor.vue'
import usercenterpage_organizer from './components/pages/UserCenter_organizer.vue'
import usercenterpage_jury from './components/pages/UserCenter_jury.vue'
import creatematch from './components/pages/CreateMatch.vue'
import matchinfopage from './components/pages/MatchInfo.vue'
import judgematch from './components/pages/JudgeMatch.vue'

import adminlogin from './components/admin/AdminLogin.vue'
import admincenter from './components/admin/AdminCenter.vue'

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
import store from './store.js';
import invitejury from './components/pages/JuryInvite.vue'

import orgmatch from './components/pages/OrgMatchInfo.vue'



var router = new VueRouter({
  routes: [
    { path: '/', redirect: '/home' },
    { path: '/home', component: homepage },
    { path: '/matchlist', component: matchlistpage },
    { path: '/matchinfo/:competition',name: 'info', component: matchinfopage },
    { path: '/matchinfo_other/:competition',name: 'info_other', component: orgmatch },
    { path: '/admin', component: adminlogin},
    { path: '/admincenter', component: admincenter},
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

    {
      path: '/usercenter_competitor',
      component: usercenterpage_competitor,
      children: [
        { path: '', redirect: 'joined' },
        { path: 'joined', component: joinedmatch, meta:{islogin:false} },
        { path: 'stared', component: staredmatch, meta:{islogin:false} },
        { path: 'userinfo', component: userinfo, meta:{islogin:false} }
      ]
    },
    {
      path: '/usercenter_organizer',
      component: usercenterpage_organizer,
      children: [
        { path: '', redirect: 'created' },
        { path: 'created', component: createdmatch, meta:{islogin:false}},
        { path: 'stared', component: staredmatch, meta:{islogin:false} },
        { path: 'userinfo', component: userinfo, meta:{islogin:false} }
      ]
    },
    {
      path: '/usercenter_jury',
      component: usercenterpage_jury,
      children: [
        { path: '', redirect: 'judged' },
        { path: 'judged', component: judgedmatch, meta:{islogin:false} },
        { path: 'stared', component: staredmatch, meta:{islogin:false} },
        { path: 'userinfo', component: userinfo, meta:{islogin:false} }
      ]
    },
    { path: '/creatematch', component: creatematch, meta:{islogin:false} },
    { path: '/judgematch/:competition',name: 'judge' , component: judgematch, meta:{islogin:false}},
    { path: '/invitejury/:competition',name: 'invite' , component: invitejury, meta:{islogin:false}}
  ]
});

router.beforeEach(function(to,from,next){
  if(to.matched.some(record=>record.meta.islogin)){
    if(store.state.islogin){
      next();
    }
    else{
      next({path:'/login',query:{redirect:to.fullPath}});
    }
  }
  else{
    next();
  }
});
export default router