<template>
  <div>
    <h1>比赛详情</h1>
    <p>{{$route.params.class}}</p>
    <p>{{$route.params.matchname}}</p>
    <div>
      <h2 v-text="match.name"></h2>
      <p>组织方：{{match.host}}</p>
      <p>状态：{{match.status}}</p>
      <img :src="match.image">
      <p>{{match.intro}}</p>
    </div>
  </div>
</template>
<script>
export default {
  data () {
    return {
      match: {
        name: '大数据竞赛',
        host: '黑箱公司',
        status: '进行中',
        intro: '随着云时代的来临，大数据（Big data）也吸引了越来越多的关注。分析师团队认为，大数据（Big data）通常用来形容一个公司创造的大量非结构化数据和半结构化数据，这些数据在下载到关系型数据库用于分析时会花费过多时间和金钱。大数据分析常和云计算联系到一起，因为实时的大型数据集分析需要像MapReduce一样的框架来向数十、数百或甚至数千的电脑分配工作'
      }
    }
  }
}




</script>
