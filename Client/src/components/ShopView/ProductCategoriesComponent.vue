<template>
  <div class="untree_co-section product-section before-footer-section">
    <div class="container-fluid">
      <h1 class="text-center mb-4">دسته بندی محصولات</h1>
      <swiper
          :breakpoints="{
          100: {
            slidesPerView: 3,
            spaceBetween: 0
          },
          750: {
            slidesPerView: 4,
            spaceBetween: 0
          },
          1000: {
            slidesPerView: 6,
            spaceBetween: 0
          },
          1200: {
            slidesPerView: 8,
            spaceBetween: 0
          }
        }"
          navigation
          :pagination="{ clickable: true }"
          class="pt-5 ps-5 pe5 p-3"
      >
        <swiper-slide
            v-for="(category) in productCategories"
            :key="category"
        >
          <router-link class="product-item p-0" :to="{name: 'shop-category', params: {category: category.id}}">
            <img :src="`${serverDomain}/${category.image}`"
                 class="img-fluid product-thumbnail">
            <h3 class="product-title">{{ category.name }}</h3>
            <span class="icon-cross">
                <img style="background-color: #9ab7a7; border-radius: 30px" src="/home/images/bag.svg"
                     class="img-fluid">
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
import useServerStore from '@/stores/server.js'
import {mapState} from "pinia"
import {Swiper, SwiperSlide} from 'swiper/vue';
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/scrollbar';
import axios from "axios";


export default {
  name:"ProductCategoriesComponent",
  data(){
    return{
      productCategories: [],
    }
  },
  components: {
    Swiper,
    SwiperSlide,
  },
  computed: {
    ...mapState(useServerStore, ['serverDomain']),
  },
  methods:{
    async getProductCategoreis() {
      await axios.get(`${this.serverDomain}/product/product-categories/`).then(
          response => {
            this.productCategories = response.data
          }).catch(error => {
        console.log(error)
      })
    },
  },
  mounted() {
    this.getProductCategoreis()
  }
}
</script>