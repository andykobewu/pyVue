import Vue from 'vue'
import VueRouter from 'vue-router'
import router from './router'
import VueWechatTitle from 'vue-wechat-title'
import Vuex from 'vuex'
import store from './store'
import api from '../axios_api'
Vue.use(api)
Vue.use(Vuex)
Vue.use(VueWechatTitle)
// 导入 ElementUI
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

import App from './App'

// 安装路由
Vue.use(VueRouter);

// 安装 ElementUI
Vue.use(ElementUI);

new Vue({
  el: '#app',
  store,
  // 启用路由
  router,
  // 启用 ElementUI
  render: h => h(App),

});
// 在跳转前执行
router.beforeEach((to, form, next) => {
  // 获取用户登录状态
  let isLogin = sessionStorage.getItem('isLogin');

  // 注销
  if (to.path == '/logout') {
    // 清空
    sessionStorage.clear();

    // 跳转到登录
    next({path: '/login'});
  }

  // 如果请求的是登录页
  else if (to.path == '/login') {
    if (isLogin != null) {
      // 跳转到首页
      next({path: '/main'});
    }
  }
  else if (to.path == '/test') {
    if (isLogin != null) {
      // 跳转到test
      next({path: '/test'});
    }
  }

  // 如果为非登录状态
  else if (isLogin == null) {
    // 跳转到登录页
    next({path: '/login'});
  }

  // 下一个路由
  next();
});
