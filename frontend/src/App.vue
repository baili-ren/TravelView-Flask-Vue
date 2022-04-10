<template>
  <div id="app">
    123
    <div>{{info}}</div>
     <el-button type="primary" @click="getInfo">主要按钮</el-button>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      info: "333"
    }
  },
  methods: {
    getInfo() {
      this.axios.post("/api/test",{})
      .then(res => {
        this.info = res.data
        console.log(res,"res===")
      })
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
