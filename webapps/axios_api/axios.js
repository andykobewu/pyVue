/* jshint esversion: 6 */

import axios from 'axios';
import Cookies from "js-cookie";
import config from './config';
import router from '@/router';
import { Toast} from 'vant';

export default function $axios(options) {
  return new Promise((resolve, reject) => {
    const instance = axios.create({
      baseURL: config.baseUrl,
      headers: config.headers,
      timeout: config.timeout,
      withCredentials: config.withCredentials,
    });

    // request 拦截器
    instance.interceptors.request.use(
      config => {
        //在发送之前做点什么
        let auth_token = Cookies.get('auth_token');
        if (auth_token) {
          config.headers.auth_token = auth_token;
        } else {
          let loginpage = Cookies.get('loginpage');
          if (loginpage) {
            router.push('/login');
          }
        }
        if (config.method === 'post') {}
        return config;
      },
      error => {
        // 判断请求超时
        if (error.code === 'ECONNABORTED' && error.message.indexOf('timeout') !== -1) {
          Toast("信号不好，请求超时")
        }
      }

    );

    // response 拦截器
    instance.interceptors.response.use(
      response => {
        //对响应数据做点什么
        let data;
        if (response.data == undefined) {
          data = JSON.parse(response.request.responseText);
        } else {
          data = response.data;
        }
        return data;
      },
      err => {
        if (err && err.response) {
          console.log(err)
        }// 返回接口返回的错误信息
        return Promise.reject(err);
      }
    );

    // 请求处理
    instance(options).then(res => {
      resolve(res);
      return false;
    }).catch(error => {
      reject(error);
    });
  });
}
