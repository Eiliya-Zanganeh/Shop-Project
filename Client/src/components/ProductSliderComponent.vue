<template>
  <div class="product-section">
    <div class="container">
      <h1 class="text-center mb-4">{{ title }}</h1>
      <swiper
          :breakpoints="{
          100: {
            slidesPerView: 2,
            spaceBetween: 0
          },
          750: {
            slidesPerView: 2,
            spaceBetween: 0
          },
          1000: {
            slidesPerView: 4,
            spaceBetween: 0
          },
          1200: {
            slidesPerView: 6,
            spaceBetween: 0
          }
          }"
          navigation
          :pagination="{ clickable: true }"
          class="pt-5 ps-5 pe5 pb-3"
      >
        <swiper-slide
            v-for="(product) in products"
            :key="product"
        >
          <router-link class="product-item p-0" :to="{name: 'detail-product', params: {product: product.id}}">
            <img :src="`${serverDomain}/${product.image}`" class="img-fluid product-thumbnail">
            <h6 style="max-height: 40px; overflow-y: hidden; text-overflow: ellipsis;">{{ product.name }}</h6>
            <h5 class="product-price">{{ Number(product.price).toLocaleString('fa-IR') }} تومان</h5>

            <span class="icon-cross">
								<img src="/public/home/images/cross.svg" class="img-fluid">
							</span>
          </router-link>
        </swiper-slide>
      </swiper>
    </div>
  </div>
</template>

<script>
import {Swiper, SwiperSlide} from 'swiper/vue';
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/scrollbar';
import {mapState} from "pinia";
import useServerStore from "@/stores/server.js";

export default {
  name: "ProductSliderComponent",
  props: ['title', 'products'],
  computed: {
    ...mapState(useServerStore, ['serverDomain']),
  },
  components: {
    Swiper,
    SwiperSlide,
  }
}
</script>
