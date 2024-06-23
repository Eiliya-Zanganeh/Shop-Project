<template>
  <div class="hero">
    <div class="container">
      <div class="row justify-content-between">
        <h1 class="text-center">محصولات</h1>
      </div>
    </div>
  </div>


  <product-categorys-component/>

  <product-slider-component :title="'محصولات ویژه'" :products="popularProducts"/>

  <product-slider-component :title="'محصولات پرفروش'" :products="buyCountProducts"/>

  <product-slider-component :title="'جدید ترین محصولات'" :products="newProducts"/>

  <product-slider-component :title="'محصولات پر بازدید'" :products="visitCountProducts"/>

</template>

<script>
import ProductCategorysComponent from "@/components/HomeView/ProductCategorysComponent.vue";
import {mapActions, mapState} from "pinia";
import useServerStore from "@/stores/server.js";
import ProductSliderComponent from "@/components/ProductSliderComponent.vue";

export default {
  name: "ShopView",
  components: {ProductSliderComponent, ProductCategorysComponent},
  methods: {
    ...mapActions(useServerStore, [
      'getPopularProducts',
      'getVisitCountProducts',
      'getProductCategorys',
      'getNewProducts',
      'getBuyCountProducts'
    ]),
  },
  computed: {
    ...mapState(useServerStore, ['popularProducts', 'buyCountProducts', 'newProducts', 'visitCountProducts']),
  },
  mounted() {
    this.getProductCategorys()
    this.getPopularProducts()
    this.getNewProducts()
    this.getBuyCountProducts()
    this.getVisitCountProducts()
  }
}
</script>