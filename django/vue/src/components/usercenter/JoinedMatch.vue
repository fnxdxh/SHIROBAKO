<template>
    <el-table
      :data="tableData"
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
        <input style="width: 260px" type="file" @change="getFile($event,scope.row.title)"></input>
        <el-button type="primary"  @click="FileUpload">上传文件</el-button>
      </template>
      </el-table-column>
    </el-table>
  </template>

  <script>
    export default {
      data() {
        return {
          tableData: [],
          refs: ["http://127.0.0.1:8000/api/upload/"],
          compet_list: [],
          items:{username:""},
        }
      },
      methods:{
         getdata() {
      this.$http
        .get("api/competitor_competition_list/")
        .then(result => {
          console.log(result.body);
          this.tableData = result.body;
        });
    },
        FileUpload(){.93206

            this.errText = '';
            //this.$emit('input', this.file);
            //let formData = new FormData();
            //var formData = new FormData();
            var formData = new window.FormData();
            var file_upload = document.querySelector('input[type=file]').files[0];
            console.log(file_upload);
            formData.append('userfile',this.file);
            //formData.append("file", this.file);
            console.log(formData.get('userfile'));
            formData.append('competition', this.competition);
            console.log(formData.get('competition'));
            this.$http.post(this.refs[0], formData,{
                headers:{
                    'Content-Type': 'multipart/form-data'
                }
            }).then(result => {
              let response_list = result.body;
              if(response_list['msg'] == 'not login'){
                alert("用户未登录！");
                this.$router.push({path: '/login'});
              }
              else if (response_list['msg'] == 'out of time') {
                alert("不在上传时间内！");
              }
              else{
                alert("上传成功！");
              }
            })
            
        },
        getFile(e,name){
          console.log(e);
          var file = e.target.files[0];
          this.file = file;
          console.log(this.file);
          this.competition = name;
      }
    },
    created() {
    this.getdata();
  }
    }
  </script>

  <style scoped>
  
  </style>