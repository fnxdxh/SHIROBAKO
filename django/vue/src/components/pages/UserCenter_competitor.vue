<template>
  <div>
    <el-container>
      <el-aside width="200px">
        <el-col>
          <el-menu class="el-menu-vertical-demo" :router="true">
            <el-menu-item index="joined">
              <span>我参加的比赛</span>
            </el-menu-item>
            <el-menu-item index="stared">
              <span>我收藏的比赛</span>
            </el-menu-item>
            <el-menu-item index="userinfo">
              <span>我的个人信息</span>
            </el-menu-item>
          </el-menu>
        </el-col>
      </el-aside>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  data(){
    return {
      items:{username: ""}
    }
  }
}
</script>

<style scoped>
</style>
