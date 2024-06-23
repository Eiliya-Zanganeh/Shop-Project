<template>
  <div class="container">
    <div class="card">
      <div class="container-fliud">
        <div class="wrapper row">
          <div class="preview col-md-6">

            <div class="preview-pic tab-content">
              <div class="tab-pane active" id="pic-1"><img :src="`${serverDomain}/${current_image}`"/></div>
            </div>
            <ul class="preview-thumbnail nav nav-tabs d-flex justify-content-cent">
              <li
                  class="active"
                  v-for="(image, idx) in product_galleries"
                  :key="image.id"
                  @click.prevent="changeImage(image.image)"
                  v-show="idx < productCount"
              >
                <a><img
                    :src="`${serverDomain}/${image.image}`"/></a>
              </li>
            </ul>
            <div v-if="product_galleries.length > 4" class="d-flex justify-content-center w-25 align-self-center">
              <button @click.prevent="sliderPrevious" class="btn btn-block btn-outline-warning m-1 p-0"
                      style="width: 30px; height: 30px"><i class="bi bi-arrow-right"></i></button>
              <button @click.prevent="sliderNext" class="btn btn-block btn-outline-warning m-1 p-0"
                      style="width: 30px; height: 30px"><i class="bi bi-arrow-left"></i></button>
            </div>
          </div>
          <div class="details col-md-6">
            <h5 class="product-title text-right">{{ product_name }}</h5>
            <br>
            <h6>موجودی در انبار {{ product_count }}</h6>
            <br>
            <p class="product-description text-right">{{ product_description }}</p>
            <h4 class="price text-right"><span>{{ Number(product_price).toLocaleString('fa-IR') }} تومان</span></h4>
            <div class="action">
              <button @click.prevent="addCart(product_id)" class="add-to-cart btn btn-block" type="button">اضافه کردن به
                سبد خرید
              </button>
            </div>
          </div>
        </div>
        <hr>
        <product-slider-component :title="'محصولات پیشنهادی'" :products="suggested_products"/>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import {mapActions, mapState} from "pinia";
import useServerStore from "@/stores/server.js";
import ProductSliderComponent from "@/components/ProductSliderComponent.vue";

export default {
  name: "DetailProductView",
  components: {ProductSliderComponent},
  computed: {
    ...mapState(useServerStore, ['serverDomain'])
  },
  data() {
    return {
      product_id: null,
      product_name: null,
      product_description: null,
      product_price: null,
      product_galleries: [],
      current_image: null,
      productCount: 4,
      suggested_products: null,
      product_count: null
    }
  },
  async mounted() {
    await axios.get(`${this.serverDomain}/product/detail_product/${this.$route.params['product']}`).then(
        (response) => {
          this.product_id = response.data.product.id
          this.product_name = response.data.product.name
          this.product_galleries = response.data.product.galleries
          this.product_galleries.unshift({id: 0, image: response.data.product.image})
          this.current_image = response.data.product.image
          this.product_description = response.data.product.description
          this.product_price = response.data.product.price
          this.suggested_products = response.data.suggested_products
          this.product_count = response.data.product.count
        }).catch((error) => {
      console.log(error)
    })
    this.timer = setInterval(this.sliderNext, 5000);
  },
  methods: {
    ...mapActions(useServerStore, ['getUsername']),
    changeImage(url) {
      this.current_image = url
    },
    sliderNext() {
      const result = this.product_galleries.shift()
      this.product_galleries.push(result)
      clearInterval(this.timer);
      this.timer = setInterval(this.sliderNext, 5000);
    },
    sliderPrevious() {
      const result = this.product_galleries.pop()
      this.product_galleries.unshift(result)
      clearInterval(this.timer);
      this.timer = setInterval(this.sliderNext, 5000);
    },
    async addCart(id) {
      this.getUsername().then(
          (login) => {
            if (!login) {
              this.$router.push({name: 'login'})
            }
          }
      )
      const access = localStorage.getItem('access')
      await axios.get(`${this.serverDomain}/user/add-cart/${id}`, {
        headers: {
          Authorization: `Bearer ${access}`
        }
      }).then(() => {
        this.$router.push({name: 'cart'})
      }).catch(() => {
        this.$router.push({name: 'login'})
      })
    }
  },
  beforeUnmount() {
    clearInterval(this.timer);
  }
}
</script>

<style>
@import "@/assets/detail/detail.css";
</style>