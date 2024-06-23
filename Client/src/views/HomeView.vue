<template>

  <hero-component/>

  <product-categorys-component/>

  <product-slider-component :title="'محصولات ویژه'" :products="popularProducts"/>

</template>

<script>
import HeroComponent from "@/components/HomeView/HeroComponent.vue";
import {mapActions, mapState} from "pinia";
import useServerStore from "@/stores/server.js";
import ProductCategorysComponent from "@/components/HomeView/ProductCategorysComponent.vue";
import ProductSliderComponent from "@/components/ProductSliderComponent.vue";

export default {
  name: "HomeView",
  components: {
    ProductSliderComponent,
    ProductCategorysComponent,
    HeroComponent
  },
  methods: {
    ...mapActions(useServerStore, ['getPopularProducts', 'getProductCategorys']),
  },
  computed: {
    ...mapState(useServerStore, ['popularProducts']),
  },
  mounted() {
    this.getPopularProducts()
    this.getProductCategorys()
  }
}
</script>

<style>
@import "@/assets/home/css/bootstrap.min.css";
@import "@/assets/home/css/font-awesome.css";
@import "@/assets/home/css/tiny-slider.css";
@import "@/assets/home/css/style.css";
@import 'bootstrap-icons/font/bootstrap-icons.css';
</style>

