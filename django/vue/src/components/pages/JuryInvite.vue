<template>
<div>
    <el-input placeholder="请输入评委用户名。" clearable v-model="name">
            <el-button type="primary" slot="append" @click="InviteJury(name)">邀请评委</el-button>
    </el-input>
    <el-table
    :data="tableData"
    style="width: 100%">
        <el-table-column
        prop="judge"
        label="已邀请评委"
        width="180">
        </el-table-column>
    </el-table>
    <p></p>
    <router-link to="/usercenter_organizor/created"><el-button>返回</el-button></router-link>
</div>
</template>

<script>
export default {
    data(){
        return{
            tableData:[
            {judge: '王小明'}],
            name: ''
        }
    },
    methods:{
        InviteJury(jury){
            var formData = new window.FormData();
            let temp_list = this.$route.path.split('/');
            console.log(temp_list);
            let competition = temp_list[temp_list.length - 1];
            formData.append('jury',jury);
            formData.append('competition_name',competition);
            this.$http.post('http://127.0.0.1:8000/api/invite_jury/',formData,{
                headers:{'Content-Type':'multipart/form-data'}
            }).then(response=>{
                var response_list = response.body;
                if (response_list['msg'] == 'no user') {
                    alert('您邀请的用户不存在！');
                }
                else if(response_list['msg'] == 'success'){
                    alert('邀请成功！')
                    this.tableData.push({judge: jury});
                }
            }
            ).catch();
        }
    }
}
</script>

<style scoped>
</style>


