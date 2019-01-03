<template>
  <div>
    <router-link to="/creatematch"><el-button type="primary">创建比赛</el-button></router-link>
    <el-table
      :data="tableData"
      style="width: 100%">
      <el-table-column
        prop="title"
        label="竞赛名称"
        width="180">
      </el-table-column>
      <el-table-column>
        <template slot-scope="scope">
        <router-link :to="{name: 'invite',params:{competition: scope.row.title}}"><el-button type="primary">进入邀请</el-button></router-link>
        </template>
      </el-table-column>
      <el-table-column>
        <template slot-scope="scope">
        <el-input placeholder="请输入每个评委评审作品数。" type="number" clearable v-model="scope.row.number">
            <el-button type="primary" slot="append" @click="Divide(scope.row.number)">邀请评委</el-button>
        </el-input>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default{
  data(){
    return{
      tableData:[
        {title:'小程序竞赛',number:0},
        {title:'大程序竞赛',number:0},
        {title:'中程序竞赛',number:0}
      ],
      compet_list:[],
      items:{username:""}
    }
  },
  mounted(){
      this.$http.get('api/organizer_competition_list/').then(response=>{
        this.compet_list = response.body;
      });
      this.items.username=sessionStorage.getItem("username");
    },
  methods:{
    Divi
  }
}
</script>

<style scoped>
</style>
