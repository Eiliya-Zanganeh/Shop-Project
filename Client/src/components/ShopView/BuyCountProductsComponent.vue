<template>
  <product-slider-component :title="'محصولات پرفروش'" :products="buyCountProducts"/>
</template>

<script>
import ProductSliderComponent from "@/components/ShopView/ProductSliderComponent.vue";
import useServerStore from "@/stores/server.js";
import {mapState} from "pinia";
import axios from "axios";

export default {
  name: "BuyCountProductsComponent",
  data() {
    return {
      buyCountProducts: []
    }
  },
  components: {ProductSliderComponent},
  methods: {
    async getBuyCountProducts() {
      await axios.get(`${this.serverDomain}/product/buy-count-products/`).then(
          response => {
            this.buyCountProducts = response.data
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
    this.getBuyCountProducts()
  }
}
</script>