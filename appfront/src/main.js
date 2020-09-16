// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import 'element-ui/lib/theme-chalk/index.css'
import ElementUI from 'element-ui'
import VideoPlayer from 'vue-video-player'
import axios from 'axios'
Vue.prototype.$axios = axios
let getCookie = function (cookie) {
  let reg = /csrftoken=([\w]+)[;]?/g
  return reg.exec(cookie)[1]
}

axios.interceptors.request.use(
  function (config) {
    // 在post请求前统一添加X-CSRFToken的header信息
    let cookie = document.cookie
    // eslint-disable-next-line eqeqeq
    if (cookie && config.method === 'post') {
      config.headers['X-CSRFToken'] = getCookie(cookie)
    }
    return config
  },
  function (error) {
    // Do something with request error
    return Promise.reject(error)
  }
)

require('video.js/dist/video-js.css')
require('vue-video-player/src/custom-theme.css')

Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.use(VideoPlayer)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
