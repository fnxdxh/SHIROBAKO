<template>
  <div id="OrgainzerPage">
      <el-container>
        <el-header style="font-size: 12px">
          <img src="./assets/logo.jpg" style="float:left"><img>
        </el-header>
        </el-container>
          <el-container>
          <el-aside width="200px">
            <el-row class="tac">
              <el-col :span="12">
                <el-menu default-active="1" class="el-menu-vertical-demo">
                  <el-menu-item index="1">
                    <span slot="title">竞赛状态</span>
                  </el-menu-item>
                  <el-menu-item index="2">
                    <span slot="title">个人信息</span>
                  </el-menu-item>
                  <el-menu-item index="3">
                    <span slot="title">修改信息</span>
                  </el-menu-item>
                  <el-menu-item index="4">
                    <span slot="title">新建赛事</span>
                  </el-menu-item>
                </el-menu>
              </el-col>
            </el-row>
          </el-aside>

          <el-main>
            <el-table :data="tableData" border style="width: 100%; margin-top:100px">
              <el-table-column prop="name" label="名称" width="180">
              </el-table-column>
              <el-table-column prop="organizer" label="主办方" width="180">
              </el-table-column>
              <el-table-column prop="detail" label="详情">
              </el-table-column>
            </el-table>
          </el-main>
      </el-container>
  </div>
</template>

<script>
  export default {

}
</script>

<style>
#app {
  font-family: Helvetica, sans-serif;
  text-align: center;
}
</style>
