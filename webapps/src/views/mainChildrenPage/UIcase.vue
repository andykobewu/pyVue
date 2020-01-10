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
              <el-button type="primary" icon="el-icon-search">搜索</el-button>
              <el-button type="primary" @click="resetForm('form')" icon="el-icon-brush">重置</el-button>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
    </el-header>
    <el-main>
      <router-view />
      <el-container>
        <div>
          <el-row  type="flex" class="row-bg" :gutter="2" justify="end" :span="24">
            <el-col><div class="grid-content bg-purple"><el-button type="primary" icon="el-icon-plus" @click="addFn">新增</el-button></div></el-col>
            <el-col><div class="grid-content bg-purple"><el-button type="primary" icon="el-icon-edit-outline">修改</el-button></div></el-col>
            <el-col><div class="grid-content bg-purple"><el-button type="primary" icon="el-icon-delete">删除</el-button></div></el-col>
            <el-col>
              <el-upload class="upload-demo" ref="upload" action="doUpload" :limit="10" :file-list="fileList" :before-upload="beforeUpload" :show-file-list="false">
                <el-button slot="trigger"  type="primary">导入用例</el-button>
              </el-upload>
            </el-col>
            <a href="../static/moban.xlsx" rel="external nofollow" download="前端用例模板">
              <el-button  type="success">下载用例</el-button>
            </a>
          </el-row>
        </div>
      </el-container>
      <el-container style="height: 500px; border: 1px solid #eee" >
        <div>
          <el-row :span="24" style=" float:left;white-space: pre-line;" ref="refForm">
            <el-table :data="tableData" stripe style="width: 100%" :border="true">
              <el-table-column type="selection" prop="id" label="用例编号" width="180"></el-table-column>
              <el-table-column prop="title" label="用例名称" width="180"></el-table-column>
              <el-table-column prop="code" label="脚本"></el-table-column>
              <el-table-column prop="createtime" label="创建时间"></el-table-column>
              <el-table-column prop="casetype" label="用例类型"></el-table-column>
              <el-table-column prop="testresult" label="执行结果"></el-table-column>
            </el-table>
          </el-row>
        </div>
      </el-container>
      <el-container>
        <el-dialog :visible="newdialogVisible" width="60%" @close="cancel" title="新增用例">
          <el-form :inline="true" :model="editForm" ref="newform" label-width="110px" :rules="rules">
            <el-form-item label="用例名称" prop="name">
              <el-input v-model="editForm.newcaseName"></el-input>
            </el-form-item>
            <el-form-item label="用例编号" prop="id">
              <el-input v-model="editForm.newcaseId"></el-input>
            </el-form-item>
            <el-form-item label="脚本" prop="script">
              <el-input v-model="editForm.newcasescript" type="textarea" placeholder="请输入要执行的脚本"></el-input>
            </el-form-item>
            <el-form-item label="用例类型" prop="type">
              <el-input v-model="editForm.casetype" disabled></el-input>
            </el-form-item>
            <el-form-item label="执行结果" prop="result">
              <el-input v-model="editForm.result" disabled></el-input>
            </el-form-item>
          </el-form>
          <div slot="footer" align="center">
            <el-button type="primary" @click="sureAdd">确定</el-button>
            <el-button type="primary" @click="cancel">取消</el-button>
          </div>
        </el-dialog>
      </el-container>
    </el-main>
  </el-container>
</template>

