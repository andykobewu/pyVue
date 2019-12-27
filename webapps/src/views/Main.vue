<template>
  <div>
    <el-container>
      <el-aside width="200px">
        <el-menu :default-openeds="['1']">
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-caret-right"></i>用例管理</template>
            <el-menu-item-group>
              <el-menu-item index="1-1">
                <router-link to="/mainChildrenPage/UIcase" class="cancel-link"><i class="el-icon-s-platform"></i>前端用例</router-link>
              </el-menu-item>
              <el-menu-item index="1-2">
                <router-link to="/mainChildrenPage/Restcase" class="cancel-link"><i class="el-icon-s-unfold"></i>接口用例</router-link>
              </el-menu-item>
              <el-menu-item index="1-3">
                <router-link to="/mainChildrenPage/Appcase" class="cancel-link"><i class="el-icon-mobile-phone"></i>App用例</router-link>
              </el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title"><i class="el-icon-caret-right"></i>报告管理</template>
            <el-menu-item-group>
              <el-menu-item index="2-1"><i class="el-icon-document"></i>前端测试报告</el-menu-item>
              <el-menu-item index="2-2"><i class="el-icon-document"></i>接口测试报告</el-menu-item>
              <el-menu-item index="2-2"><i class="el-icon-document"></i>App测试报告</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
        </el-menu>
      </el-aside>

      <el-container>
        <el-header style="text-align: left; font-size: 12px;">
          <span>titlename</span>
          <div style="float: right">
            <el-dropdown>
              <i class="el-icon-setting" style="margin-right: 15px"></i>
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item>个人信息</el-dropdown-item>
                <el-dropdown-item>退出登录</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
            <span>admin</span>
          </div>
        </el-header>
        <el-main>
          <router-view />

        </el-main>
      </el-container>
    </el-container>

  </div>
</template>

<script>
  export default {
    name: "Main",
    data() {
      return {
        tableData: [{
          id: '001',
          title: '登录用例',
          code: '/login'
        }, {
          date: '2016-05-04',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1517 弄'
        }, {
          date: '2016-05-01',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1519 弄'
        }, {
          date: '2016-05-03',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1516 弄'
        }]
      }
    },
    methods: {
      created() {
        this.titlename = this.$route.params.children.title
      }
    }
  }
</script>

<style scoped lang="scss">
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }

  .el-aside {
    color: #333;
  }
  .cancel-link {
    text-decoration: none;
  }
</style>
