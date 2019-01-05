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
        <router-link :to="{name: 'judge',params:{competition: scope.row.name}}"><el-button type="primary">进入评审</el-button></router-link>
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
          this.tableData = result.body;
        });
    },
      },
      created() {
    this.getdata();
  }
}
</script>

<style scoped>
</style>
