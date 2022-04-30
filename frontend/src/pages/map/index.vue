<template>
  <!-- 调用接口 -->
  <div class="map-container">
    <div class="action"><el-button type="primary" icon="el-icon-s-flag" circle @click="closeLabel"></el-button></div>
    <div id="baiduMap" class="baidu-map" ref="baiduMapEcharts"></div>
  </div>
</template>

<script>
import "echarts/extension/bmap/bmap";
import dataJSON from "../../assets/json/data.json";
import geoCoordMapJSON from "../../assets/json/geoCoordMap.json";
// import Scene from "../../assets/json/Scene.json"
export default {
  name: "Map",
  data() {
    return {
      baiduMapEcharts: null,
      data: [],
      geoCoordMap: {},
      option: {},
      showLabel: false,
    };
  },
  mounted() {
    this.initBaiduMap();
  },
  methods: {
    // 初始化数据
    initData() {
      this.data = dataJSON;
      this.geoCoordMap = geoCoordMapJSON;
    },
    // 数据格式转化
    convertData(data) {
      let res = [];
      for (let i = 0; i < data.length; i++) {
        let geoCoord = this.geoCoordMap[data[i].name];
        if (geoCoord) {
          res.push({
            name: data[i].name,
            value: geoCoord.concat(data[i].value),
          });
        }
      }
      return res;
    },
    initBaiduMap() {
      this.baiduMapEcharts = this.$echarts.init(this.$refs.baiduMapEcharts);
      this.initData();
      this.option = {
        title: {
          text: "中国旅游数据",
          left: "center",
        },
        tooltip: {
          // trigger: "item",
          formatter: function (params) {
            let info =
              '<p style="font-size:18px">' +
              params.name
              '</p><p style="font-size:14px"></p>';
              console.log(params,999)
            return info;
          },
          backgroundColor: "rgba(15,37,110, 0.7)", //提示标签背景颜色
          textStyle: {
            color: "#fff",
          }, //提示标签字体颜色
        },
        bmap: {
          center: [104.114129, 37.550339],
          zoom: 5,
          roam: true,
          mapStyle: {
            styleJson: [
              {
                featureType: "water",
                elementType: "all",
                stylers: {
                  color: "#d1d1d1",
                },
              },
              {
                featureType: "land",
                elementType: "all",
                stylers: {
                  color: "#f3f3f3",
                },
              },
              {
                featureType: "railway",
                elementType: "all",
                stylers: {
                  visibility: "off",
                },
              },
              {
                featureType: "highway",
                elementType: "all",
                stylers: {
                  color: "#fdfdfd",
                },
              },
              {
                featureType: "highway",
                elementType: "labels",
                stylers: {
                  visibility: "off",
                },
              },
              {
                featureType: "arterial",
                elementType: "geometry",
                stylers: {
                  color: "#fefefe",
                },
              },
              {
                featureType: "arterial",
                elementType: "geometry.fill",
                stylers: {
                  color: "#fefefe",
                },
              },
              {
                featureType: "poi",
                elementType: "all",
                stylers: {
                  visibility: "off",
                },
              },
              {
                featureType: "green",
                elementType: "all",
                stylers: {
                  visibility: "off",
                },
              },
              {
                featureType: "subway",
                elementType: "all",
                stylers: {
                  visibility: "off",
                },
              },
              {
                featureType: "manmade",
                elementType: "all",
                stylers: {
                  color: "#d1d1d1",
                },
              },
              {
                featureType: "local",
                elementType: "all",
                stylers: {
                  color: "#d1d1d1",
                },
              },
              {
                featureType: "arterial",
                elementType: "labels",
                stylers: {
                  visibility: "off",
                },
              },
              {
                featureType: "boundary",
                elementType: "all",
                stylers: {
                  color: "#fefefe",
                },
              },
              {
                featureType: "building",
                elementType: "all",
                stylers: {
                  color: "#d1d1d1",
                },
              },
              {
                featureType: "label",
                elementType: "labels.text.fill",
                stylers: {
                  color: "#999999",
                },
              },
            ],
          },
        },
        series: [
          {
            name: "景区名称",
            type: "scatter",
            coordinateSystem: "bmap",
            data: this.convertData(this.data),
            symbolSize: function (val) {
              return val[2] / 10;
            },
            encode: {
              value: 200,
            },
            label: {
              formatter: "{b}",
              position: "right",
              show: this.showLabel,
            },
            emphasis: {
              label: {
                show: true,
              },
            },
          },
          {
            name: "景区名称",
            type: "effectScatter",
            coordinateSystem: "bmap",
            data: this.convertData(
              this.data
                .sort(function (a, b) {
                  return b.value - a.value;
                })
                .slice(0, 6)
            ),
            symbolSize: function (val) {
              return val[2] / 10;
            },
            encode: {
              value: 2,
            },
            showEffectOn: "render",
            rippleEffect: {
              brushType: "stroke",
            },

            // 是否显示景点名称
            label: {
              formatter: "{b}",
              position: "right",
              show: true,
            },
            itemStyle: {
              shadowBlur: 10,
              shadowColor: "#333",
            },
            emphasis: {
              scale: true,
            },
            zlevel: 1,
          },
        ],
      };
      this.baiduMapEcharts.setOption(this.option);
    },
    closeLabel() {
      this.showLabel = !this.showLabel
      this.initBaiduMap()
    }
  },
};
</script>

<style scoped lang = "scss">
.map-container {
  position: relative;
  height: 100%;
  width: 100%;
  .baidu-map {
    width: 100%;
    height: 100%;
  }
  .action{
    position: absolute;
    top: 16px;
    left: 16px;
    z-index: 2;
  }
}
</style>