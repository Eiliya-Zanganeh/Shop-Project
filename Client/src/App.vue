<template>

  <header-component/>

  <RouterView/>

  <footer-component/>

</template>
<script>
import {mapActions} from "pinia";
import useServerStore from "@/stores/server.js";
import HeaderComponent from "@/components/HeaderComponent.vue";
import FooterComponent from "@/components/FooterComponent.vue";

export default {
  name: "App",
  components: {FooterComponent, HeaderComponent},
  methods: {
    ...mapActions(useServerStore, ['getSiteSetting', 'getUsername']),
  },
  async mounted() {
    await this.getSiteSetting()
    await this.getUsername()
  }
}
</script>


