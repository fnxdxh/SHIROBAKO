<template>
  <div id="app">
    <el-container>
      <el-header>
        <el-row>
          <el-col :span="3">
            <router-link to="/home">
              <img src="src\assets\images\logo.jpg">
            </router-link>
          </el-col>
          <el-col :span="8">
            <el-menu mode="horizontal" :router="true">
              <el-menu-item index="home">首页</el-menu-item>
              <el-menu-item index="matchlist">赛事</el-menu-item>
            </el-menu>
          </el-col>
          <el-col :span="5">
            <el-input placeholder="请输入内容" prefix-icon="el-icon-search"></el-input>
          </el-col>
          <el-col :span="1" :offset="3">
            <i class="el-icon-bell"></i>
          </el-col>
          <el-col :span="4">
            <div v-if="$store.state.islogin">
              <router-link to="/usercenter">
                <img src="src\assets\images\photo.jpg">
              </router-link>
            </div>
            <div v-else>
              <router-link to="/login">
                <el-button>登录</el-button>
              </router-link>
              <router-link to="/register">
                <el-button>注册</el-button>
              </router-link>
            </div>
          </el-col>
        </el-row>
      </el-header>
      <el-main>
        <router-view></router-view>
      </el-main>
      <el-footer>Footer</el-footer>
    </el-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      
    };
  }
};
</script>

<style>
</style>
