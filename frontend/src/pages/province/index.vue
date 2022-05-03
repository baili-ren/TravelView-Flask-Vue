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
      <!-- <div class="polar-bar item-echarts" ref="polarBarEcharts"></div> -->
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
      dataXJ_JD: [
        "库尔勒体育公园",
        "天山天池",
        "天山大峡谷",
        "赛里木湖",
        "那拉提旅游风景区",
        "中华福寿山",
        "喀纳斯景区",
        "天山野生动物园",
        "乌尔禾魔鬼城",
        "温宿大峡谷",
        "定海神针",
        "火焰山景区",
        "马牙山",
        "独山子大峡谷",
        "南山牧场",
      ],
      dataXJ_Num: [676, 76, 34, 34, 20, 20, 26, 16, 14, 28, 4, 6, 6, 16, 6],
    };
  },
  mounted() {
    this.initData();
    // this.initTreeEcharts();
    this.initPolarBarEcharts();
  },
  methods: {
    initData() {
      this.provienceName = this.$router.history.current.query;
      console.log(this.$router.history, "this.$router.history==== 省份页面");
      const params = {
        province: this.provienceName["province"],
      };
      // this.axios.post("/api/province/5a", params).then((res) => {
      //   console.log(res, "res===");
      //   this.treeData.name = this.provienceName["province"];
      //   let spotsList = [];
      //   res.data.data.map((item) => {
      //     spotsList.push({
      //       name: item.Scenic5AName,
      //       value: item.id,
      //     });
      //   });
      //   this.treeData.children[0].children = spotsList;
      //   this.initTreeEcharts();
      // });
      console.log(this.treeData, "this.treeData======");
    },
    goBack() {
      this.$router.back();
    },

    // 5A景区的树状图
    initTreeEcharts() {
      this.treeChart = this.$echarts.init(this.$refs.treeEcharts);
      this.treeChart.on("contextmenu", (params) => {
        console.log(params);
        if (params.componentType === "series") {
          this.selectedOrg = params.data;
          this.popoverPanelShow = true;
        } else {
          return;
        }
      });
      this.treeChart.setOption({
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
						text: '推荐景点',

						textAlign:'center'
					},
        xAxis: {
          type: "category",
          data: this.dataXJ_JD,
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
            data: this.dataXJ_Num,
            type: "bar",
            showBackground: true,
            backgroundStyle: {
              color: "rgba(180, 180, 180, 0.2)",
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
      };
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
      width: calc(100% - 16px);
      height: calc(100% - 16px);
    }
  }
}
</style>