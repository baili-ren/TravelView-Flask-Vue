<template>
  <div id="app">
    <el-container class="main-container">
      <el-header class="main-container-header"><top-nav></top-nav></el-header>
      <el-container>
        <el-aside width="200px" class="main-container-side">
          <side-nav></side-nav>
        </el-aside>
        <el-main class="main-container-main">
          <router-view />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import TopNav from "./components/TopNav";
import SideNav from "./components/SideNav";
export default {
  name: "App",
  components: {
    TopNav,
    SideNav,
  },
  data() {
    return {
      info: "333",
      msg: "99",
      info3: "",
    };
  },
  methods: {
    getInfo() {
      this.axios.post("/bb/test", {}).then((res) => {
        this.info = res.data;
        console.log(res, "res===");
      });
      this.axios.post("/apis/test02", {}).then((res) => {
        console.log(res, "res02===");
        this.msg = res.data;
      });
      this.axios.post("/aa", {}).then((res) => {
        this.info3 = res.data;
      });
    },
  },
};
</script>

<style scoped lang="scss">
.main-container {
  background: red;
  &-header{
    background: blanchedalmond;
  }

}
</style>
