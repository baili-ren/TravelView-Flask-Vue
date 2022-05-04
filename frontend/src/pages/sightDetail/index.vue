<template>
  <div class="sight-detail-container">
    <!-- <baidu-map>
      <bm-view class="baidu-aa-view" style="width: 100%; height:100px; flex: 1"></bm-view>
    </baidu-map> -->
     <baidu-map class="map" :center="{lng: 116.404, lat: 39.915}" :zoom="15" :scroll-wheel-zoom="true">
  </baidu-map>
  </div>
</template>

<script>
export default {
  name: "SightDetail",
  components: {},
  data() {
    return {
      location: "",
      keyword: "",
    };
  },
  mouted: {},
  methods: {},
};
</script>

<style scoped lang="scss">
sight-detail-container {
  height: calc(100% - 32px);
  width: calc(100% - 32px);
  .baidu-aa-view{
      border: 5px red solid;
    //   width:100%;
    //   height: 100px;
    //   flex:1;
  }
}
</style>
