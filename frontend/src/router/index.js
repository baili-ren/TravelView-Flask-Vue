import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/pages/home'
import Province from '@/pages/province'
import Map from '@/pages/map'


Vue.use(Router)

export default new Router({
  routes: [{
      path: '/',
      redirect: '/home'
    },
    {
      path: '/home',
      name: 'Home',
      component: Home,
      // children: [
      //   {
      //     path: '/home/test',
      //     component: () => import('../pages/test')
      //   },
      // ]
    },
    {
      path: '/map',
      name: 'map',
      component: Map,
    },
    {
      path: '/home/province',
      name: 'province',
      component: Province,
    },
  ]
})
