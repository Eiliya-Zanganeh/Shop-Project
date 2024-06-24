<template>
  <div id="carouselExampleFade" class="carousel slide carousel-fade" data-bs-ride="carousel">
    <div class="carousel-indicators">
      <button
          type="button"
          v-for="(banner, idx) in siteBanners" :key="banner.id"
          :data-bs-slide-to="idx"
          :class="{active:idx===0}"
          :aria-current="idx===0"
          data-bs-target="#carouselExampleFade"
      ></button>
    </div>
    <div class="carousel-inner">
      <div
          :class="[{active:idx===0}, 'carousel-item']"
          v-for="(banner, idx) in siteBanners"
          :key="banner.id"
          data-bs-interval="10000"
      >
        <img :src="`${serverDomain}/${banner.image}`" class="d-block w-100" alt="..."
             style="height: 400px; object-fit: cover;">
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade"
            data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade"
            data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
</template>

<script>
import useServerStore from '@/stores/server.js'
import {mapState} from "pinia";

export default {
  name: "HeroComponent",
  computed: {
    ...mapState(useServerStore, ['serverDomain', 'siteName', 'siteDescription', 'siteBanners'])
  }
}
</script>

<style>
.image-enter-from {
  opacity: 0;
}

.image-enter-active {
  transition: all 1s linear;
  animation: zoom-in 1s linear forwards;
}

@keyframes zoom-in {
  from {
    transform: scale(0, 0);
  }
  to {
    transform: scale(1, 1);
  }
}
</style>


