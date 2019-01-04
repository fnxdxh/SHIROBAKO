<template>
  <div>
    <router-link to="/creatematch">
      <el-button type="primary">创建比赛</el-button>
    </router-link>
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
      <el-table-column label="查看详情" width="150">
        <template slot-scope="scope">
          <router-link to="/matchinfo">
            <el-button type="primary">详情</el-button>
          </router-link>
        </template>
      </el-table-column>
      <el-table-column label="邀请评委" width="150">
        <template slot-scope="scope">
        <router-link :to="{name: 'invite',params:{competition: scope.row.title}}"><el-button type="primary">进入邀请</el-button></router-link>
        </template>
      </el-table-column>
      <el-table-column label="分配作品">
        <template slot-scope="scope">
        <el-input placeholder="请输入每个评委评审作品数。" type="number" clearable v-model="scope.row.number">
            <el-button type="primary" slot="append" @click="Divide(scope.row.number,scope.row.title)">分配</el-button>
        </el-input>
        </template>
      </el-table-column>
    </el-table>
  </div>
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
      tableData: [
        {title:'小程序竞赛',
         sponsor:'青蛙大学',
         number:18
        }
      ]
    };
  },
  methods: {
    getdata() {
      this.$http
        .get("api/organizer_competition_list/")
        .then(result => {
          console.log(result.body);
          this.tableData = result.body;
        });
    },
    Divide(number,title){
      var formdata = new FormData();
      formdata.append('competition_name',title);
      formdata.append('time',number);
      this.$http.post('api/divide_paper/',formdata,{
                headers:{'Content-Type':'multipart/form-data'}
            }).then(response=>{
              alert('分配成功！');
            }).catch()
    }
  },

  created() {
    this.getdata();
  }
};
</script>