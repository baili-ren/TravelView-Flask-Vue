<template>
  <div>
    <el-menu
      :default-active="this.$route.path"
      class="side-menu"
      @open="handleOpen"
      @close="handleClose"
      :collapse="isCollapse"
      style="height: 100%"
      router
    >
       <el-menu-item index="/home">
        <i class="el-icon-menu"></i>
        <span slot="title">省份数据</span>
      </el-menu-item>
      <el-menu-item index="/map">
        <i class="el-icon-menu"></i>
        <span slot="title">散点地图</span>
      </el-menu-item>
      <el-menu-item index="/wholeChina">
        <i class="el-icon-menu"></i>
        <span slot="title">旅游经济</span>
      </el-menu-item>
      <!-- <el-submenu index="3">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span slot="title">导航三</span>
        </template>
        <el-menu-item-group>
          <span slot="title">分组一</span>
          <el-menu-item index="1-1">选项1</el-menu-item>
          <el-menu-item index="1-2">选项2</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group title="分组2">
          <el-menu-item index="1-3">选项3</el-menu-item>
        </el-menu-item-group>
        <el-submenu index="1-4">
          <span slot="title">选项4</span>
          <el-menu-item index="1-4-1">选项1</el-menu-item>
        </el-submenu>
      </el-submenu> -->
      <el-menu-item  @click="toggleCollapse" class="item-bottom">
        <i :class=" isCollapse? 'el-icon-caret-right': 'el-icon-caret-left'"></i>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: "SideNav",
  data() {
    return {
      isCollapse: true,
    };
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    toggleCollapse() {
      this.isCollapse = !this.isCollapse;
      this.$emit("isCollapse", this.isCollapse);
    },
  },
};
</script>

<style scoped lang = "scss">
.side-menu {
  .item-bottom {
    position: fixed;
    bottom: 0;
  }
}

</style>