<template>
  <div id="sidebar">
    <el-col :span="6">
      <el-menu
        default-active="2"
        class="el-menu-vertical-demo"
      >
        <el-menu-item index="1">
          <span>我参加的比赛</span>
        </el-menu-item>
        <el-menu-item index="2">
          <span>我创建的比赛</span>
        </el-menu-item>
        <el-menu-item index="3">
          <span>我评审的比赛</span>
        </el-menu-item>
        <el-menu-item index="4">
          <span>我收藏的比赛</span>
        </el-menu-item>
        <el-menu-item index="5">
          <span>我的个人信息</span>
        </el-menu-item>
      </el-menu>
    </el-col>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
};
</script>

<style>
</style>
