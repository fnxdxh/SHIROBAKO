<template>
  <div>
    <el-table
      :data="tableData"
      style="width: 100%">
      <el-table-column
        prop="title"
        label="竞赛名称"
        width="180">
      </el-table-column>
      <el-table-column
        label="进入评审"
        width="200">
        <template slot-scope="scope">
        <router-link :to="{name: 'judge',params:{competition: scope.row.title}}"><el-button type="primary">进入评审</el-button></router-link>
      </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
      data() {
        return {
          tableData: [],
          refs: ["http://127.0.0.1:8000/upload"],
          compet_list: [],
          items:{username:""}
        }
      },
      methods:{
        getdata() {
      this.$http
        .get("api/jury_competition_list/")
        .then(result => {
          console.log(result.body);
          let response_list = result.body;
          if(response_list[0]['msg'] == 'no competition'){
            alert('没有此比赛！');
          }
          else if(response_list[0]['msg'] == 'not log in'){
            alert('用户未登录！');
            this.$router.push({path: '/login'});
          }
          else if(response_list[0]['msg'] == 'success'){
            this.tableData = response_list;
          }
        });
    },
      },
      created(){
        this.getdata();
      }
}
</script>

<style scoped>
</style>