<script>
  import axios from 'axios'
    export default {
      name: "UIcase",
      data() {
        return {
          editForm: {
            newcaseId: '',
            newcaseName: '',
            newcasescript:'',
            casetype:'UI用例',
            result:'未执行'
          },
          rules: {
            name: [{required: true, message: '', trigger: 'blur'}],
            id: [{required: true, message: '', trigger: 'blur'}],
            script: [{required: true, message: '', trigger: 'blur'}],
            type: [{required: false, message: '', trigger: 'blur'}],
            result: [{required: false, message: '', trigger: 'blur'}],

          },
          form: {
            name: '',
            region: '',
            date1: '',
            date2: ''
          },
          urls: {
            create: '/api/createcase/'
          },
          newdialogVisible:false,
          viewType: 'ADD',
          fileList: [],
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
        getcaselist(){

        },
        sureAdd: function () {
          var _self = this;
          _self.getdate();
          var formUrl = _self.urls.create;
          var param = {
            caseName: _self.editForm.newcaseName,
            // flowAdmin: _self.commonparams.CurrentuserId,
            systemId: 'AUTOTEST',
            startTime: _self.startTime
          };
          _self.$refs.newform.validate(function (valid) {
            if (!valid) {
              _self.$message({
                message: '请检查输入项是否合法!',
                type: 'warning'
              });
              return;
            }
          });
          service.request({
            method: 'POST',
            url: formUrl,
            data: param,
            callback: function (code, message, response) {
              if (response.code === 0) {
                _self.$refs.reftable.remoteData();
                _self.$message('用例新增成功!');
                _self.newdialogVisible = false;
              } else {
                _self.$message({message: response.message, type: 'error'});
              }
            }
          });
        },
        getdate: function () {
          var d = new Date();
          var year = d.getFullYear();
          var month = (d.getMonth() + 1) < 10 ? '0' + (d.getMonth() + 1) : d.getMonth() + 1;
          var date = d.getDate() < 10 ? '0' + d.getDate() : d.getDate();
          var hour = d.getHours() < 10 ? '0' + d.getHours() : d.getHours();
          var minutes = d.getMinutes() < 10 ? '0' + d.getMinutes() : d.getMinutes();
          var seconds = d.getSeconds() < 10 ? '0' + d.getSeconds() : d.getSeconds();
          var myWant = year + '-' + month + '-' + date + ' ' + hour + ':' + minutes + ':' + seconds;
          this.startTime = myWant;
        },
        resetForm(form) {
          this.$refs[form].clearSelection();
        },
        /**
         * 控制保存按钮、xdialog、表单的状态
         * @param viewType 表单类型
         * @param editable 可编辑,默认false
         */
        switchStatus: function (viewType, editable) {
          var _self = this;
          _self.viewType = viewType;
          if (viewType == 'EDIT') {
            _self.updatedialogVisible = true;
          } else if (viewType == 'ADD') {
            _self.newdialogVisible = true;
          }
        },
        /**
         * 新增按钮
         */
        addFn: function () { // 新增
          var _self = this;
          _self.switchStatus('ADD', true); // 切换面板状态
        },
        beforeUpload(file){
          console.log(file,'文件');
          this.files = file;
          const extension = file.name.split('.')[1] === 'xls'
          const extension2 = file.name.split('.')[1] === 'xlsx'
          const isLt2M = file.size / 1024 / 1024 < 5
          if (!extension && !extension2) {
            this.$message.warning('上传模板只能是 xls、xlsx格式!')
            return
          }
          if (!isLt2M) {
            this.$message.warning('上传模板大小不能超过 5MB!')
            return
          }
          this.fileName = file.name;
          return false // 返回false不会自动上传
        },
        submitUpload() {
          console.log('上传'+this.files.name)
          if(this.fileName == ""){
            this.$message.warning('请选择要上传的文件！')
            return false
          }
          let fileFormData = new FormData();
          fileFormData.append('file', this.files, this.fileName);//filename是键，file是值，就是要传的文件，test.zip是要传的文件名
          let requestConfig = {
            headers: {
              'Content-Type': 'multipart/form-data'
            },
          }
          this.$http.post(`/basedata/oesmembers/upload?companyId=`+this.company, fileFormData, requestConfig).then((res) => {
            debugger
            if (data && data.code === 0) {
              this.$message({
                message: '操作成功',
                type: 'success',
                duration: 1500,
                onClose: () => {
                  this.visible = false
                  this.$emit('refreshDataList')
                }
              })
            } else {
              this.$message.error(data.msg)
            }
          })
        },
        cancel: function () {
          var _self = this;
          _self.newdialogVisible = false;
          _self.$nextTick(function () {
            _self.editForm.newflowName = '';
          });
        }

      }
    }
</script>

<style scoped>
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {

  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
</style>
