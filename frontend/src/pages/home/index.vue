<template>
  <div class="home-container">
    <div class="china-map" ref="chinaMapEcharts"></div>
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      chinaMapEcharts: null,
      dataMap2: [],
    };
  },
  mounted() {
    this.initChinaMapEcharts();
  },
  methods: {
    initData() {
      // 景区数量
      this.dataMap2 = [
        {
          name: "北京",
          value: 239,
        },
        {
          name: "天津",
          value: 94,
        },
        {
          name: "上海",
          value: 113,
        },
        {
          name: "重庆",
          value: 230,
        },
        {
          name: "河北",
          value: 414,
        },
        {
          name: "河南",
          value: 357,
        },
        {
          name: "云南",
          value: 233,
        },
        {
          name: "辽宁",
          value: 340,
        },
        {
          name: "黑龙江",
          value: 411,
        },
        {
          name: "湖南",
          value: 289,
        },
        {
          name: "安徽",
          value: 563,
        },
        {
          name: "山东",
          value: 1200,
        },
        {
          name: "新疆",
          value: 351,
        },
        {
          name: "江苏",
          value: 596,
        },
        {
          name: "浙江",
          value: 572,
        },
        {
          name: "江西",
          value: 392,
        },
        {
          name: "湖北",
          value: 387,
        },
        {
          name: "广西",
          value: 469,
        },
        {
          name: "甘肃",
          value: 300,
        },
        {
          name: "山西",
          value: 165,
        },
        {
          name: "内蒙古",
          value: 331,
        },
        {
          name: "陕西",
          value: 392,
        },
        {
          name: "吉林",
          value: 74,
        },
        {
          name: "福建",
          value: 367,
        },
        {
          name: "贵州",
          value: 425,
        },
        {
          name: "广东",
          value: 200,
        },
        {
          name: "青海",
          value: 107,
        },
        {
          name: "西藏",
          value: 17,
        },
        ,
        {
          name: "四川",
          value: 441,
        },
        {
          name: "宁夏",
          value: 58,
        },
        {
          name: "海南",
          value: 56,
        },
        {
          name: "台湾",
          value: 112,
        },
        {
          name: "香港",
          value: 43,
        },
        {
          name: "澳门",
          value: 56,
        },
      ];
    },
    initChinaMapEcharts() {
      this.chinaMapEcharts = this.$echarts.init(this.$refs.chinaMapEcharts);
      let option = {
        tooltip: {
          formatter: function (params) {
            let info =
              '<p style="font-size:18px">' +
              params.name +
              '</p><p style="font-size:14px">点击显示该省份的景区数量和客流量</p>';
            return info;
          },
          backgroundColor: "rgba(15,37,110, 0.7)", //提示标签背景颜色
          textStyle: {
            color: "#fff",
          }, //提示标签字体颜色
        },
        visualMap: {
          min: 1,
          max: 900,
          text: ["High", "Low"],
          realtime: false,
          calculable: true,
          inRange: {
            color: [
              "#ffffbf",
              "#fee090",
              "#fdae61",
              "#f46d43",
              "#d73027",
              "#a50026",
            ],
          },
        },
        geo: {
          map: "china",
          roam: false, // 一定要关闭拖拽
          zoom: 1.23,
          center: [0, 0], // 调整地图位置
          label: {
            normal: {
              show: true, //关闭省份名展示
              fontSize: "10",
              color: "#FFF",
            },
            emphasis: {
              show: true,
            },
          },
        },
        series: [
          {
            type: "map",
            map: "china",
            roam: false,
            zoom: 1.23,
            center: [105, 36],
            geoIndex: 1,
            aspectScale: 0.75, //长宽比
            showLegendSymbol: false, // 存在legend时显示
            label: {
              normal: {
                show: false,
              },
              emphasis: {
                show: false,
                textStyle: {
                  color: "#fff",
                },
              },
            },
            itemStyle: {
              normal: {
                borderColor: "#0F256E",
                borderWidth: 0.5,
              },
              emphasis: {
                areaColor: "#FFDEAD",
                shadowOffsetX: 0,
                shadowOffsetY: 0,
                shadowBlur: 5,
                borderWidth: 1,
                shadowColor: "rgba(0, 0, 0, 0.5)",
              },
            },
            data: null,
          },
        ],
      };
      this.initData();
      option.series[0].data = this.dataMap2;
      this.chinaMapEcharts.setOption(option);
    },
  },
};
</script>

<style scoped lang = "scss">
.home-container {
  height: 100%;
  width: 100%;
  .china-map {
    width: 100%;
    height: 100%;
  }
}
</style>