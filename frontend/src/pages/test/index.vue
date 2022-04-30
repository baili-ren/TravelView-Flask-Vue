<template>
  <!-- 调用接口 -->
  <div class="map-container">
    <baidu-map class="map" :center="{ lng: 116.404, lat: 39.915 }" :zoom="14">
      <bml-heatmap :data="data" :max="100" :radius="20"> </bml-heatmap>
    </baidu-map>
  </div>
</template>

<script>
import "echarts/extension/bmap/bmap";
import dataJSON from "../../assets/json/data.json";
import geoCoordMapJSON from "../../assets/json/geoCoordMap.json";
import pointsJSON from "../../assets/json/points.json";
import { BmlHeatmap } from "vue-baidu-map";
export default {
  name: "Test",
  components: { BmlHeatmap },
  data() {
    return {
      baiduMapEcharts: null,
      data: [],
      points: null,
      geoCoordMap: {},
      option: {},
      mapData: {},
    };
  },
  mounted() {
    // this.initBaiduMap();
    this.mapData = this.pointsJSON;
  },
  methods: {
    // 初始化数据
    initData() {
      this.data = dataJSON;
      this.geoCoordMap = geoCoordMapJSON;
      this.points = pointsJSON;
    },
    // 数据格式转化
    // convertData(data) {
    //   let res = [];
    //   for (let i = 0; i < data.length; i++) {
    //     let geoCoord = this.geoCoordMap[data[i].name];
    //     if (geoCoord) {
    //       res.push({
    //         name: data[i].name,
    //         value: geoCoord.concat(data[i].value),
    //       });
    //     }
    //   }
    //   return res;
    // },
    // initBaiduMap() {
    //   this.baiduMapEcharts = this.$echarts.init(this.$refs.baiduMapEcharts);
    //   this.initData();
    //   this.option = {
    //     animation: false,
    //     bmap: {
    //       center: [120.13066322374, 30.240018034923],
    //       zoom: 14,
    //       roam: true,
    //     },
    //     visualMap: {
    //       show: false,
    //       top: "top",
    //       min: 0,
    //       max: 5,
    //       seriesIndex: 0,
    //       calculable: true,
    //       inRange: {
    //         color: ["blue", "blue", "green", "yellow", "red"],
    //       },
    //     },
    //     series: [
    //       {
    //         type: "heatmap",
    //         coordinateSystem: "bmap",
    //         data: this.points,
    //         pointSize: 5,
    //         blurSize: 6,
    //       },
    //     ],
    //   };
    //   this.baiduMapEcharts.setOption(this.option);
    // },
  },
};
</script>

<style scoped lang = "scss">
.map-container {
  height: 100%;
  width: 100%;
  .baidu-map {
    width: 100%;
    height: 100%;
  }
}
</style>