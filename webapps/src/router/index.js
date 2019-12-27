import Vue from 'vue'
import Router from 'vue-router'

import Login from "../views/Login"
import Main from '../views/Main'
import Appcase from '../views/mainChildrenPage/Appcase'
import UIcase from '../views/mainChildrenPage/UIcase'
import Restcase from '../views/mainChildrenPage/Restcase'


Vue.use(Router);

export default new Router({
  routes: [
    {
      // 登录页
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      // 首页
      path: '/main',
      name: 'Main',
      component: Main,
      //配置嵌套路由
      children:[
        {path:'/mainChildrenPage/UIcase',component:UIcase,title:'前端用例' },
        {path:'/mainChildrenPage/Restcase',component:Restcase,title:'接口用例'},
        {path:'/mainChildrenPage/Appcase',component:Appcase,title:'App用例'}
      ]
    },
  ]
});
