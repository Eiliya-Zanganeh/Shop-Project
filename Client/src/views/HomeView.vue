<template>

  <hero-component/>
  <product-categories-component>
    <swiper-slide>
      <router-link class="p-0 d-flex justify-content-center align-items-center flex-column" :to="{name: 'shop'}">
        <br>
        <button class="btn btn-outline-danger text-center p-0 w-50">
          <br>
          <i style="font-size: 5vh;"
             class="bi bi-arrow-left"></i>
        </button>
      </router-link>
    </swiper-slide>
  </product-categories-component>
  <popular-products-component/>

</template>

<script>
import HeroComponent from "@/components/HomeView/HeroComponent.vue";
import ProductCategoriesComponent from "@/components/ShopView/ProductCategoriesComponent.vue";
import PopularProductsComponent from "@/components/ShopView/PopularProductsComponent.vue";
import {SwiperSlide} from "swiper/vue";

export default {
  name: "HomeView",
  components: {
    SwiperSlide,
    PopularProductsComponent,
    ProductCategoriesComponent,
    HeroComponent
  }
}
</script>

<style>
@import "@/assets/home/css/bootstrap.min.css";
@import "@/assets/home/css/tiny-slider.css";
@import "@/assets/home/css/style.css";
@import 'bootstrap-icons/font/bootstrap-icons.css';
</style>

