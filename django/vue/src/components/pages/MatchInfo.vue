<template>
  <div>
    <el-container>
      <el-main  :data="match" style="width: 100%">
        <div>
          <h2 v-text="match.title"></h2>
          <p>组织方：{{match.organizer}}</p>
          <p>截止时间：{{match.end_time}}</p>
          <p>{{match.description}}</p>
          <el-button type="primary" @click="signup">报名</el-button>
        </div>
      </el-main>
    </el-container>
  </div>
</template>
<script>
export default {
  data() {
    return {
      match: []
    };
  },
  methods: {
    getdata() {
      this.$http
        .get("http://127.0.0.1:8000/api/competition_detail/", {params:{ competition_title: 'test1' }})
        .then(result => {
          console.log(result.body);
          this.match = result.body;
        });
    },
    signup() {
      this.$http.get("api/competitor_sign_up/", {params:{ competition_title: 'test1' }}).then(result => {
        console.log(result.body);
        if (result.body.error_num === 0) {
          alert("报名成功");
        this.$store.commit('signup', 1)
          this.$router.push({path: '/usercenter_competitor'})
        } else {
          alert("报名成功");
        }
      });
    }
  },
  created() {
    this.getdata();
  }
}




</script>



<style scoped>
  .el-main {
    background-color:#E9EEF3;
    color: #333;
    text-align: center;
  }
</style>
