<template>
    <div>
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
