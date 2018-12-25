<template>
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
    width="400">
    <template slot-scope="scope">
        <el-button type="primary"  @click="FileDownload">下载文件</el-button>
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
            this.$http.get('http://localhost:8000').then(response => {
            console.log(response.data);
            // get body data
            this.content = response.body;
            }, response => {
                console.log("error");
            });
            
        }
    },
    mounted:function(){
        
    }
}
</script>

<style scoped>
</style>

