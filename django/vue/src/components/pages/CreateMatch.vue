<template>
  <div>
    <el-form :model="form" ref="form" label-width="100px" class="demo-form">
      <el-form-item label="竞赛封面" prop="img">
        <el-upload
          action="#"
          :limit="1"
          accept="image/jpeg, image/jpg, image/png"
          :auto-upload="false"
          :on-exceed="handleExceed"
          :before-upload="handleBefore"
          :file-list="fileList"
          :on-remove="handleRemove"
          list-type="picture"
        >
          <el-button type="primary" size="small">上传图片</el-button>
        </el-upload>
      </el-form-item>
      <el-form-item label="竞赛名称" prop="title">
        <el-input v-model="form.title"></el-input>
      </el-form-item>
      <el-form-item label="主办方" prop="sponsor">
        <el-input v-model="form.sponsor"></el-input>
      </el-form-item>
      <el-form-item label="报名时间" required>
        <el-col :span="11">
          <el-form-item prop="sign_up_start">
            <el-date-picker
              type="date"
              placeholder="选择日期"
              v-model="form.sign_up_start"
              style="width: 100%;"
            ></el-date-picker>
          </el-form-item>
        </el-col>
        <el-col class="line" :span="2">-</el-col>
        <el-col :span="11">
          <el-form-item prop="sign_up_end">
            <el-date-picker
              type="date"
              placeholder="选择日期"
              v-model="form.sign_up_end"
              style="width: 100%;"
            ></el-date-picker>
          </el-form-item>
        </el-col>
      </el-form-item>
      <el-form-item label="比赛时间" required>
        <el-col :span="11">
          <el-form-item prop="start_time">
            <el-date-picker
              type="date"
              placeholder="选择日期"
              v-model="form.start_time"
              style="width: 100%;"
            ></el-date-picker>
          </el-form-item>
        </el-col>
        <el-col class="line" :span="2">-</el-col>
        <el-col :span="11">
          <el-form-item prop="end_time">
            <el-date-picker
              type="date"
              placeholder="选择日期"
              v-model="form.end_time"
              style="width: 100%;"
            ></el-date-picker>
          </el-form-item>
        </el-col>
      </el-form-item>
      <el-form-item label="赛事详情" prop="description">
        <el-input type="textarea" v-model="form.description"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('form')">立即创建</el-button>
        <el-button @click="resetForm('form')">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        id: 0,
        title: "",
        img: "",
        sponsor: "",
        sign_up_start: "",
        sign_up_end: "",
        start_time: "",
        end_time: "",
        description: "",
        username:""
      },
      fileList: [],
      items: {username: ""}
      // rules: {
      //   title: [{ required: true, message: "请输入竞赛名称", trigger: "blur" }],
      //   sponsor: [{ required: true, message: "请输入主办方", trigger: "blur" }],
      //   sign_up_start: [
      //     {
      //       type: "date",
      //       required: true,
      //       message: "请选择日期",
      //       trigger: "change"
      //     }
      //   ],
      //   sign_up_end: [
      //     {
      //       type: "date",
      //       required: true,
      //       message: "请选择日期",
      //       trigger: "change"
      //     }
      //   ],
      //   start_time: [
      //     {
      //       type: "date",
      //       required: true,
      //       message: "请选择日期",
      //       trigger: "change"
      //     }
      //   ],
      //   end_time: [
      //     {
      //       type: "date",
      //       required: true,
      //       message: "请选择日期",
      //       trigger: "change"
      //     }
      //   ],
      //   description: [{ required: true, message: "请填写竞赛详情", trigger: "blur" }]
      // }
    };
  },
  methods: {
    submitForm(formtitle) {
      this.$refs[formtitle].validate(valid => {
        if (valid) {
          let str1 = this.dateToString(this.form.sign_up_start);
          let str2 = this.dateToString(this.form.sign_up_end);
          let str3 = this.dateToString(this.form.start_time);
          let str4 = this.dateToString(this.form.end_time);
          console.log(str1);
          consol
          e.log(str2);
          console.log(str3);
          console.log(str4);
          this.form.sign_up_start = str1;
          this.form.sign_up_end = str2;
          this.form.start_time = str3;
          this.form.end_time = str4;
          this.form.username = this.items.username;
          this.form.id = this.$store.state.matchid
          this.$store.commit('creatematch', this.form)
          this.$http.post('http://127.0.0.1:8000/api/create_competition/',this.form,
                          {headers: {'Content-Type': 'application/x-www-form-urlencoded'}});
          alert("创建成功!");
        } else {
          console.log("创建失败!");
          return false;
        }
      });
    },
    resetForm(formtitle) {
      this.$refs[formtitle].resetFields();
    },
    handleBefore(file) {
      const isIMAGE =
        file.raw.type === "image/jpeg" ||
        file.raw.type === "image/jpg" ||
        file.raw.type === "image/png";
      if (!isIMAGE) {
        this.$message.error("上传图片只能是 jpg,jpeg,png格式!");
        return false;
      }
      this.img = file;
      return false;
    },
    handleExceed(file, fileList) {
      this.$message.error(
        `当前限制选择 1 个文件，本次选择了 ${
          files.length
        } 个文件，共选择了 ${files.length + fileList.length} 个文件`
      );
    },
    handleRemove(file, fileList) {
      fileList.length = 0;
      this.img = "";
    },
    dateToString(date){ 
      var year = date.getFullYear(); 
      var month =(date.getMonth() + 1).toString(); 
      var day = (date.getDate()).toString();  
      if (month.length == 1) { 
        month = "0" + month; 
      } 
      if (day.length == 1) { 
        day = "0" + day; 
      }
      var dateTime = year + "-" + month + "-" + day;
      return dateTime; 
  }
  },
  mounted(){
    this.items.username=sessionStorage.getItem("username");
  }
};
</script>

<style scoped>
</style>
