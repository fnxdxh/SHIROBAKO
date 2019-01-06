<template>
    <div>
        <el-table>
            <el-table-column label="排名" type="index"></el-table-column>
            <el-table-column label="用户名" prop="username"></el-table-column>
            <el-table-column label="分数" prop="grade"></el-table-column>
        </el-table>
    </div>
</template>

<script>
export default {
    data(){
        return{
            tableData:[]
        }
    },
    methods:{
        getdata() {
            let temp_list = this.$route.path.split('/');
            console.log(temp_list);
            let competition = temp_list[temp_list.length - 1];
            console.log(competition);
            competition = decodeURIComponent(competition);
            console.log(competition);
            this.$http
            .post("api/grade_list/",{'competition_name':competition})
            .then(result => {
                console.log(result.body);
                let table = result.body;
                if(table[0]['msg'] == 'out of time'){
                    alert("排行榜尚未公布！");
                }
                else if(table[0]['msg'] == 'success'){
                    this.tableData = result.body;
                }
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


