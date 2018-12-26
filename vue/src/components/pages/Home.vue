<template>
  <div>
    <h1>HomePage</h1>
    <h1>{{$store.state.count}}</h1>
    <h1>{{msg}}</h1>
  </div>
</template>

<script>
export default{
  data(){
    return{
      msg:{key: '初始msg'}
    }
  },
  created: {

  }
}
</script>

<style scoped>
</style>
