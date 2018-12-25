<template>
  <div>
    <div id="loginbox">
      <el-form :model="form" ref="form" label-width="80px">
        <el-form-item label="用户名">
          <el-input v-model="form.username" placeholder="请输入用户名"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="form.password" placeholder="请输入密码"></el-input>
        </el-form-item>

        <el-form-item>
          <el-button type="primary" @click="login">登录</el-button>
        </el-form-item>
      </el-form>
    </div>
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
        .post("http://127.0.0.1:8000/api/login_competitor/", this.form, {
          emulateJSON: true
        })
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

#loginbox{
  width: 400px;
  height: 300px;
  position: absolute;
  top: 50%;
  left: 50%;
  margin-top: -150px;
  margin-left: -200px;
}
</style>
