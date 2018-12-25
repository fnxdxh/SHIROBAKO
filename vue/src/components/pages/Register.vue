<template>
  <div>
    <el-menu mode="horizontal" :router="true">
      <el-menu-item index="competitor">我是参赛者</el-menu-item>
      <el-menu-item index="organizer">我是主办方</el-menu-item>
      <el-menu-item index="jury">我是评委</el-menu-item> 
    </el-menu>

    <router-view></router-view>
  </div>
</template>

<script>
export default {

};
</script>

<style scoped>
</style>
