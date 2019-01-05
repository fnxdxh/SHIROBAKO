<template>
  <div id="app">
    <el-container>
      <el-header>
        <el-row>
          <el-col :span="5">
            <router-link to="/home">
              <h3>SHIROBAKO</h3>
            </router-link>
          </el-col>
          <el-col :span="4">
            <el-menu mode="horizontal" :router="true">
              <el-menu-item index="/home">首页</el-menu-item>
              <el-menu-item index="/matchlist">赛事</el-menu-item>
            </el-menu>
          </el-col>
          <el-col :span="7">
            <el-form :inline="true" :model="formInline">
              <el-form-item>
                <el-input v-model="formInline.keyword" placeholder="请输入关键词"></el-input>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="search">搜索</el-button>
              </el-form-item>
            </el-form>
          </el-col>
          <el-col :span="1" :offset="3">
            <i class="el-icon-bell"></i>
          </el-col>
          <el-col :span="4">
            <div v-if="$store.state.identify === 1">
              <router-link to="/usercenter_competitor">
                <!-- <img src="src\assets\images\photo.jpg"> -->
                <el-button type="primary">个人中心</el-button>
              </router-link>
              <el-button type="primary" @click="logout">登出</el-button>
            </div>
            <div v-else-if="$store.state.identify === 2">
              <router-link to="/usercenter_organizer">
                <!-- <img src="src\assets\images\photo.jpg"> -->
                <el-button type="primary">个人中心</el-button>
              </router-link>
              <el-button type="primary" @click="logout">登出</el-button>
            </div>
            <div v-else-if="$store.state.identify === 3">
              <router-link to="/usercenter_jury">
                <!-- <img src="src\assets\images\photo.jpg"> -->
                <el-button type="primary">个人中心</el-button>
              </router-link>
              <el-button type="primary" @click="logout">登出</el-button>
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
      <el-footer id="footer"></el-footer>
    </el-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      formInline: {
        keyword: ''
      }
    };
  },
  methods: {
    search() {
      this.$http.post("api/search/", {to_search: this.formInline.keyword}).then(result => {
        this.$store.commit("writelist", result.body);
        this.$router.push({path:"/matchlist"});
      })
    },
    logout() {
      this.$http.get("api/logout/").then(result => {
        console.log(result.body);
        if (result.body.error_num === 0) {
          alert("登出成功");
          this.$store.commit("logout");
          this.$router.push({ path: "/home" });
        } else {
          alert("登出失败");
        }
      });
    }
  }
};
</script>

<style scoped>
</style>

