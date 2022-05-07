<template>
  <div class="whole-china-container">
    <!-- 各省的4A和5A景区数量 -->
    <div id="columnAChart" class="column-a-chart item-echarts"></div>
    <!-- 全国热门景点 -->
    <div id="columnsTopHotChart" class="item-echarts"></div>
    <!-- 景点评分与价格,热度 -->
    <div class="item-echarts sight-score">
      <div id="scorePriceChart" class="score-price"></div>
      <div id="scoreHotChart" class="score-hot"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "WholeChina",
  data() {
    return {
      acolumnData: [], //4a5a数值数组
      aprovince: [], // 4A5A对应省份名称
      topHotValueData: [], //热门景区热度值
      topHotSightNameData: [], //热门景区名字
      scorePriceData: [],
      scoreHotData: [],
    };
  },
  mounted() {
    this.initData();
  },
  methods: {
    initData() {
      const province = [
        "上海",
        "云南",
        "内蒙古",
        "北京",
        "吉林",
        "四川",
        "天津",
        "宁夏",
        "安徽",
        "山东",
        "山西",
        "广东",
        "广西",
        "新疆",
        "江苏",
        "江西",
        "河北",
        "河南",
        "浙江",
        "海南",
        "湖北",
        "湖南",
        "甘肃",
        "福建",
        "西藏",
        "贵州",
        "辽宁",
        "重庆",
        "陕西",
        "青海",
        "黑龙江",
      ];
      //   4a5a景区数量
      this.axios.get("/api/province/4a5aCount").then((res) => {
        const data = res.data.data;
        let columnAArr = []; // 各省4A5A景点数量
        let provinceNameArr = [];
        province.map((item) => {
          columnAArr.push(data[item]);
          provinceNameArr.push(item);
        });
        this.acolumnData = columnAArr;
        this.aprovince = provinceNameArr;
        this.initColumnAChart();
      });
      //   全国热门景点热度
      this.axios.get("/api/sight/heat", {}).then((res) => {
        const data = res.data.data.slice(0, 40);
        let hotValueArr = [];
        let sightNameArr = [];
        data.map((item) => {
          hotValueArr.push(item.value);
          sightNameArr.push(item.name);
        });
        this.topHotSightNameData = sightNameArr;
        this.topHotValueData = hotValueArr;
        this.initColumnsTopHotChart();
      });
      // 景点评分和价格
      this.axios.get("/api/sight/scorePrice").then((res) => {
        const data = res.data.data;
        let arr = [];
        arr = data.find((res) => {
          return res.value < "500";
        });
        this.scorePriceData = data.slice(0, 200);
        console.log(this.scorePriceData, "this.scorePriceData------------");
        this.initscorePriceChart();
      });

      // 景点评分和热度
      this.axios.get("/api/sight/scoreHeat").then((res) => {
        const data = res.data.data;
        this.scoreHotData = data.slice(1, 200);
        console.log(this.scoreHotData, "this.scoreHotData----------------");
        this.initscoreHotChart();
      });
    },
    // 4A5A景区各省的个数柱状图
    initColumnAChart() {
      let columnchart = this.$echarts.init(
        document.getElementById("columnAChart")
      );
      let options = {
        title: {
          text: "各省4A5A景点数量",
          textAlign: "left",
          textStyle: {
            color: "#696969",
            fontWeight: "500",
            fontSize: 16,
          },
        },
        toolbox: {
          feature: {
            magicType: { type: ["line", "bar"] }, //图表类型切换
          },
        },
        xAxis: {
          type: "category",
          data: null,
          axisLabel: {
            interval: 0, //横轴信息全部显示
            rotate: -15, //-15度角倾斜显示
          },
        },
        yAxis: {
          type: "value",
        },
        series: [
          {
            data: null,
            type: "bar",
            itemStyle: {
              normal: {
                label: {
                  show: true, //开启显示
                  position: "top", //在上方显示
                  textStyle: {
                    //数值样式
                    color: "black",
                    fontSize: 16,
                  },
                },
              },
            },
          },
        ],
        dataZoom: [
          // dataZoom组件 用于区域缩放
          {
            type: "slider",
            show: true,
            yAxisIndex: [0], // 控制对应的x轴，这里表示这个dataZoom控制第一个x轴
            height: 8,
            borderColor: "#ADD8E6",
            fillerColor: "#ADD8E6", // 滑块颜色
            bottom: "5px", // 滚动条距离页面底部的距离
            startValue: 0, // 数据窗口范围的起始数值
            endValue: 10, // 数据窗口范围的结束数值
            showDataShadow: false,
            showDetail: false,
          },
          {
            type: "inside",
            yAxisIndex: [0], // 控制对应的x轴，这里表示这个dataZoom控制第一个x轴
            startValue: 0, // 数据窗口范围的起始数值
            endValue: 10, // 数据窗口范围的结束数值
          },
        ],
      };
      options.xAxis.data = this.aprovince;
      options.series[0].data = this.acolumnData;
      columnchart.setOption(options);
    },
    // 全国推荐景区柱状图
    initColumnsTopHotChart() {
      let columnTopHotchart = this.$echarts.init(
        document.getElementById("columnsTopHotChart")
      );
      let options = {
        title: {
          text: "全国热门景点热度",
          textAlign: "left",
          textStyle: {
            color: "#696969",
            fontWeight: "500",
            fontSize: 16,
          },
        },
        toolbox: {
          feature: {
            magicType: { type: ["line", "bar"] }, //图表类型切换
          },
        },
        xAxis: {
          type: "value",
        },
        yAxis: {
          type: "category",
          data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
          axisLabel: {
            interval: 0, //横轴信息全部显示
            rotate: -15, //-15度角倾斜显示
          },
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true,
        },
        legend: {
          data: ["热度"],
        },
        series: [
          {
            name: "热度",
            data: [120, 200, 150, 80, 70, 110, 130],
            type: "bar",
            itemStyle: {
              normal: {
                label: {
                  show: true, //开启显示
                  position: "right", //在上方显示
                  textStyle: {
                    //数值样式
                    color: "black",
                    fontSize: 16,
                  },
                },
              },
            },
          },
        ],
        dataZoom: [
          // dataZoom组件 用于区域缩放
          {
            type: "slider",
            show: true,
            yAxisIndex: [0], // 控制对应的x轴，这里表示这个dataZoom控制第一个x轴
            height: 8,
            borderColor: "#ADD8E6",
            fillerColor: "#ADD8E6", // 滑块颜色
            bottom: "5px", // 滚动条距离页面底部的距离
            startValue: 0, // 数据窗口范围的起始数值
            endValue: 10, // 数据窗口范围的结束数值
            showDataShadow: false,
            showDetail: false,
          },
          {
            type: "inside",
            yAxisIndex: [0], // 控制对应的x轴，这里表示这个dataZoom控制第一个x轴
            startValue: 0, // 数据窗口范围的起始数值
            endValue: 10, // 数据窗口范围的结束数值
          },
        ],
      };
      options.yAxis.data = this.topHotSightNameData.reverse();
      options.series[0].data = this.topHotValueData.reverse();
      columnTopHotchart.setOption(options);
    },
    // 评分和价格的关系
    initscorePriceChart() {
      let scorePriceChart = this.$echarts.init(
        document.getElementById("scorePriceChart")
      );
      let options = {
        title: {
          text: "景点评分和价格的关系",
          textAlign: "left",
          textStyle: {
            color: "#696969",
            fontWeight: "500",
            fontSize: 16,
          },
        },
        xAxis: {
          name: "评分",
          min: 3,
          max: 5,
        },
        yAxis: {
          name: "价格",
          max: 1000,
        },
        series: [
          {
            symbolSize: 20,
            data: [],
            type: "scatter",
          },
        ],
      };
      options.series[0].data = this.scorePriceData;
      scorePriceChart.setOption(options);
    },
    initscoreHotChart() {
      let scoreHotChart = this.$echarts.init(
        document.getElementById("scoreHotChart")
      );
      let options = {
        title: {
          text: "景点评分和热度的关系",
          textAlign: "left",
          textStyle: {
            color: "#696969",
            fontWeight: "500",
            fontSize: 16,
          },
        },
        xAxis: {
          name: "评分",
          min: 3,
          max: 5,
        },
        yAxis: {
          name: "热度",
        },
        series: [
          {
            symbolSize: 20,
            data: [],
            type: "scatter",
          },
        ],
      };
      options.series[0].data = this.scoreHotData;
      scoreHotChart.setOption(options);
    },
  },
};
</script>


<style scoped lang="scss">
.whole-china-container {
  height: calc(100% - 32px);
  width: calc(100% - 32px);
  padding: 16px;
  border: 2px solid rgba(15, 37, 110, 0.3);
  border-radius: 8px;
  overflow-y: auto;
  .column-a-chart {
    height: calc(100% - 32px);
    width: calc(100% - 32px);
    height: 100%;
  }
  .item-echarts {
    width: calc(100% - 16px);
    height: 100%;
    border: 2px solid #fff;
    border-radius: 8px;
    margin-bottom: 16px;
    background: rgba(15, 37, 110, 0.3);
  }
  .sight-score {
    display: flex;
  }
  .score-price {
    width: calc(50% - 32px);
    height: calc(100% - 32px);
    margin: 16px;
    border: 1px #fff solid;
    border-radius: 8px;
  }
  .score-hot {
    width: calc(50% - 32px);
    height: calc(100% - 32px);
    margin: 16px;
    border: 1px #fff solid;
    border-radius: 8px;
  }
}
</style>


