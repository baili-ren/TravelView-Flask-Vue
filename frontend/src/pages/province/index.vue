<template>
    <div>
      provience
      <span>{{provienceName}}</span>
      <el-button type="info" icon="el-icon-back" circle @click="goBack"></el-button>
    </div>
</template>

<script>
export default {
  name: 'Province',
  data () {
    return {
      provienceName: 111,
    }
  },
  mounted(){
    this.initData()
  },
  methods: {
    initData(){
      this.provienceName = this.$router.history.current.query
      console.log(this.$router.history,'this.$router.history==== 省份页面')
    },
    goBack() {
      this.$router.back();
    }
  }
}
</script>

<style scoped lang = "scss">

</style>