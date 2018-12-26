<template>
    <div>
        <el-table :data="tabledata">
            <el-table-column prop="username" label="待审核主办方">
            </el-table-column>
        </el-table>
        
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
        }
    },
    created(){
        this.gettabledata()
    }
}
</script>

<style scoped>

</style>
