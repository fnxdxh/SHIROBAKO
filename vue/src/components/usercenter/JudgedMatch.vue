<template>
  <div>
    <el-table
      :data="tableData"
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
        <router-link to="/creatematch"><el-button type="primary">进入评审</el-button></router-link>
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
          refs: ["http://127.0.0.1:8000/upload"]
        }
      }
}
</script>

<style scoped>
</style>
