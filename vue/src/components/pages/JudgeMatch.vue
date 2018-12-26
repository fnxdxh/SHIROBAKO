<template>
<div>
    <el-table
    :data="tableData"
    style="width: 100%">
        <el-table-column
        prop="index"
        label="作品序号"
        width="180">
        </el-table-column>
        <el-table-column
        label="下载文件"
        width="180">
        <template slot-scope="scope">
            <el-button type="primary"  @click="FileDownload">下载文件</el-button>
        </template>
        </el-table-column>
        <el-table-column
        prop="score"
        label="评分结果"
        width="110">
        </el-table-column>
        <el-table-column
        label="评分"
        width="400"
        type="number">
        <template slot-scope="scope">
        <el-input placeholder="请输入分数，分数介于0~100分内。" clearable type="number" v-model="score">
            <el-button type="primary" slot="append">提交分数</el-button>
        </el-input>
        </template>
        </el-table-column>
    </el-table>
    <p></p>
    <router-link to="/usercenter/judged"><el-button>返回</el-button></router-link>
</div>
</template>

<script>
export default {
    data(){
        return{
            tableData: [{
            index: '1',
            score: '15.7'
            }, {
            index: '2',
            score: ''
            }, {
            index: '3',
            score: '18.6'
            }, {
            index: '4',
            score: '100'
            }],
        }
    },
    methods:{
        FileDownload(){
            this.$http.get('http://localhost:8000/api/file_upload/').then(response => {
            console.log(response.data);
            // get body data
            this.file = response.body;
            }, response => {
                console.log("error");
            });
            let filename = this.file.name;
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
        UpdateScore(){
            this.$http.post('http://127.0.0.1:8000/api/upload_grade/',)
        }
    }
}
</script>

<style scoped>
</style>

