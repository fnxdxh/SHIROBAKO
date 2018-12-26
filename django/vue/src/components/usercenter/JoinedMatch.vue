<template>
    <el-table
      :data="compet_list"
      style="width: 100%">
      <el-table-column
        prop="title"
        label="竞赛名称"
        width="180">
      </el-table-column>
      <el-table-column
        label="上传文件"
        width="400">
        <template slot-scope="scope">
        <input style="width: 260px" type="file" @change="getFile($event,scope.row.name)">上传</input>
        <el-button type="primary"  @click="FileUpload">上传文件</el-button>
      </template>
      </el-table-column>
    </el-table>
  </template>

  <script>
    export default {
      data() {
        return {
          tableData: [{
            name: '小程序竞赛',
            score: '18.5',
          }, {
            name: '大程序竞赛',
            score: '24.0',
          }, {
            name: '中程序竞赛',
            score: '',
          }, {
            name: 'mini程序竞赛',
            score: '90.8',
          }],
          refs: ["http://127.0.0.1:8000/api/upload/"],
          compet_list: []
        }
      },
      methods:{
        FileUpload(){
            this.errText = '';
            //this.$emit('input', this.file);
            //let formData = new FormData();
            //var formData = new FormData();
            var formData = new window.FormData();
            formData.append('userfile', document.querySelector('input[type=file]').files[0]);
            //formData.append("file", this.file);
            console.log(formData.get('userfile'));
            formData.append('competition', this.competition);
            console.log(formData.get('competition'));
            this.$http.post(this.refs[0], formData,{
                headers:{
                    'Content-Type': 'multipart/form-data'
                }
            }).then(function(res){})
            
        },
        getFile(e,name){
          console.log(e);
          this.file = e.target.files[0];
          this.competition = name;
      }
    },
    mounted(){
      this.$http.get('http://127.0.0.1:8000/api/competitor_competition_list/').then(response=>{
        let json_list = response.body.json()
        for(let i = 0;i < json_list.length;i++){
          this.compet_list.append(json_list[i]);
        }
      });;
    }
    }
  </script>

  <style scoped>
  
  </style>