<template>
  <el-container>
    <el-header style="text-align: left; font-size: 12px;">
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
                v-model="value1" type="datetimerange" :picker-options="pickerOptions" range-separator="至" start-placeholder="开始日期" end-placeholder="结束日期" align="right">
              </el-date-picker>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item>
              <el-button type="primary">搜索</el-button>
              <el-button type="primary" @click="resetForm('form')">重置</el-button>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
    </el-header>
    <el-main>
      <router-view />
      <el-container>
        <el-table :data="tableData" stripe style="width: 100%">
          <el-table-column type="selection" prop="id" label="用例编号" width="180"></el-table-column>
          <el-table-column prop="title" label="用例标题" width="180"></el-table-column>
          <el-table-column prop="code" label="脚本"></el-table-column>
          <el-table-column prop="createtime" label="创建时间"></el-table-column>
          <el-table-column prop="casetype" label="用例类型"></el-table-column>
          <el-table-column prop="testresult" label="执行结果"></el-table-column>
        </el-table>
      </el-container>
    </el-main>
  </el-container>
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
          value1: '',
          tableData: [{
            id: '001',
            title: '登录用例',
            code: '/login',
            createtime:'2019-12-27',
            casetype:'UIcase',
            testresult:'未执行'
          }]
        }
      },
      methods: {
        onSubmit() {
          console.log('submit!');
        },
        resetForm(form) {
          this.$refs[form].resetFields();
        }
      }
    }
</script>

<style scoped>

</style>
