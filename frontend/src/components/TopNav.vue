<template>
  <div class="top-nav">
    <div class="top-nav-title">旅游数据分析系统</div>
  </div>
</template>

<script>
export default {
  name: "TopNav",
  data() {
    return {};
  },
};
</script>

<style scoped lang="scss">
.top-nav {
  &-title {
    color: #ffffff;
    font-family: "Roboto",fallback-font;
    font-size: 20px;
    font-weight: 550;
    letter-spacing: 2px;
    line-height: 60px;
    margin-left: 16px;
  }
}
</style>