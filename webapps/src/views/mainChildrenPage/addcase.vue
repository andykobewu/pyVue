<template>
  <el-dialog :title="viewTitle[viewType]" :visible.sync="newdialogVisible" width="650px" @close="cancel">
    <yu-form :inline="true" :model="editForm" ref="newform" label-width="110px" :rules="rules">
      <yu-form-item label="流程名称" prop="name">
        <yu-input v-model="editForm.newflowName"></yu-input>
      </yu-form-item>
    </yu-form>
    <div slot="footer" align="center">
      <el-button type="primary" @click="sureAdd">确定</el-button>
      <el-button type="primary" @click="cancel">取消</el-button>
    </div>
  </el-dialog>
</template>

<script>
    export default {
        name: "addcase",
        data(){
          return {
            viewType: 'ADD',
            editForm: {
              newcaseId: '',
              newcaseName: ''
            }
          }

        },
        methods:{
          sureAdd: function () {
            var _self = this;
            _self.getdate();
            var formUrl = _self.urls.create;
            var param = {
              flowName: _self.editForm.newflowName,
              flowAdmin: _self.commonparams.CurrentuserId,
              orgId: yufp.session.org.code,
              systemId: 'cmis',
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
            yufp.service.request({
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
          cancel: function () {
            var _self = this;
            _self.newdialogVisible = false;
            _self.$nextTick(function () {
              _self.editForm.newflowName = '';
            });
          },
        }
    }
</script>

<style scoped>

</style>
