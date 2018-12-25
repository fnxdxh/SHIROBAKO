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
import store from './store';



var router = new VueRouter({
  routes: [
    { path: '/', redirect: '/home' },
    { path: '/home', component: homepage },
    { path: '/matchlist', component: matchlistpage },
    { path: '/login', component: loginpage,},
    { path: '/register', component: registerpage },
    { path: '/list', component: listpage },

    {
      path: '/usercenter',
      component: usercenterpage,
      meta:{
        islogin:false,
      },
      children: [
        { path: '', redirect: 'joined' },
        { path: 'created', component: createdmatch, meta:{islogin:false}},
        { path: 'joined', component: joinedmatch, meta:{islogin:false} },
        { path: 'judged', component: judgedmatch, meta:{islogin:false} },
        { path: 'stared', component: staredmatch, meta:{islogin:false} },
        { path: 'userinfo', component: userinfo, meta:{islogin:false} }
      ]
    },
    { path: '/creatematch', component: creatematch, meta:{islogin:false} },
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