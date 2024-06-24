<template>
  <div class="untree_co-section product-section before-footer-section">
    <div class="container">
      <div class="alert alert-info alert-dismissible fade show" role="alert">
        <h3 class="alert-heading text-center"><strong>فروش ویژه</strong> جشنواره تخفیفاتی و پیشنهاد های شگفت انگیز</h3>
      </div>

      <h5 class="bg-dark text-light m-1 text-center rounded-3" style="width: 25vh">تعداد محصولات ({{ Number(count).toLocaleString('fa-IR') }})</h5>
      <br>
      <div class="row">
        <div
            v-for="product in products"
            :key="product.id"
            class="col-12 col-md-4 col-lg-3 mb-5"
        >
          <router-link class="product-item p-0" :to="{name: 'detail-product', params: {product: product.id}}">
            <div class="position-relative">
              <img :src="product.image"
                   class="img-fluid product-thumbnail rounded-3">
              <span
                  v-if="product.offer_price"
                  style="left: 18%; top:3%; border-radius: 10%; width: 20%"
                  class="position-absolute bg-danger text-light"
              >{{ product.offer }}%</span>
            </div>
            <h6 style="height:40px;max-height: 40px; overflow-y: hidden; text-overflow: ellipsis;">{{ product.name }}</h6>
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
        </div>

        <div class="d-flex justify-content-center mt-2">
          <button
              class="btn btn-block btn-dark m-1"
              style="width: 20vh"
              @click.prevent="previousPage"
              type="button"
              v-if="previous !== null"
          >
            محصولات قبلی
          </button>
          <button
              class="btn btn-block btn-dark m-1"
              style="width: 20vh"
              @click.prevent="nextPage"
              type="button"
              v-if="next !== null"
          >
            محصولات بعدی
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import useServerStore from '@/stores/server.js'
import {mapState} from "pinia";
import axios from "axios";

export default {
  name: "SpecialProductsView",
  data() {
    return {
      products: null,
      next: null,
      previous: null,
      count: null
    }
  },
  computed: {
    ...mapState(useServerStore, ['serverDomain'])
  },
  async mounted() {
    await axios.get(`${this.serverDomain}/product/spacial_products/`).then(
        (response) => {
          this.products = response.data.results
          this.next = response.data.next
          this.previous = response.data.previous
          this.count = response.data.count
        }).catch((error) => {
      console.log(error)
    })
  },
  methods:{
    async previousPage(){
      await axios.get(this.previous).then(
          (response) => {
            this.products = response.data.results
            this.next = response.data.next
            this.previous = response.data.previous
            this.count = response.data.count
          }).catch((error) => {
        console.log(error)
      })
    },
    async nextPage(){
      await axios.get(this.next).then(
          (response) => {
            this.products = response.data.results
            this.next = response.data.next
            this.previous = response.data.previous
            this.count = response.data.count
          }).catch((error) => {
        console.log(error)
      })
    }
  }
}
</script>
