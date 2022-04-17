module.exports = {
  proxy: {
    '/api': { //将xxx域名印射为/apis
      target: 'http://127.0.0.1:5000', // 接口域名
      //   secure: false, // 如果是https接口，需要配置这个参数
      changeOrigin: false, //是否跨域
      // pathRewrite: {
      //   '^/api': '' //需要rewrite的,
      // }
    }
  }
}
