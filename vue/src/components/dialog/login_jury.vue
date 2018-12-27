<template>
  <div>
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
</template>

<script>
export default {
  data() {
    return {
      form: {
        username: "",
        password: ""
      }
    };
  },
  methods: {
    login() {
      this.$http.post("api/login_jury/", this.form).then(result => {
        console.log(result.body);
        if (result.body.error_num === 0) {
          alert("登陆成功");
          this.$store.commit('login', 3)
          this.$router.push({path: '/usercenter_jury'})
        } else {
          alert("登录失败");
        }
      });
    }
  }
};
</script>

<style scoped>
</style>
