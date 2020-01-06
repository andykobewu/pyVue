<template>
  <div id="app">
    <div v-for="item in listone" :key="item.id"> <img :src="item.imgurl" alt="" class="img"></div>
  </div>
</template>

<script>
    export default {
        name: "test",
      data(){
        return{
          listone:[]
        }
      },
      //执行方法
      created(){
        this.GetListImg();
      },
      //方法
      methods:{
        GetListImg(){
          var that = this;
          that.$axios({
            methods:"get",
            //接口地址  api-代理+接口端口号之后的其余地址
            url:"/test"
          }).then(response =>{
            //验证数据是否获取到
            // console.log(response.data);
            that.listone=response.data.data.listone;
            console.log(that.listone);
          })
        }
      }
    }
</script>

<style scoped>

</style>
