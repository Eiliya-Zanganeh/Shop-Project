<template>

  <transition mode="out-in" appear name="fade" type="transition" >

    <login-form-component @changePage="changePage" v-if="page === 'login'" key="login"/>

    <register-form-component @changePage="changePage"  v-else-if="page === 'register'" key="register"/>

  </transition>

</template>

<script>
import LoginFormComponent from "@/components/LoginView/LoginFormComponent.vue";
import RegisterFormComponent from "@/components/LoginView/RegisterFormComponent.vue";

export default {
  name: "LoginView",
  components: {LoginFormComponent, RegisterFormComponent},
  data(){
    return{
      page: 'login'
    }
  },
  methods:{
    changePage(page){
      this.page = page
    }
  }

}
</script>

<style>
@import "@/assets/login/login.css";

section{
  background-color: #ffbcbc;
}

.fade-enter-from {
  opacity: 0;

}
.fade-enter-active {
  transition: all 1.0s linear;
}
.fade-leave-active {
  transition: all .5s linear;
}
.fade-leave-to {
  opacity: 0;
}
</style>