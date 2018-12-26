<template>

  <div class="root">

    <div id="left">

      <div class="card"><Card dis-hover><h2>{{ title }}</h2></Card></div>

      <div class="card"><Card dis-hover padding="0">

        <div id="taskTitle"><h3 style="text-align: left;">细分任务详情</h3></div>

        <ul>

          <li v-for="a in assignments">

            <Card>

              <Row class="text">

                <Col span="2"><h3>{{ a.order }}</h3></Col>

                <Col span="22" class="left">

                  <p>任务状态: {{ a.status }}</p>

                  <p>任务描述: </p>

                  <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ a.description }}</p>

                  <p v-if="(a.status == '进行中' || a.status == '已完成' || a.status == '纠纷中') && isowner">翻译结果:&nbsp;<a :href="DownloadAssignment(a.submission)">{{ a.submission }}</a></p>

                  <div class="button">

                    <Button type="primary" @click="callConfirm(a)" v-if="a.status == '进行中' && isowner">任务验收</Button>

                    <Button type="primary" v-if="a.status == '试译中' && isowner" @click="callTestConfirm(a)" >查看试译结果</Button>

                    <Button type="primary" @click="pickup(a)" v-if="a.status == '待领取' && !isowner">领取任务</Button>

                    <span v-if="a.status == '已完成'">任务评分:&nbsp;<Rate allow-half disabled v-model="a.score"><span class="orange">{{ a.score }}</span></Rate></span>

                  </div>

                  <span v-if="a.status == '纠纷中' && isowner">

                    <p v-if="!a.hasDispute">请耐心等待翻译者回应</p>

                    <p v-if="a.hasDispute">请耐心等待管理员处理</p>

                  </span>

                  <span v-if="a.status == '已完成' && isowner && a.hasDispute">

                    <p v-if="a.disputeResult == 0"> 申诉状态：未完成（发生未知错误） </p>

                    <p v-if="a.disputeResult == 1"> 申诉状态：管理员同意了翻译者的申诉，评语：{{a.statement}} </p>

                    <p v-if="a.disputeResult == 2"> 申诉状态：管理员拒绝了翻译者的申诉，评语：{{a.statement}} </p>

                  </span>

                </Col>

              </Row>

            </Card>

          </li>

        </ul>

        <Modal title="试译结果" v-model="testConfirm" :mask-closable="false" :loading="loading">

          <p class="bottom-10">试译语段：</p>

          <p class="bottom-10">{{ testText }}</p>

          <p class="bottom-10">翻译结果：</p>

          <p class="bottom-10">{{ testResult }}</p>

          <div slot="footer">

            <Button type="error" @click="responseTestResult(false)">不通过</Button>

            <Button type="primary" @click="responseTestResult(true)">通过</Button>

          </div>

        </Modal>

        <Modal title="确认任务" v-model="modalConfirm" :mask-closable="false" @on-ok="acceptAssignment" :loading="loading">

          <RadioGroup v-model="confirm" class="options">

            <Radio label="accept"></Radio>

            <Radio label="reject"></Radio>

          </RadioGroup><br>

          <Rate v-if="confirm === 'accept'" show-text allow-half v-model="valueCustomText">

            <span class="orange">{{ valueCustomText }}</span>

          </Rate>

          <Input v-else v-model="text" type="textarea" :rows="4" placeholder="请写出你的拒绝理由"></Input>

        </Modal>

      </Card></div>

    </div>

    <div id="right" :class="rightFixed === true ? 'isFixed' :''">

      <div class="card"><Card dis-hover>

        <h3 id="right-info">任务信息</h3>

        <p>任务状态：{{ status }}</p>

        <p>任务描述：{{ description }}</p>

        <p>任务语言：{{ language }}</p>

        <p>资质要求：{{ requirementLicense }}</p>

        <p>发布时间：{{ publishTime }}</p>

        <p>截止时间：{{ ddlTime }}</p>

        <p>要求译者等级：&nbsp;<Rate allow-half disabled v-model="requirementLevel"></Rate></p>

        <p>任务文件：<a :href="DownloadTask(taskFile)">{{ taskFile }}</a></p>

        <Button v-if="status == '待发布'" @click="publishTask"  type="info">立即发布</Button>

      </Card></div>

    </div>

  </div>

</template>