/*
 * 系统登录模块
 */
import axios from '../axios'
// 登录
export const login = (data) => {
  return axios({
    url: '/test',
    method: 'post',
    data:'登录成功'
  });
};
