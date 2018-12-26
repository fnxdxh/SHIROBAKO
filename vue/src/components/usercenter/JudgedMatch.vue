<template>
  <div>
    <el-table
      :data="compet_list"
      style="width: 100%">
      <el-table-column
        prop="name"
        label="竞赛名称"
        width="180">
      </el-table-column>
      <el-table-column
        label="进入评审"
        width="200">
        <template slot-scope="scope">
        <router-link :to="{name: 'judge',params:{competition: scope.row.name}}"><el-button type="primary">进入评审</el-button></router-link>
      </template>
      </el-table-column>
      <el-table-column
        prop="date"
        label="截止日期">
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
      data() {
        return {
          tableData: [{
            name: '小程序竞赛',
            date: '2018.12.15'
          }, {
            name: '大程序竞赛',
            date: '2019.1.1'
          }, {
            name: '中程序竞赛',
            date: ''
          }, {
            name: 'mini程序竞赛',
            date: '2018.11.14'
          }],
          refs: ["http://127.0.0.1:8000/upload"],
          compet_list: []
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
