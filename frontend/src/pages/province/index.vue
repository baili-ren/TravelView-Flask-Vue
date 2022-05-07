<template>
  <div class="province-container">
    <div class="province-container-header">
      <div>{{ provienceName.province }}</div>
      <el-button
        type="info"
        icon="el-icon-back"
        circle
        @click="goBack"
      ></el-button>
    </div>
    <div class="province-container-body">
      <!-- 5A景区 -->
      <div class="tree item-echarts" ref="treeEcharts"></div>
      <!-- 人气景区 -->
      <div
        id="categoryChart"
        class="category-chart item-echarts"
        ref="categoryChart"
      ></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Province",
  data() {
    return {
      provienceName: "省份",
      treeChart: null,
      polarBarChart: null,
      treeData: {
        name: "省份名称",
        children: [
          {
            name: "5A景区",
            children: [
              {
                name: "5A景区1",
                value: 3322,
              },
              {
                name: "5A景区2",
                value: 3322,
              },
            ],
          },
        ],
      },
      // 柱状图数据
      colSightNameData: null, //景点名称
      colSaleCountData: null, //销量
      colHeatData: null, //热度
      colScoreData: null, // 评分
      colPriceData: null, // 价格
      colcommentCountData: null, // 评论数
      pointsArr: null,
    };
  },
  mounted() {
    this.initData();
    // this.initTreeEcharts();
    // this.initPolarBarEcharts();
  },
  methods: {
    goBack() {
      this.$router.back();
    },
    initData() {
      this.provienceName = this.$router.history.current.query;
      console.log(this.$router.history, "this.$router.history==== 省份");
      const params = {
        province: this.provienceName["province"],
        sightName: "",
        star: "5A",
      };
      // 查询各省的5A景区
      this.axios.post("/api/province/5a", params).then((res) => {
        this.treeData.name = this.provienceName["province"];
        let spotsList = [];
        let pointsInfoList = [];
        res.data.data.map((item) => {
          spotsList.push({
            name: item.sightName,
            value: item.intro,
          });
          pointsInfoList.push({
            sight: item.sightName,
            lng: item.point[0],
            lat: item.point[1],
            price: item.price,
            intro: item.intro,
            saleCount: item.saleCount,
            score: item.score,
            commentCount: item.commentCount,
            address: item.address,
          });
        });
        this.pointsArr = pointsInfoList;
        this.treeData.children[0].children = spotsList;
        this.initTreeEcharts();
      });

      // 推荐景区柱状图
      const params4a = {
        province: this.provienceName["province"],
        sightName: "",
        star: "4A",
      };
      this.axios.post("/api/province/5a", params4a).then((res) => {
        let sightNameArr = [];
        let saleCountArr = [];
        let scoreArr = [];
        let priceArr = [];
        res.data.data.map((item) => {
          saleCountArr.push(item.saleCount);
          sightNameArr.push(item.sightName);
          scoreArr.push(item.score);
          priceArr.push(item.price);
        });
        this.colSightNameData = sightNameArr;
        this.colSaleCountData = saleCountArr;
        this.colScoreData = scoreArr;
        this.colPriceData = priceArr;
        this.initPolarBarEcharts();
      });
    },

    // 5A景区的树状图
    initTreeEcharts() {
      this.treeChart = this.$echarts.init(this.$refs.treeEcharts);
      this.treeChart.on("contextmenu", (params) => {
        if (params.componentType === "series") {
          this.selectedOrg = params.data;
          this.popoverPanelShow = true;
        } else {
          return;
        }
      });
      let option = {
        tooltip: {
          trigger: "item",
          triggerOn: "mousemove",
        },
        series: [
          {
            type: "tree",
            data: [this.treeData],
            top: "1%",
            left: "15%",
            bottom: "1%",
            right: "20%",

            symbolSize: 12,

            label: {
              normal: {
                position: "left",
                verticalAlign: "middle",
                align: "right",
                fontSize: 12,
              },
            },

            leaves: {
              label: {
                normal: {
                  position: "right",
                  verticalAlign: "middle",
                  align: "left",
                },
              },
            },
            expandAndCollapse: true,
            animationDuration: 550,
            animationDurationUpdate: 750,
          },
        ],
      };
      this.treeChart.setOption(option);
      const _this = this;
      // 点击景点跳转百度地图
      this.treeChart.on("click", function (params) {
        if (params.data.name && params.data.name != "5A景区") {
          // 对应景点的信息
          const spot = _this.pointsArr.find((res) => {
            return res.sight == params.data.name;
          });
          console.log(_this.pointsArr, "pointsArr---------景点的信息---");
          _this.$router.push({
            path: "/home/province/sightDetail",
            query: {
              province: _this.provienceName["province"],
              sight: params.name,
              lng: spot.lng,
              lat: spot.lat,
              points: spot,
            },
          });
          // params传参页面刷新数据丢失，可以存在localStorage中
          // _this.$router.push({
          //   name: "SightDetail",
          //   params: {
          //     test001:"999"
          //   },
          // });
        } else {
          console("无详情");
        }
      });
    },
    hidePopoverPanel() {
      this.popoverPanelShow = false;
    },

    // 人气景点
    initPolarBarEcharts() {
      this.polarBarChart = this.$echarts.init(
        document.getElementById("categoryChart")
      );
      let options = {
        title: {
          text: "推荐景点的信息对比",
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
        legend: {
          data: ["销量", "评分", "价格"],
        },
        xAxis: {
          type: "category",
          data: this.colSightNameData, //景点名称
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
            name: "销量",
            data: null, //景点数值
            type: "bar",
            showBackground: false,
            backgroundStyle: {
              color: "rgba(180, 180, 180, 0.1)",
            },
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
          {
            name: "评分",
            data: null, //景点数值
            type: "bar",
            showBackground: false,
            backgroundStyle: {
              color: "rgba(180, 180, 180, 0.1)",
            },
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
          {
            name: "价格",
            data: null, //景点数值
            type: "bar",
            showBackground: false,
            backgroundStyle: {
              color: "rgba(180, 180, 180, 0.1)",
            },
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
            xAxisIndex: [0], // 控制对应的x轴，这里表示这个dataZoom控制第一个x轴
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
            xAxisIndex: [0], // 控制对应的x轴，这里表示这个dataZoom控制第一个x轴
            startValue: 0, // 数据窗口范围的起始数值
            endValue: 10, // 数据窗口范围的结束数值
          },
        ],
      };
      options.series[0].data = this.colSaleCountData;
      options.series[1].data = this.colScoreData;
      options.series[2].data = this.colPriceData;

      this.polarBarChart.setOption(options);
    },
  },
};
</script>

<style scoped lang = "scss">
.province-container {
  height: calc(100% - 32px);
  width: calc(100% - 32px);
  padding: 16px;
  margin-bottom: 16px;
  border: 2px solid rgba(15, 37, 110, 0.3);
  border-radius: 10px;
  overflow-y: auto;
  &-header {
    height: 40px;
    line-height: 40px;
    margin: 0 16px 16px 16px;
    text-align: center;
    display: flex;
    justify-content: space-between;
    color: #0f256e;
  }
  &-body {
    width: 100%;
    height: calc(100% - 72px);
    .item-echarts {
      border: 2px solid #fff;
      border-radius: 8px;
      margin-bottom: 16px;
      background: rgba(15, 37, 110, 0.3);
    }

    .tree {
      width: calc(100% - 16px);
      height: calc(100% - 16px);
    }
    .category-chart {
      padding: 16px;
      width: calc(100% - 48px);
      height: calc(100% - 16px);
    }
  }
}
</style>