<template>
  <div class="sight-detail-container">
    <baidu-map
      class="map"
      :center="{ lng: spotLng, lat: spotLat }"
      :zoom="15"
      :scroll-wheel-zoom="true"
      style="
        height: calc(100% - 92px);
        width: calc(100% - 96px);
        position: absolute;
      "
    >
      <bm-marker
        :position="{ lng: spotLng, lat: spotLat }"
        :dragging="true"
        animation="BMAP_ANIMATION_BOUNCE"
        @click="infoWindowOpen"
      >
        <bm-label
          :content="spotName"
          :labelStyle="{ color: '#483D8B', fontSize: '16px' }"
          :offset="{ width: -35, height: 30 }"
        />
        <bm-info-window
          :show="show"
          @close="infoWindowClose"
          @open="infoWindowOpen"
        >
          <el-card class="box-card">
            <div class="text item">
              {{ "景点名称: " + spotObj.sight }}
            </div>
            <div class="text item">
              {{ "景点地址:" + spotObj.address }}
            </div>
            <div class="text item">
              {{ "景点票价: " + spotObj.price }}
            </div>
            <div class="text item">
              {{ "景点销售额: " + spotObj.saleCount }}
            </div>
            <div class="text item">
              {{ "景点评分: " + spotObj.score }}
            </div>
            <div class="text item">
              {{ "景点简介: " + spotObj.intro }}
            </div>
          </el-card>
        </bm-info-window>
      </bm-marker>
    </baidu-map>
    <el-button
      style="position: absolute; right: 32px; top: 92px"
      type="info"
      icon="el-icon-back"
      circle
      @click="goBack"
    ></el-button>
  </div>
</template>

<script>
export default {
  name: "SightDetail",
  components: {},
  data() {
    return {
      show: false,
      spotName: "景区",
      spotLng: 116.404,
      spotLat: 39.915,
      spotObj: {
        address: "景点地址",
        commentCount: 4509,
        intro: "景点简介",
        lat: "39.915",
        lng: "116.404",
        price: 10,
        saleCount: 30,
        score: 4.8,
        sight: "景点名称",
      },
    };
  },
  created() {
    const query = this.$route.query;
    console.log(this.$route, "this.$route-----------");
    this.spotLng = query.lng;
    this.spotLat = query.lat;
    this.spotName = query.sight;
    this.spotObj = query.points;
  },
  mounted() {},
  methods: {
    infoWindowClose() {
      this.show = false;
    },
    infoWindowOpen() {
      this.show = true;
    },
    goBack() {
      this.$router.back();
    },
  },
};
</script>

<style scoped lang="scss">
sight-detail-container {
  position: relative;
  height: calc(100% - 32px);
  width: calc(100% - 32px);
  .box-card {
    .text {
      font-size: 14px;
    }
    .item {
      padding: 18px 0;
    }
    .box-card {
      width: 480px;
    }
  }
}
</style>
