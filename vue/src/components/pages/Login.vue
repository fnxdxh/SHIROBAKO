<template>
  <div>
    <el-menu mode="horizontal" :router="true">
      <el-menu-item index="competitor">我是参赛者</el-menu-item>
      <el-menu-item index="organizer">我是主办方</el-menu-item>
      <el-menu-item index="jury">我是评委</el-menu-item> 
    </el-menu>
    <router-view></router-view>

    </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        username: "",
        password: ""
      },
      isLogin: 0
    };
  },
  methods: {
    login() {
      this.$http
        .post("api/login_competitor/", this.form)
        .then(result => {
          console.log(result.body);
          if (result.body.error_num === 0) {
            alert("登陆成功");
            this.$router.replace('/usercenter');
          } else {
            alert("登录失败");
            this.$router.replace('/login');
          }
        });
    }
  }
};
</script>

<style scoped>

/* #loginbox{
  width: 400px;
  height: 300px;
  position: absolute;
  top: 50%;
  left: 50%;
  margin-top: -150px;
  margin-left: -200px;
} */
</style>
