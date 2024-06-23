<template>
  <nav class="custom-navbar navbar navbar navbar-expand-md navbar-dark" arial-label="Furni navigation bar">
    <div class="container">
      <router-link class="navbar-brand" :to="{name: 'home'}">{{ siteName }}<span> .</span></router-link>

      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarsFurni"
              aria-controls="navbarsFurni" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarsFurni">
        <ul class="custom-navbar-nav navbar-nav ms-auto mb-2 mb-md-0">
          <router-link class="nav-item" :to="{name: 'home'}">
            <p class="nav-link text-center">خانه</p>
          </router-link>
          <router-link class="nav-item" :to="{name: 'shop'}">
            <p class="nav-link text-center">فروشگاه</p>
          </router-link>
          <li><a class="nav-link text-center" href="about.html">درباره ما</a></li>
          <li><a class="nav-link text-center" href="services.html">سرویس ها</a></li>
          <li><a class="nav-link text-center" href="blog.html">مقالات</a></li>
          <li><a class="nav-link text-center" href="contact.html">تماس با ما</a></li>
        </ul>

        <ul class="custom-navbar-cta navbar-nav mb-2 mb-md-0 ms-5 justify-content-center">
          <router-link
              :to="{name: 'login'}"
              class="text-center m-0"
              v-if="username === null"
          >
            <a class="nav-link m-2">
              <img src="/home/images/user.svg">
            </a>
          </router-link>
          <router-link
              :to="{name: 'cart'}"
              class="text-center m-0"
              v-if="username !== null"
          >
              <img src="/home/images/cart.svg">
          </router-link>
        </ul>
      </div>
    </div>
  </nav>
</template>
<script>
import useServerStore from '@/stores/server.js'
import {mapState} from "pinia";

export default {
  name: "HeaderComponent",
  computed: {
    ...mapState(useServerStore, ['siteName', 'username'])
  },

}
</script>