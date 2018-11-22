<template>
  <div id="Home">
    <el-container>
        <el-header style="font-size: 12px">
          <img src="./assets/images/logo.jpg" style="float:left; margin-left: 15px"><img>
          <el-button type="primary" style="float:right; margin-right: 15px" plain>登录</el-button>
          <el-button type="primary" style="float:right; margin-right: 15px" plain>注册</el-button>
        </el-header>
        <el-main>

          <el-carousel :interval="4000" type="card" height="200px">
            <el-carousel-item v-for="item in 3" :key="item">
              <h3><a href="">{{ item }}</a></h3>
            </el-carousel-item>
          </el-carousel>

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
    data() {
      return {
        tableData: [{
          name: '竞赛1',
          organizer: '白箱官方平台',
          detail: '大数据竞赛'
        }, 
        {
          name: '竞赛2',
          organizer: '白箱官方平台',
          detail: '小程序竞赛'
        }]
      }
    }
}
</script>

<style>
a {
  text-decoration:none
}
#app {
  font-family: Helvetica, sans-serif;
  text-align: center;
}
.el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }
  
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  
  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>
