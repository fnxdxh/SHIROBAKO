<template>
  <div>
    <h1>HomePage</h1>
    <el-table
      :data="compet_list"
      style="width: 100%">
      <el-table-column
        prop="title"
        label="竞赛名称"
        width="180">
      </el-table-column>
      <el-table-column
        prop="sponsor"
        label="主办方"
        width="280">
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default{
  data(){
    return{
      msg:{key: '初始msg'}
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
