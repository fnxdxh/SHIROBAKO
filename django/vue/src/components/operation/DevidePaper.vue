<template>
    <div>
        <el-form :inline="true" :model="form" ref="form" label-width="80px">
            <el-form-item label="次数">
                <el-input v-model="form.times" placeholder="每张试卷批改次数"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="onSubmit">提交</el-button>
            </el-form-item>
        </el-form>
        
    </div>
</template>

<script>
export default {
    data(){
        return {
            form: {
                times: 0
            }
        }
    },
    methods: {
        onSubmit(){
            this.$http.post('api/divide_paper/', {title: 'mytitle', time: this.form.times})
        }
    }
}
</script>

<style scoped>

</style>
