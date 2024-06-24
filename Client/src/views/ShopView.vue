<template>

  <product-categories-component/>

  <popular-products-component/>

  <buy-count-products-component/>

  <new-products-component/>

  <visit-count-products-component/>

</template>

<script>
import ProductCategoriesComponent from "@/components/ShopView/ProductCategoriesComponent.vue";
import PopularProductsComponent from "@/components/ShopView/PopularProductsComponent.vue";
import BuyCountProductsComponent from "@/components/ShopView/BuyCountProductsComponent.vue";
import NewProductsComponent from "@/components/ShopView/NewProductsComponent.vue";
import VisitCountProductsComponent from "@/components/ShopView/VisitCountProductsComponent.vue";

export default {
  name: "ShopView",
  components: {
    VisitCountProductsComponent,
    NewProductsComponent,
    BuyCountProductsComponent,
    PopularProductsComponent,
    ProductCategoriesComponent
  }
}
</script>