<template>
  <div>
    <el-form
      :model="from"
      :rules="rules"
      ref="from"
      label-width="100px"
      class="demo-from"
    >
      <el-form-item label="竞赛封面">
        
      </el-form-item>
      
      <el-form-item label="竞赛名称名称" prop="name">
        <el-input v-model="from.name"></el-input>
      </el-form-item>
      <el-form-item label="主办方" prop="sponsor">
        <el-input v-model="from.sponsor"></el-input>
      </el-form-item>
      <el-form-item label="报名时间" required>
        <el-col :span="11">
          <el-form-item prop="date1">
            <el-date-picker
              type="date"
              placeholder="选择日期"
              v-model="from.date1"
              style="width: 100%;"
            ></el-date-picker>
          </el-form-item>
        </el-col>
        <el-col class="line" :span="2">-</el-col>
        <el-col :span="11">
          <el-form-item prop="date2">
            <el-date-picker
              type="date"
              placeholder="选择日期"
              v-model="from.date2"
              style="width: 100%;"
            ></el-date-picker>
          </el-form-item>
        </el-col>
      </el-form-item>
      <el-form-item label="比赛时间" required>
        <el-col :span="11">
          <el-form-item prop="date3">
            <el-date-picker
              type="date"
              placeholder="选择日期"
              v-model="from.date3"
              style="width: 100%;"
            ></el-date-picker>
          </el-form-item>
        </el-col>
        <el-col class="line" :span="2">-</el-col>
        <el-col :span="11">
          <el-form-item prop="date4">
            <el-date-picker
              type="date"
              placeholder="选择日期"
              v-model="from.date4"
              style="width: 100%;"
            ></el-date-picker>
          </el-form-item>
        </el-col>
      </el-form-item>
      <el-form-item label="赛事详情" prop="desc">
        <el-input type="textarea" v-model="from.desc"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('from')">立即创建</el-button>
        <el-button @click="resetForm('from')">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      from: {
        name: "",
        sponsor: "",
        date1: "",
        date2: "",
        date3: "",
        date4: "",
        desc: ""
      },
      rules: {
        name: [{ required: true, message: "请输入活动名称", trigger: "blur" }],
        sponsor: [{ required: true, message: "主办方", trigger: "blur" }],
        date1: [
          {
            type: "date",
            required: true,
            message: "请选择日期",
            trigger: "change"
          }
        ],
        date2: [
          {
            type: "date",
            required: true,
            message: "请选择日期",
            trigger: "change"
          }
        ],
        date3: [
          {
            type: "date",
            required: true,
            message: "请选择日期",
            trigger: "change"
          }
        ],
        date4: [
          {
            type: "date",
            required: true,
            message: "请选择日期",
            trigger: "change"
          }
        ],
        desc: [{ required: true, message: "请填写活动形式", trigger: "blur" }]
      }
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          alert("创建成功!");
        } else {
          console.log("创建失败!");
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    }
  }
};
</script>

<style scoped>
</style>
