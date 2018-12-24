<template>

    <div id="tasks" class="card">

      <Card shadow class="tasks" padding=0>

        <div id="taskListTitle"><h2>我的比赛</h2></div>

        <div>

          <ul>

            <li v-for="task in pageList">

              <Card padding=10 @click.native="checkTaskDetail(task.id)">

                <p slot="title" id="taskTitle">

                  {{ task.title }}&nbsp;&nbsp;&nbsp;<span v-for="tag in task.tags"><Tag><h4>{{ tag }}</h4></Tag></span>

                </p>

                <p id="taskStatus">比赛状态：{{ task.status }}</p>

                <p id="taskTime">起始时间：{{ task.publishTime }}&nbsp;&nbsp;&nbsp;截止时间：{{ task.ddlTime }}</p>

                <p id="taskDescription">{{ task.description }}</p>

              </Card>

            </li>

          </ul>

        </div>

      </Card>

      <div id="pages">

        <Page :total="page_total_num" page-size="5" show-elevator @on-change="setPageList"></Page>

      </div>

    </div>

  </div>

</template>



<script>

  /* eslint-disable no-new */

  export default {

    name: 'tasks',

    data () {

      return {

        tasklist: [],

        page_total_num: 0,

        pageList: []

      }

    },

    mounted: function () {

      const headers = new Headers({

        'Content-Type': 'application/json'

      })

      let that = this

      fetch('api/GetEmployerTasks', { method: 'GET',

        headers,

        credentials: 'include'})

      .then(function (response) {

        return response.json().then(function (data) {

          that.tasklist = []

          for (let task of data.taskList) {

            switch (task.status) {

              case 0:

                task.status = '待发布'

                break

              case 1:

                task.status = '进行中'

                break

              case 2:

                task.status = '已结束'

                break

            }

            that.tasklist.push({

              id: task.id,

              title: task.title,

              status: task.status,

              publishTime: Date(task.publishTime),

              ddlTime: Date(task.ddlTime),

              tags: task.tag,

              language: task.language,

              description: task.description

            })

          }

          that.page_total_num = that.tasklist.length

          that.setPageList(1)

        })

      }).catch(function (ex) {

        alert('Network Error')

      })

    },

    methods: {

      checkTaskDetail: function (taskid) {

        this.$router.push('/task/' + taskid)

      },

      setPageList (page) {

        this.pageList.splice(0, this.pageList.length)

        this.pageList = this.tasklist.slice((page - 1) * 5, page * 5)

      }

    }

  }

</script>



<!-- Add "scoped" attribute to limit CSS to this component only -->

<style scoped>

  .root {

    margin-left: 460px;

    width: 600px;

    padding: 20px;

  }

  .card {

    margin-bottom: 20px;

  }


  #taskListTitle {

    text-align: left;

    padding: 10px 0 10px 20px;

  }

  #taskTitle {

    font-size: 16px;

    text-align: left;

  }

  #taskDescription {

    text-align: left;

    color: #495060;

  }

  #taskTime, #taskStatus {

    font-size: 12px;

    text-align: left;

    color: #80848f;

  }

  #pages {

    padding: 20px;

  }


  h4 {

    font-size: 12px;

  }