<template>
    <el-table
      :data="tableData"
      style="width: 100%">
      <el-table-column
        prop="name"
        label="竞赛名称"
        width="180">
      </el-table-column>
      <el-table-column
        label="上传文件"
        width="400">
        <template slot-scope="scope">
        <el-input style="width: 260px" type="file" @change="getFile($event, scope.row.name)" @click="FileUpload">上传</el-input>
      </template>
      </el-table-column>
      <el-table-column
        prop="score"
        label="评分结果">
      </el-table-column>
    </el-table>
  </template>

  <script>
    export default {
      data() {
        return {
          tableData: [{
            name: '小程序竞赛',
            score: '18.5'
          }, {
            name: '大程序竞赛',
            score: '24.0'
          }, {
            name: '中程序竞赛',
            score: ''
          }, {
            name: 'mini程序竞赛',
            score: '90.8'
          }],
          refs: ["http://127.0.0.1:8000/api/upload"]
        }
      },
      methods:{
        FileUpload(name){
            this.file = this.upath;
            this.errText = '';
            this.$emit('input', this.file);
            let formData = new FormData();
            formData.append("attachment", this.file);
            formData.append("competition", this.competition);
            this.$http.post(this.refs[0], formData,{
                headers:{
                    'Content-Type': 'multipart/form-data'
                }
            }).then(function(res){})
        },
        getFile(event, name) {
        this.upath = event.files;
        this.competition = name;
      }
      }
      
    }
  </script>

  <style scoped>
  
  </style>