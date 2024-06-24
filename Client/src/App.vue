<template>

  <header-component/>

  <RouterView/>

  <footer-component/>

</template>
<script>
import {mapActions} from "pinia";
import useServerStore from "@/stores/server.js";
import HeaderComponent from "@/components/App/HeaderComponent.vue";
import FooterComponent from "@/components/App/FooterComponent.vue";

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


