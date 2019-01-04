<template>
    <div>
        <!-- <table>
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
        </table> -->
        
        <el-table :data="tableData4" style="width: 100%" max-height="250">
    <el-table-column fixed prop="date" label="日期" width="150">
    </el-table-column>
    <el-table-column prop="name" label="姓名" width="120">
    </el-table-column>
    <el-table-column prop="province" label="省份" width="120">
    </el-table-column>
    <el-table-column prop="city" label="市区" width="120">
    </el-table-column>
    <el-table-column prop="address" label="地址" width="300">
    </el-table-column>
    <el-table-column prop="zip" label="邮编" width="120">
    </el-table-column>
    <el-table-column label="操作" width="120">
      <template slot-scope="scope">
        <el-button @click.native.prevent="deleteRow(scope.$index, tableData4)" type="text" size="small">
          移除
        </el-button>
      </template>
    </el-table-column>
  </el-table>
        
    </div>
</template>

<script>
export default {
    // data(){
    //     return {
    //         tabledata: []
    //     }
    // },
    // methods: {
    //     gettabledata(){
    //         this.$http.get('api/wait_list/').then(result => {
    //             console.log(result.body)
    //             this.tabledata = result.body
    //         })
    //     },
    //     accept(username){
    //         console.log(username)
    //         this.$http.post('api/recognize/', {'username': username}).then(result => {
    //             console.log(result.body)
    //             this.gettabledata()
    //         })
    //     }
    // },
    // created(){
    //     this.gettabledata()
    // }
    methods: {
      deleteRow(index, rows) {
        rows.splice(index, 1);
      }
    },
    data() {
      return {
        tableData4: [{
          date: '2016-05-03',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          zip: 200333
        }, {
          date: '2016-05-02',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          zip: 200333
        }, {
          date: '2016-05-04',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          zip: 200333
        }, {
          date: '2016-05-01',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          zip: 200333
        }, {
          date: '2016-05-08',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          zip: 200333
        }, {
          date: '2016-05-06',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          zip: 200333
        }, {
          date: '2016-05-07',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          zip: 200333
        }]
      }
    }
}
</script>

<style scoped>

</style>
