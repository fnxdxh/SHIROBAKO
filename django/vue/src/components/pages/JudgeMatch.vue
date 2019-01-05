<template>
<div>
    <el-table
    :data="tableData"
    style="width: 100%">
        <el-table-column
        prop="name"
        label="作品名"
        width="180">
        </el-table-column>
        <el-table-column
        label="下载文件"
        width="180">
        <template slot-scope="scope">
            <el-button type="primary"  @click="FileDownload(scope.row.name)">下载文件</el-button>
        </template>
        </el-table-column>
        <el-table-column
        label="打分"
        width="400">
        <template slot-scope="scope">
        <el-input placeholder="请输入分数，分数介于0~100分内。" clearable type="number" v-model="scope.row.score">
            <el-button type="primary" slot="append" @click="UpdateScore(scope.row.name,scope.row.score)">提交分数</el-button>
        </el-input>
        </template>
        </el-table-column>
        <el-table-column
         prop="grade"
         label="评分结果"
         width="180">
        </el-table-column>
    </el-table>
    <p></p>
    <router-link to="/usercenter_jury/judged"><el-button>返回</el-button></router-link>
</div>
</template>

<script>
export default {
    data(){
        return{
            tableData: [],
            file_list: [],
            items: {username: ""}
        }
    },
    methods:{
        getdata() {
      this.$http
        .get("api/file_list/")
        .then(result => {
          console.log(result.body);
          this.tableData = result.body;
        });
    },
        FileDownload(filename){
            var formdata = new window.FormData();
            formdata.append('filename',filename)
            this.$http.post('http://localhost:8000/api/file_download/',formdata,{headers:{
                    'Content-Type': 'multipart/form-data'
                }}).then(response => {
            console.log(response.data);
            // get body data;
            const blob = new Blob([response.body]);
            if (window.navigator.msSaveOrOpenBlob) {
            // 兼容IE10
                navigator.msSaveBlob(blob, filename);
            } 
            else {
            //  chrome/firefox
            let aTag = document.createElement('a');
            aTag.download = filename;
            aTag.href = URL.createObjectURL(blob);
            aTag.click();
            URL.revokeObjectURL(aTag.href);
            }
            }, response => {
                console.log("error");
            });
           
        },
        UpdateScore(filename,score){
            let temp_list = this.$route.path.split('/');
            console.log(temp_list);
            let competition = temp_list[temp_list.length - 1];
            console.log(competition);
            let score_list = {grade: score, filename: filename,title: competition};
            console.log(score_list);
            var formData = new window.FormData;
            formData.append('grade',score);
            formData.append('filepath',filename);
            formData.append('title',competition);
            this.$http.post('http://127.0.0.1:8000/api/upload_grade/',formData,{
                headers:{
                    'Content-Type': 'multipart/form-data'
                }
            }).then(result => {
                alert('打分成功！');
            });
        },
         getdata() {
             let temp_list = this.$route.path.split('/');
            console.log(temp_list);
            let competition = temp_list[temp_list.length - 1];
            console.log(competition);
      this.$http
        .get("api/file_list/",{params:{competition_name:competition}})
        .then(result => {
          console.log(result.body);
          this.tableData = result.body;
        });
    }
},
created() {
    this.getdata();
  }
}
</script>

<style scoped>
</style>

