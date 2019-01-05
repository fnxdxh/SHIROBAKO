<template>
  <el-table :data="tableData" style="width: 100%">
    <el-table-column type="expand">
      <template slot-scope="props">
        <el-form label-position="left" inline class="demo-table-expand">
          <el-form-item label="比赛名称">
            <span>{{ props.row.title }}</span>
          </el-form-item>
          <el-form-item label="开始时间">
            <span>{{ props.row.start_time }}</span>
          </el-form-item>
          <el-form-item label="结束时间">
            <span>{{ props.row.end_time }}</span>
          </el-form-item>
          <el-form-item label="组织单位">
            <span>{{ props.row.sponsor }}</span>
          </el-form-item>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column label="比赛名称" prop="title"></el-table-column>
    <el-table-column label="组织单位" prop="sponsor"></el-table-column>
    <el-table-column label="查看详情" width="200">
      <template slot-scope="scope">
        <router-link to="/matchinfo">
          <el-button type="primary">详情</el-button>
        </router-link>
      </template>
    </el-table-column>
  </el-table>
</template>

<style>
.demo-table-expand {
  font-size: 0;
}
.demo-table-expand label {
  width: 90px;
  color: #99a9bf;
}
.demo-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 50%;
}
</style>

<script>
export default {
  data() {
    return {
      tableData: []
    };
  },
  methods: {
    getdata() {
      this.tableData = this.$store.state.list;
    }
  },

  created() {
    this.getdata();
  }
};
</script>