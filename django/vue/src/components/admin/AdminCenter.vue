<template>
    <div>
        <h1>{{tabledata}}</h1>
        <el-table :data="tabledata">
            <el-table-column prop="name" label="待审核主办方">
            </el-table-column>
            <el-table-column label="操作">
                <el-button type="text" @click="accept(username)">通过</el-button>               
            </el-table-column>
            
        </el-table> -->
        <table>
            <thead>
                <tr>
                    <th>待审核主办方</th>
                    <th>审核通过</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in tabledata" :key="item.username">
                    <td>{{item.username}}</td>
                    <td><a href="" @click.prevent="accept(item.username)">审核通过</a></td>
                </tr>
            </tbody>
        </table>
        
    </div>
</template>

<script>
export default {
    data(){
        return {
            tabledata: []
        }
    },
    methods: {
        gettabledata(){
            this.$http.get('api/wait_list/').then(result => {
                console.log(result.body)
                this.tabledata = result.body
            })
        },
        accept(username){
            console.log(username)
            this.$http.post('api/recognize/', {'username': username}).then(result => {
                console.log(result.body)
                this.gettabledata()
            })
        }
    },
    created(){
        this.gettabledata()
    }
}
</script>

<style scoped>

</style>
