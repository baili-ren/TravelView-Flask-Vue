// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import './styles/index.scss'
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from'element-ui'
import'element-ui/lib/theme-chalk/index.css'
import axios from 'axios'
import echarts from 'echarts'
import "echarts/map/js/china.js"
import BaiduMap from 'vue-baidu-map'


Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.prototype.axios = axios
Vue.prototype.$echarts = echarts
//全局挂载
Vue.use(BaiduMap, {
  ak: 'VtvFQV2H0BHUdB7Ynk4FipHAQRKi5SGx'
})
// axios.defaults.baseURL='http://127.0.0.1:5000'
axios.defaults.baseURL='http://119.91.232.173:5000'

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
