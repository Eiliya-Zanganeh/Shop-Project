<template>
  <div class="product-section">
    <div class="container-fluid">
      <h1 class="text-center">{{ title }}</h1>
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
          class="pt-5 pb-3"
      >
        <swiper-slide
            v-for="(product) in products"
            :key="product"
        >
          <router-link class="product-item p-0" :to="{name: 'detail-product', params: {product: product.id}}">
            <div class="position-relative">
              <img :src="`${serverDomain}/${product.image}`"
                   class="img-fluid product-thumbnail rounded-3">
              <span
                  v-if="product.offer_price"
                  style="left: 18%; top:3%; border-radius: 10%; width: 20%"
                  class="position-absolute bg-danger text-light"
              >{{ product.offer }}%</span>
            </div>
            <h6 style="height:40px;max-height: 40px; overflow-y: hidden; text-overflow: ellipsis;">{{
                product.name
              }}</h6>
            <h5
                class="product-price text-center"
                v-if="product.offer_price"
            >{{ Number(product.offer_price).toLocaleString('fa-IR') }}
              تومان</h5>
            <h5 :class="[{'product-price': !product.offer_price, 'offer':product.offer_price }]">
              {{ Number(product.price).toLocaleString('fa-IR') }} تومان</h5>
            <h5 v-if="!product.offer_price"><br></h5>
            <span class="icon-cross">
								<img src="/home/images/cross.svg" class="img-fluid">
							</span>
          </router-link>
        </swiper-slide>
        <slot/>
      </swiper>
    </div>
  </div>
  <hr>
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

<style>
.offer {
  opacity: 50%;
  font-size: 18px;
  text-decoration: line-through;
  text-align: center;
}
</style>
