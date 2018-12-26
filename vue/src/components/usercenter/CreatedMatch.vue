<template>
  <div>
    <router-link to="/creatematch"><el-button type="primary">创建比赛</el-button></router-link>
    <el-table
      :data="compet_list"
      style="width: 100%">
      <el-table-column
        prop="title"
        label="竞赛名称"
        width="180">
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default{
  data(){
    return{
      tableData:[],
      compet_list:[]
    }
  },
  mounted(){
      this.$http.get('http://127.0.0.1:8000/api/organizer_competition_list/').then(response=>{
        let json_list = response.body.json()
        for(let i = 0;i < json_list.length;i++){
          this.compet_list.append(json_list[i]);
        }
      });;
    }
}
</script>

<style scoped>
</style>
