<template>
  <el-table
    :data="tableData5"
    style="width: 100%">
    <el-table-column type="expand">
      <template slot-scope="props">
        <el-form label-position="left" inline class="demo-table-expand">
          <el-form-item label="比赛名称">
            <span>{{ props.row.name }}</span>
          </el-form-item>
          <el-form-item label="比赛 ID">
            <span>{{ props.row.id }}</span>
          </el-form-item>          
          <el-form-item label="开始时间">
            <span>{{ props.row.starttime }}</span>
          </el-form-item>
          <el-form-item label="结束时间">
            <span>{{ props.row.ddltime }}</span>
          </el-form-item>
          <el-form-item label="组织单位">
            <span>{{ props.row.host }}</span>
          </el-form-item>
          <el-form-item label="比赛状态">
            <span>{{ props.row.status }}</span>
          </el-form-item>
          <el-form-item label="比赛描述">
            <span>{{ props.row.desc }}</span>
          </el-form-item>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column
      label="比赛 ID"
      prop="id">
    </el-table-column>
    <el-table-column
      label="比赛名称"
      prop="name">
    </el-table-column>
    <el-table-column
      label="比赛状态"
      prop="status">
    </el-table-column>
    <el-table-column
      label="查看详情"
      width="200">
      <template slot-scope="scope">
      <router-link to="/matchinfo"><el-button type="primary">详情</el-button></router-link>
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
        tableData5: [{
          id: '12987122',
          name: '大数据竞赛',
          host: '黑箱公司',
          desc: '为在校大学生举办的大数据竞赛，奖金丰厚请来参加',
          status: '进行中',
          starttime: '2018-12-18',
          ddltime: '2018-12-31'
        }, {
          id: '12987123',
          name: '大数据竞赛',
          host: '黑箱公司',
          desc: '为在校大学生举办的大数据竞赛，奖金丰厚请来参加',
          status: '进行中',
          starttime: '2018-12-18',
          ddltime: '2018-12-31'
        }, {
          id: '12987125',
          name: '大数据竞赛',
          host: '黑箱公司',
          desc: '为在校大学生举办的大数据竞赛，奖金丰厚请来参加',
          status: '进行中',
          starttime: '2018-12-18',
          ddltime: '2018-12-31'
        }, {
          id: '12987126',
          name: '大数据竞赛',
          host: '黑箱公司',
          desc: '为在校大学生举办的大数据竞赛，奖金丰厚请来参加',
          status: '进行中',
          starttime: '2018-12-18',
          ddltime: '2018-12-31'
        }]
      }
    }
  }
</script>