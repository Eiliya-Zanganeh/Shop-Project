<template>
  <product-slider-component :title="'محصولات ویژه'" :products="popularProducts">
    <swiper-slide>
      <router-link class="p-0 d-flex justify-content-center align-items-center flex-column" :to="{name: 'special_products'}">
        <br><br><br>
        <button class="btn btn-outline-danger text-center p-0 w-50">
          <br>
          <i style="font-size: 5vh;"
             class="bi bi-arrow-left"></i>
        </button>
      </router-link>
    </swiper-slide>
  </product-slider-component>
</template>

<script>
import ProductSliderComponent from "@/components/ShopView/ProductSliderComponent.vue";
import useServerStore from "@/stores/server.js";
import {mapState} from "pinia";
import axios from "axios";
import {SwiperSlide} from "swiper/vue";

export default {
  name: "PopularProductsComponent",
  data() {
    return {
      popularProducts: []
    }
  },
  components: {SwiperSlide, ProductSliderComponent},
  methods: {
    async getPopularProducts() {
      await axios.get(`${this.serverDomain}/product/popular-products/`).then(
          response => {
            this.popularProducts = response.data
          }).catch(error => {
        console.log(error)
      })
    }
  },
  computed: {
    ...mapState(useServerStore, ['serverDomain']),
  },
  mounted() {
    this.getPopularProducts()
  }
}
</script>