import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/pages/home'
import Province from '@/pages/province'
import Map from '@/pages/map'
import Test from '@/pages/test'
import WholeChina from '@/pages/wholeChina'
import SightDetail from '@/pages/sightDetail'

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
      path: '/home/province',
      name: 'Province',
      component: Province,
    },
    {
      path: '/home/province/sightDetail',
      name: 'SightDetail',
      component: SightDetail,
    },
    {
      path: '/map',
      name: 'Map',
      component: Map,
    },
    {
      path: '/wholeChina',
      name: 'WholeChina',
      component: WholeChina,
    },
    {
      path: '/test',
      name: 'Test',
      component: Test,
    },
  ]
})
