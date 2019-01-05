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
        <input style="width: 260px" type="file" @change="getFile($event,scope.row.name)"></input>
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
            score: '',
          }, {
            name: '大程序竞赛',
            score: '',
          }, {
            name: '中程序竞赛',
            score: '',
          }, {
            name: 'mini程序竞赛',
            score: '',
          }],
          refs: ["http://127.0.0.1:8000/api/upload/"],
          compet_list: [],
          items:{username:""},
          file_list:[
            {name:''}
          ]
        }
      },
      methods:{
        FileUpload(){
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
            }).then(resule => {
              alert('上传成功！');
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
    mounted(){
      this.$http.get('http://127.0.0.1:8000/api/competitor_competition_list/').then(response=>{
        this.compet_list = response.body;
      });
      this.items.username=sessionStorage.getItem("username");
    }
    }
  </script>

  <style scoped>
  
  </style>