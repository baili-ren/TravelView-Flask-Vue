import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import Home from '@/pages/home'
// import Province from '@/pages/province'
import ChinaMap from '@/pages/chinaMap'


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
      children: [
        {
          path: '/home/map',
          component: () => import('../pages/chinaMap')
        },
      ]
    },
    {
      path: '/map',
      name: 'map',
      component: ChinaMap,
    },
  ]
})
