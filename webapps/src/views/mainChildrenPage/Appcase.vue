<template>

  <el-form ref="form" :model="form" label-width="80px">
    <el-row>
      <el-col :span="4">
        <el-form-item label="用例名称">
          <el-input v-model="form.name"></el-input>
        </el-form-item>
      </el-col>
      <el-col :span="4">
        <el-form-item label="用例级别">
          <el-select v-model="form.region" placeholder="请选择活动区域">
            <el-option label="级别1" value="001"></el-option>
            <el-option label="级别2" value="002"></el-option>
            <el-option label="级别3" value="003"></el-option>
          </el-select>
        </el-form-item>
      </el-col>
      <el-col :span="10">
        <el-form-item label="创建时间">
          <el-date-picker
            v-model="value1"
            type="datetimerange"
            :picker-options="pickerOptions"
            range-separator="至"
            start-placeholder="开始日期"
            end-placeholder="结束日期"
            align="right">
          </el-date-picker>
        </el-form-item>
      </el-col>
      <el-col :span="6">
        <el-button type="primary">搜索</el-button>
        <el-button type="primary">重置</el-button>
      </el-col>
    </el-row>
  </el-form>
</template>

<script>
  export default {
    name: "UIcase",
    data() {
      return {
        form: {
          name: '',
          region: '',
          date1: '',
          date2: ''
        },
        pickerOptions: {
          shortcuts: [{
            text: '最近一周',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: '最近一个月',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: '最近三个月',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
              picker.$emit('pick', [start, end]);
            }
          }]
        },
        value1: ''
      }
    },
    methods: {
      onSubmit() {
        console.log('submit!');
      }
    }
  }
</script>

<style scoped>

</style>
