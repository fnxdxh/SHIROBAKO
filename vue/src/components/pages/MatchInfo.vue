<template>
  <div>
    <h1>matchinfo.vue</h1>
    <p>{{$route.params.class}}</p>
    <p>{{$route.params.matchname}}</p>
    <div>
      <h2 v-text="match.matchname"></h2>
      <p>组织方：{{match.matchhost}}元</p>
      <p>状态：{{match.matchstatus}}</p>
      <img :src="match.matchimage">
      <p>{{match.matchintro}}</p>
    </div>
  </div>
</template>
<script>
import {Getmatch} from '../../../api/api'
export default {
  data () {
    return {
      match: {}
    }
  },
  mounted () {
    let params = {
      matchname: this.$route.params.matchname,
      matchclass: this.$route.params.class
    }
    Getmatch(params).then(res => {
      console.log(res)
      this.match = res.data.curmatch
    })
  }
}
</script>
