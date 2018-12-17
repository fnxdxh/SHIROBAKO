<template>
  <div>
    <el-table :data="this.$store.state.matches">
      <el-table-column prop="name" label="赛事名称" width="180"></el-table-column>
      <el-table-column prop="sponsor" label="主办方" width="180"></el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  methods: {}
};
</script>

<style scoped>
</style>