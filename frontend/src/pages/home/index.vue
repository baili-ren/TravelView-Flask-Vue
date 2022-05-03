<template>
  <div class="home-container">
    <div class="title">中国各省份旅游数据分析</div>
    <div id="chinaMap" class="china-map" ref="chinaMapEcharts"></div>
    <div class="btns">
      <el-button type="info" @click="showHotMap">热门程度</el-button>
      <el-button type="info" @click="showNumMap">景区数量</el-button>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      chinaMapEcharts: null,
      dataMapHeat: [],
      dataMapCount: [],
      showHot: true, //默认展示热门程度
    };
  },
  mounted() {
    this.initData();
    // this.initChinaMapEcharts();
    console.log(this.$router, "this.$router===, 地图页面挂载时");
  },
  methods: {
    // 各省旅游热度地图
    showHotMap() {
      this.showHot = true;
      this.initChinaMapEcharts();
    },
    // 各省景点数量地图
    showNumMap() {
      this.showHot = false;
      this.initChinaMapEcharts();
    },
    initData() {
      // 全国省份列表   万人次
      this.dataMapHeat = [
        { name: "北京", value: 376.9 },
        { name: "天津", value: 50.76 },
        { name: "上海", value: 599.16 },
        { name: "重庆", value: 169.72 },
        { name: "河北", value: 73.56 },
        { name: "河南", value: 113.76 },
        { name: "云南", value: 586.5 },
        { name: "辽宁", value: 236.93 },
        { name: "黑龙江", value: 99.29 },
        { name: "湖南", value: 250.14 },
        { name: "安徽", value: 210.74 },
        { name: "山东", value: 294.41 },
        { name: "新疆", value: 25.78 },
        { name: "江苏", value: 266.46 },
        { name: "浙江", value: 329.83 },
        { name: "江西", value: 61.14 },
        { name: "湖北", value: 349.94 },
        { name: "广西", value: 294.8 },
        { name: "甘肃", value: 11.37 },
        { name: "山西", value: 49.8 },
        { name: "内蒙古", value: 186.56 },
        { name: "陕西", value: 329.61 },
        { name: "吉林", value: 121.11 },
        { name: "福建", value: 239.98 },
        { name: "贵州", value: 23.5 },
        { name: "广东", value: 856.96 },
        { name: "青海", value: 4.7 },
        { name: "西藏", value: 36.91 },
        { name: "四川", value: 313.09 },
        { name: "宁夏", value: 3.61 },
        { name: "海南", value: 107.91 },
        { name: "台湾", value: 56.34 },
        { name: "香港", value: 57.34 },
        { name: "澳门", value: 67.34 },
      ];
      // 景区数量
      this.dataMapCount = [
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
          value: 220,
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

      // 查询各省的热度与景点数
      this.axios.get("/api/province/info").then((res) => {
        const data = res.data.data
        let arrCount = []
        let arrHeat = []
        data.map(item => {
          arrCount.push({
            name: item.provinceName,
            value: item.count,
          })
          arrHeat.push({
            name: item.provinceName,
            value: item.heat
          })
        })
        this.dataMapHeat = arrHeat
        this.dataMapCount =arrCount
        this.initChinaMapEcharts()
      });
    },
    initChinaMapEcharts() {
      this.chinaMapEcharts = this.$echarts.init(this.$refs.chinaMapEcharts);
      let label = "热度"
      if(this.showHot){
        label = "热度"
      }else{
        label="景区数"
      }
      let option = {
        tooltip: {
          formatter: function (params) {
            let info =
              '<p style="font-size:18px">' +
              params.name+ ":" + params.value +`${label}`+
              '</p><p style="font-size:14px">点击显示该省份的旅游信息详情</p>';
            return info;
          },
          backgroundColor: "rgba(15,37,110, 0.7)", //提示标签背景颜色
          textStyle: {
            color: "#fff",
          }, //提示标签字体颜色
        },
        visualMap: {
          min: 1,
          max: 100000,
          text: ["最热门", "最冷门"],
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
      if (this.showHot) {
        option.series[0].data = this.dataMapHeat;
        option.visualMap.max=100000
        option.visualMap.text=["最热门", "最冷门"]

      } else {
        option.series[0].data = this.dataMapCount;
        option.visualMap.max=10000
        option.visualMap.text=["最多景点", "最少景点"]
      }
      this.chinaMapEcharts.setOption(option);

      const _this = this;
      this.chinaMapEcharts.on("click", function (params) {
        if (params.data.name) {
          _this.$router.push({
            path: "/home/province",
            query: { province: params.name },
          });
        } else {
          alert("该省份无数据");
        }
        console.log(_this.$router, "_this.$router  ，点击省份");
      });
    },
  },
};
</script>

<style scoped lang = "scss">
.home-container {
  height: calc(100% - 32px);
  width: calc(100% - 32px);
  padding: 16px;
  background: rgba(15, 37, 110, 0.7);
  border-radius: 10px;
  .title {
    color: #fff;
  }
  .china-map {
    width: calc(100% - 16px);
    height: calc(100% - 16px);
  }
  .btns {
    position: absolute;
    display: flex;
    /* flex-flow: column; */
    bottom: 100px;
    right: 100px;
    .el-button {
      border-radius: 50px;
    }
  }
}
</style>