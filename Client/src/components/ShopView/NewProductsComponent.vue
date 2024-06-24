<template>
  <product-slider-component :title="'جدید ترین محصولات'" :products="newProducts"/>
</template>

<script>
import ProductSliderComponent from "@/components/ShopView/ProductSliderComponent.vue";
import useServerStore from "@/stores/server.js";
import {mapState} from "pinia";
import axios from "axios";

export default {
  name: "NewProductsComponent",
  data() {
    return {
      newProducts: []
    }
  },
  components: {ProductSliderComponent},
  methods: {
    async getNewProducts() {
      await axios.get(`${this.serverDomain}/product/new-products/`).then(
          response => {
            this.newProducts = response.data
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
    this.getNewProducts()
  }
}
</script>