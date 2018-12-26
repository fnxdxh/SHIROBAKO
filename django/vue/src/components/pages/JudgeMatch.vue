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
        prop="score"
        label="评分结果"
        width="110">
        </el-table-column>
        <el-table-column
        label="评分"
        width="400">
        <template slot-scope="scope">
        <el-input placeholder="请输入分数，分数介于0~100分内。" clearable type="number" v-model="score">
            <el-button type="primary" slot="append" @click="UpdateScore(scope.row.name,scope.row.score)">提交分数</el-button>
        </el-input>
        </template>
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
            tableData: [{
            name: 'helloworld.zip',
            score: '15.7'
            }, {
            name: 'fucktheworld.txt',
            score: ''
            }, {
            name: 'nicetomeetyou.rar',
            score: '18.6'
            }, {
            name: 'mi.txt',
            score: '100'
            }],
        }
    },
    methods:{
        FileDownload(filename){
            var formData = new window.FormData();
            formData.append('filename', filename);
            this.$http.post('http://127.0.0.1:8000/api/file_download/',formData,
            {headers:{'Content-Type':'multipart/form-data'}}).then(response => {
            console.log(response.data);
            // get body data
            this.file = response.body;
            }, response => {
                console.log("error");
            });
            
            const blob = new Blob([this.file]);
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
        },
        UpdateScore(filename,score,path){
            let temp_list = this.$router.path.split('/');
            let competition = temp_list[temp_list.length - 1];
            let score_list = {grade: score, filename: filename,title: competition};
            this.$http.post('http://127.0.0.1:8000/api/upload_grade/',score_list);
        }
    }
}
</script>

<style scoped>
</style>

