<template>
  <div id="app" class="main-container">
    <div class="main-container-header" @click="testt">
      <top-nav></top-nav>
    </div>
    <div class="main-container-mid">
      <div class="left" :class="isCollapse ? 'left-shrink':'left-expand'">
        <side-nav @isCollapse="getIsCollapse"></side-nav>
      </div>
      <div class="right">
        <router-view />
      </div>
    </div>
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
      isCollapse: true,
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
    getIsCollapse(isCollapse) {
      this.isCollapse = isCollapse
    },
    testt(){
      console.log(this.$router.path,888)
      console.log(this.$route,778)

    }
  },
};
</script>

<style scoped lang="scss">
.main-container {
  height: 100vh;
  width: 100vw;
  &-header {
    height: 60px;
    background: #0f256e;
  }
  &-mid {
    display: flex;
    flex-direction: row;
    // align-items: center;
    height: calc(100vh - 60px);
    .left {
      background: #fff;
      // box-shadow: 1px 0px 6px 0px rgba(32, 33, 36, 0.2);
      box-shadow: 1px 0px 6px 0px red;
    }
    .left-expand {
      width: 200px;
    }
    .left-shrink {
      width: 64px;
    }
    .right {
      padding: 16px;
      width: 100%;
      background: ghostwhite;
    }
  }
}
</style>
