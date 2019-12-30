<template>
  <div class="specificartical borderStyle container" >
    <h1 class='title'>{{specific.title}} </h1>
    <div class='content'>
      <div><span class='annotation'><i></i>{{specific.date}}</span>/
        <span class='annotation'><i></i>{{specific.browse}}</span>/
        <div>{{specific.content}}</div>
        <div class='attention'><i>@</i></div>
        <div class='lable'><i>*</i><a v-for="(tag,index) in specific.tags" :key="index">{{index!=0?',':''}}{{tag}}</a></div>
      </div>

    </div>
  </div>
</template>

<script>
  import {mapState,  mapActions} from 'vuex'
  export default {
    name: 'specificartical',
    computed: {
      ...mapState({
        specific:state=>state.ArchiveStore.specific,
      })
    },
    methods:{
      ...mapActions([
        'getArticlesSpecific'
      ]),
    },
    activated:function(){this.getArticlesSpecific(this.$route.params.id);
    }
  }
</script>
