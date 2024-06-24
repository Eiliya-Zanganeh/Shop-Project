<template>
  <product-slider-component :title="'محصولات پر بازدید'" :products="visitCountProducts"/>
</template>

<script>
import ProductSliderComponent from "@/components/ShopView/ProductSliderComponent.vue";
import useServerStore from "@/stores/server.js";
import {mapState} from "pinia";
import axios from "axios";

export default {
  name: "VisitCountProductsComponent",
  data() {
    return {
      visitCountProducts: []
    }
  },
  components: {ProductSliderComponent},
  methods: {
    async getVisitCountProducts() {
      await axios.get(`${this.serverDomain}/product/visit-count-products/`).then(
          response => {
            this.visitCountProducts = response.data
          }
      ).catch((error) => {
        console.log(error)
      })
    },
  },
  computed: {
    ...mapState(useServerStore, ['serverDomain']),
  },
  mounted() {
    this.getVisitCountProducts()
  }
}
</script>