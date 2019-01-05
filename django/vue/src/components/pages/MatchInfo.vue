<template>
  <div>
    <el-container>
      <el-main  :data="match" style="width: 100%">
        <div>
          <h2 v-text="match.title"></h2>
          <p>组织方：{{match.organizer}}</p>
          <p>报名开始时间：{{match.sign_up_start}}</p>
          <p>报名截止时间：{{match.sign_up_end}}</p>
          <p>比赛开始时间：{{match.start_time}}</p>
          <p>比赛截止时间：{{match.end_time}}</p>
          <p>{{match.description}}</p>
          <el-button type="primary" @click="signup">报名</el-button>
          <router-link to="/home"><el-button type="primary">返回</el-button></router-link>
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
      let temp_list = this.$route.path.split('/');
      console.log(temp_list);
      let competition = temp_list[temp_list.length - 1];
      competition = decodeURIComponent(competition);
      console.log(competition);
      this.$http
        .post("http://127.0.0.1:8000/api/competition_detail/", { 'competition_title': competition })
        .then(result => {
          console.log(result.body);
          this.match = result.body;
        });
    },
    signup() {
      let temp_list = this.$route.path.split('/');
      console.log(temp_list);
      let competition = temp_list[temp_list.length - 1];
      competition = decodeURIComponent(competition);
      console.log(competition);
      this.$http.post("http://127.0.0.1:8000/api/sign_up/", { 'competition_title': competition }).then(result => {
        console.log(result.body);
        let response_list = result.body;
        if (response_list['msg'] == 'out of time') {
          alert("不在报名时间内！");
        } 
        else if(response_list['msg'] == 'signed up'){
          alert("您已报过名！");
          this.$router.push({path: '/usercenter_competitor'});
        }
        else if(response_list['msg'] == 'not login'){
          alert("用户未登录！");
          this.$router.push({path: '/login'});
        }
        else if(response_list['msg'] == 'failed'){
          alert("报名失败！");
        }
        else{
          alert("报名成功！");
          this.$router.push({path: '/usercenter_competitor'});
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
