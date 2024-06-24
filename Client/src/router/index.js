import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LoginView from "@/views/LoginView.vue";
import ShopView from "@/views/ShopView.vue";
import CategoryShopView from "@/views/CategoryShopView.vue";
import DetailProductView from "@/views/DetailProductView.vue";
import CartView from "@/views/CartView.vue";
import CheckoutView from "@/views/CheckoutView.vue";
import SpecialProductsView from "@/views/SpecialProductsView.vue";

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/shop',
    name: 'shop',
    component: ShopView
  },
  {
    path: '/shop-category/:category',
    name: 'shop-category',
    component: CategoryShopView
  },
  {
    path: '/detail-product/:product',
    name: 'detail-product',
    component: DetailProductView
  },
  {
    path: '/cart',
    name: 'cart',
    component: CartView
  },
  {
    path: '/special-products',
    name: 'special_products',
    component: SpecialProductsView
  },
  {
    path: '/checkout',
    name: 'checkout',
    component: CheckoutView
  },
  {
    path: '/:catchAll(.*)*',
    redirect: {name: 'home'}
  }
]

const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes,
  linkExactActiveClass: 'active'
})

export default router
