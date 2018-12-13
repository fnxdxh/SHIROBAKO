<template>
  <div>
    <h1>MatchList</h1>
    <div>{{msg}}</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      msg: 'msg'
    }
  },
  methods: {
    getMatchList(){
      this.$http.get('/api/getList').then(result => {
        console.log('ok')
      })
    }
  },
  created() {
    this.getMatchList()
  },
}

</script>

<style scoped>
</style>