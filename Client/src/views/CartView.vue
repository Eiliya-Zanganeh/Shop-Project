<template>
  <div class="untree_co-section before-footer-section">
    <div class="container">
      <div class="row mb-5">
        <form class="col-md-12" method="post">
          <div class="site-blocks-table">
            <table class="table">
              <thead>
              <tr>
                <th class="product-thumbnail">عکس محصول</th>
                <th class="product-name">نام محصول</th>
                <th class="product-price">قیمت محصول</th>
                <th class="product-quantity">تعداد محصول</th>
                <th class="product-total">جمع قیمت ها</th>
                <th class="product-remove">حذف محصول</th>
              </tr>
              </thead>
              <tbody>
              <tr v-for="(product, idx) in cart" :key="product.id">
                <td class="product-thumbnail">
                  <router-link class="text-decoration-none"
                               :to="{name: 'detail-product', params: {product: product.product.id}}">
                    <img :src="`${serverDomain}/${product.product.image}`" alt="Image" class="img-fluid">
                  </router-link>
                </td>
                <td class="product-name">
                  <h2 class="h5 text-black">
                    <router-link class="text-decoration-none"
                                 :to="{name: 'detail-product', params: {product: product.product.id}}">
                      <p style="max-width: 250px;white-space: nowrap; overflow: hidden; text-overflow: ellipsis">
                        {{ product.product.name }}
                      </p>
                    </router-link>
                  </h2>
                </td>
                <td><h4>{{ Number(product.product.price).toLocaleString('fa-IR') }} تومان</h4></td>
                <td class="p-0">
                  <div class="input-group mb-3 d-flex align-items-center quantity-container" style="max-width: 120px;">
                    <div class="input-group-prepend">
                      <button v-if="product.count > 1 && hiddenBtn" @click.prevent="minCount(product.id, idx)"
                              class="btn btn-outline-black decrease" type="button">&minus;
                      </button>
                    </div>
                    <input type="text" class="form-control text-center quantity-amount" :value="product.count"
                           placeholder=""
                           aria-label="Example text with button addon" aria-describedby="button-addon1">
                    <div class="input-group-append">
                      <button v-if="hiddenBtn" @click.prevent="addCount(product.id, idx)"
                              class="btn btn-outline-black increase"
                              type="button">&plus;
                      </button>
                    </div>
                  </div>

                </td>
                <td><h4>{{ Number(product.product.price * product.count).toLocaleString('fa-IR') }} تومان</h4></td>
                <td>
                  <button @click.prevent="removeCart(product.id, idx)" class="btn btn-black btn-sm">X</button>
                </td>
              </tr>
              </tbody>
            </table>
          </div>
        </form>
      </div>

      <div class="row">

        <div class="col-md-6">
          <div class="row justify-content-center">
            <div class="col-md-7">
              <div class="row">
                <div class="col-md-12 text-right border-bottom mb-5">
                  <h3 class="text-black h4 text-uppercase">اطلاعات سبد خرید</h3>
                </div>
              </div>
              <div class="row mb-3">
                <div class="col-md-6">
                  <span class="text-black">Subtotal</span>
                </div>
                <div class="col-md-6 text-right">
                  <h4 class="text-black">{{ cartCounts }}</h4>
                </div>
              </div>
              <div class="row mb-5">
                <div class="col-md-6">
                  <span class="text-black">Total</span>
                </div>
                <div class="col-md-6 text-right">
                  <h4 class="text-black">{{ cartPrice }}</h4>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-6 mt-5">
          <div class="row mb-5">
            <div class="col-md-6 mb-3 mb-md-0">
              <router-link
                  :to="{name: 'checkout'}"
                  class="btn btn-outline-black btn-sm btn-block text-light"
              >
                تکمیل فرایند خرید
              </router-link>
            </div>
            <div class="col-md-6">
              <router-link
                  :to="{name: 'shop'}"
                  class="btn btn-outline-black btn-sm btn-block text-light"
              >
                ادامه خرید
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import useServerStore from '@/stores/server.js'
import {mapActions, mapState} from "pinia";

export default {
  name: "CartView",
  data() {
    return {
      cart: [],
      hiddenBtn: true
    }
  },
  methods: {
    ...mapActions(useServerStore, ['getUsername']),
    async addCount(id, idx) {
      this.hiddenBtn = false
      const access = localStorage.getItem('access')
      await axios.get(`${this.serverDomain}/user/add-count-cart/${id}/`, {
        headers: {
          Authorization: `Bearer ${access}`
        }
      }).then((responce) => {
        this.hiddenBtn = true
        if (this.cart[idx]['count'] === responce.data) {
          alert("موجودی در انبار کافی نیست")
        } else {
          this.cart[idx]['count'] = responce.data
        }
      }).catch(() => {
        this.$router.push({name: 'login'})
      })
    },
    async minCount(id, idx) {
      this.hiddenBtn = false
      const access = localStorage.getItem('access')
      await axios.get(`${this.serverDomain}/user/min-count-cart/${id}/`, {
        headers: {
          Authorization: `Bearer ${access}`
        }
      }).then((responce) => {
        this.cart[idx]['count'] = responce.data
        this.hiddenBtn = true
      }).catch(() => {
        this.$router.push({name: 'login'})
      })
    },
    async removeCart(id, idx) {
      this.hiddenBtn = false
      const access = localStorage.getItem('access')
      await axios.get(`${this.serverDomain}/user/remove-cart/${id}/`, {
        headers: {
          Authorization: `Bearer ${access}`
        }
      }).then(() => {
        this.cart.pop(idx)
        this.hiddenBtn = true
      }).catch(() => {
        this.$router.push({name: 'login'})
      })
    }
  },
  computed: {
    ...mapState(useServerStore, ['serverDomain']),
    cartCounts(){
      let count = 0
      this.cart.forEach((product) => {
        count += product['count']
      })
      return count
    },
    cartPrice(){
      let price = 0
      this.cart.forEach((product) => {
        price += Number(product['product']['price']) * product['count']
      })
      return price.toLocaleString('fa-IR')
    }
  },
  beforeMount() {
    this.getUsername().then(
        (login) => {
          if (!login) {
            this.$router.push({name: 'login'})
          }
        }
    )
  },
  async mounted() {
    const access = localStorage.getItem('access')
    await axios.get(`${this.serverDomain}/user/cart/`, {
      headers: {
        Authorization: `Bearer ${access}`
      }
    }).then((response) => {
      this.cart = response.data
    }).catch(() => {
      this.$router.push({name: 'login'})
    })
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
