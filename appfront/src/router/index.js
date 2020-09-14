import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Book from '@/components/Book'
import VideosLayout from '@/components/VideosLayout'
import Video from '@/components/Video'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/book',
      name: 'Book',
      component: Book
    },
    {
      path: '/video',
      name: 'Video',
      component: Video
    },
    {
      path: '/video_layout',
      name: 'VideosLayout',
      component: VideosLayout
    }
  ]
})
