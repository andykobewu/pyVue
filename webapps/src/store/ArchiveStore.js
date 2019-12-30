import axios from '../assets/js/axios'

const actions = {
  specific: {
    browse: 0,
    content: '',
    title: '',
    date: '',
    tags: []
  }
}

getArticlesSpecific({ commit, state }, id)
{ //得到指定文章详情
  axios.Get({
    url: 'get_article_specific',
    params: {
      id: id
    },
    callback: (res) => {
      // console.log(res);
      let data = res.data
      state.specific = {
        browse: data['browse'],
        content: data['content'],
        title: data['title'],
        date: data['date'],
        tags: data['tags']
      }
      state.loading = false;
      //   specific
    }
  })

}
