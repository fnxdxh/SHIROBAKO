<template>
    <div>
        <h1>{{msg}}</h1>
    </div>
</template>

<script>
export default {
    data(){
        return {
            msg: {}
        }
    },
    methods: {
        getmsg(){
            this.$http.get('api/wait_list/').then(result => {
                console.log(result.body)
                this.msg = result.body
            })
        }
    },
    created(){
        this.getmsg()
    }
}
</script>

<style scoped>

</style>
