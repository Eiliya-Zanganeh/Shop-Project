<template>
  <div class="hero">
    <div class="container">
      <div class="row justify-content-between">
        <div class="col-lg-6">
          <div class="intro-excerpt">
            <h1 class="text-right"><span class="d-block">» {{ siteName }}</span></h1>
            <p class="mb-4 text-right">{{ siteDescription }}</p>
            <p><a href="" class="btn btn-secondary m-2">خدمات</a><a href="#" class="btn btn-white-outline text-light">محصولات</a>
            </p>
          </div>
        </div>
        <div class="col-lg-6">
          <div class="hero-img-wrap"></div>
          <transition name="image" appear>
            <img style="width: 100%; height: auto" :src="`${serverDomain}/${descriptionImg}`">
          </transition>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import useServerStore from '@/stores/server.js'
import {mapState} from "pinia";

export default {
  name: "HeroComponent",
  computed: {
    ...mapState(useServerStore, ['serverDomain', 'siteName', 'siteDescription', 'descriptionImg'])
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