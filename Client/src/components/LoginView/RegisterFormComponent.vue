<template>
  <section class="ftco-section">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-md-12 col-lg-10">
          <div class="wrap d-md-flex">
            <div class="text-wrap p-4 p-lg-5 text-center d-flex align-items-center order-md-last">
              <div class="text w-100">
                <h2>ثبت نام حساب کاربری</h2>
                <p>آیا قبلا ثبت نام کردید؟</p>
                <button type="button" class="btn btn-white btn-outline-white" @click.prevent="changePage">ورود</button>
              </div>
            </div>
            <div class="login-wrap p-4 p-lg-5">
              <div class="d-flex">
                <div class="w-100 text-right">
                  <h3 class="mb-4">ثبت نام</h3>
                </div>
              </div>
              <div v-if="showAlert" :class="alertBackgroundColorClass"
                   class="text-light p-2 text-center rounded mb-3 dir-rtl">
                {{ alertMessage }}
              </div>
              <VeeForm @submit="register" class="signin-form">
                <div class="form-group mb-3">
                  <label class="label d-block text-right" for="name">نام و نام خانوادگی</label>
                  <VeeField
                      :rules="'required|max:64'"
                      name="name"
                      type="text"
                      class="form-control text-right"
                      placeholder="نام و نام خانوادگی"
                  />
                  <VeeErrorMessage name="name" class="text-danger d-block text-center dir-rtl"/>
                </div>
                <div v-if="howActiveUserAccount === 'email'" class="form-group mb-3">
                  <label class="label d-block text-right" for="name">ایمیل</label>
                  <VeeField
                      :rules="'required|email'"
                      name="email"
                      type="email"
                      class="form-control text-right"
                      placeholder="ایمیل"
                  />
                  <VeeErrorMessage name="email" class="text-danger d-block text-center dir-rtl"/>
                </div>
                <div v-else-if="howActiveUserAccount === 'phone'" class="form-group mb-3">
                  <label class="label d-block text-right" for="name">شماره تلفن همراه</label>
                  <VeeField name="phone" :rules="'required|min:11|max:11|numeric'" :bails="false"
                            v-slot="{ field, errors }">
                    <input
                        type="text"
                        class="form-control text-right"
                        placeholder="شماره تلفن همراه"
                        v-bind="field"
                    >
                    <div v-for="error in errors" :key="error" class="text-danger d-block text-center dir-rtl">{{
                        error
                      }}
                    </div>
                  </VeeField>
                </div>
                <div class="form-group mb-3">
                  <label class="label d-block text-right" for="password">رمز عبور</label>
                  <VeeField
                      name="password"
                      type="password"
                      class="form-control text-right"
                      placeholder="رمز عبور"
                      :rules="'required|min:8|max:64'"
                  />
                  <VeeErrorMessage class="text-danger d-block text-center" name="password"/>
                </div>
                <div class="form-group mb-3">
                  <label class="label d-block text-right" for="password">تکرار رمز عبور</label>
                  <VeeField
                      name="confrim_password"
                      type="password"
                      class="form-control text-right"
                      placeholder="تکرار رمز عبور"
                      :rules="'required|confirmed:@password'"
                  />
                  <VeeErrorMessage class="text-danger d-block text-center" name="confrim_password"/>

                </div>
                <div v-if="showSubmitButton" class="form-group">
                  <button type="submit" class="form-control btn btn-primary submit px-3">ثبت کاربر جدید</button>
                </div>
              </VeeForm>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import {ErrorMessage as VeeErrorMessage} from "vee-validate";
import {mapState} from "pinia";
import useServerStore from "@/stores/server.js";
import axios from "axios";

export default {
  name: "RegisterFormComponent",
  components: {VeeErrorMessage},
  emits: ['changePage'],
  data() {
    return {
      alertBackgroundColorClass: "",
      showAlert: false,
      alertMessage: "",
      showSubmitButton: true
    }
  },
  computed: {
    ...mapState(useServerStore, ['howActiveUserAccount', 'serverDomain'])
  },
  methods: {
    changePage() {
      this.$emit('changePage', 'login')
    },
    async register(values) {
      this.showSubmitButton = false
      this.alertMessage = "در حال ثبت نام..."
      this.alertBackgroundColorClass = "bg-info"
      this.showAlert = true

      let username = ""
      if (this.howActiveUserAccount === 'phone') {
        username = values.phone
      } else if (this.howActiveUserAccount === 'email') {
        username = values.email
      }

      await axios.post(`${this.serverDomain}/user/register/`, {
        username: username,
        first_name: values.name,
        password: values.password
      }).then(() => {
        this.alertMessage = "ثبت نام با موفقیت انجام شد لطفا با لینکی که برای شما ارسال می شود اکانت خود را فعال کنید."
        this.alertBackgroundColorClass = "bg-success"
      }).catch((error) => {
        this.alertBackgroundColorClass = "bg-warning"
        if (error.response.data.message === 'user is exits'){
          this.alertMessage = "کاربر تکراری می باشد"
        } else {
          this.alertMessage = "مشکلی در ارسال داده رخ داده..."
        }
        this.showSubmitButton = true
      })
    }
  }
}
</script>