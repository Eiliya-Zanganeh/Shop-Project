<template>
  <section class="ftco-section">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-md-12 col-lg-10">
          <div class="wrap d-md-flex">
            <div class="text-wrap p-4 p-lg-5 text-center d-flex align-items-center">
              <div class="text w-100">
                <h2>ورود به صفحه کاربری</h2>
                <p>آیا حساب کاربری ندارید؟</p>
                <button type="button" class="btn btn-white btn-outline-white" @click.prevent="changePage">ثبت نام
                </button>
              </div>
            </div>
            <div class="login-wrap p-4 p-lg-5">
              <div class="d-flex">
                <div class="w-100">
                  <h3 class="mb-4 text-right">ورود کاربر</h3>
                </div>

              </div>
              <div v-if="showAlert" :class="alertBackgroundColorClass"
                   class="text-light p-2 text-center rounded mb-3 dir-rtl">
                {{ alertMessage }}
              </div>
              <VeeForm @submit="login" class="signin-form">
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
                      :rules="'required|min:8'"
                      type="password"
                      class="form-control text-right"
                      placeholder="رمز عبور"
                  />
                  <VeeErrorMessage name="password" class="text-danger d-block text-center dir-rtl"/>
                </div>
                <div class="form-group">
                  <button v-if="showSubmitButton" type="submit" class="form-control btn btn-primary submit px-3">ورود
                  </button>
                </div>
                <div class="form-group d-md-flex">
                  <div class="w-100 text-md-right">
                    <a href="#" class="d-block text-right">فراموشی رمز عبور</a>
                  </div>
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
import useServerStore from '@/stores/server.js'
import {mapState, mapActions, mapWritableState} from "pinia";
import axios from "axios";

export default {
  name: "LoginFormComponent",
  data() {
    return {
      alertBackgroundColorClass: "",
      showAlert: false,
      alertMessage: "",
      showSubmitButton: true
    }
  },
  emits: ['changePage'],
  computed: {
    ...mapState(useServerStore, ['howActiveUserAccount', 'serverDomain']),
    ...mapWritableState(useServerStore, ['username'])
  },
  methods: {
    changePage() {
      this.$emit('changePage', 'register')
    },
    ...mapActions(useServerStore, ['getSiteSetting']),
    async login(values) {
      this.showSubmitButton = false
      this.alertMessage = "در حال ورود..."
      this.alertBackgroundColorClass = "bg-info"
      this.showAlert = true

      let username = ""
      if (this.howActiveUserAccount === 'phone') {
        username = values.phone
      } else if (this.howActiveUserAccount === 'email') {
        username = values.email
      }
      try {
        const result = await axios.post(`${this.serverDomain}/user/token/`, {
          username: username,
          password: values.password
        })
        localStorage.setItem('access', result.data['access']);
        localStorage.setItem('refresh', result.data['refresh']);
        this.username = username
        this.alertMessage = "ورود با موفقیت انجام شد..."
        this.alertBackgroundColorClass = "bg-success"
      } catch (e) {
        this.alertBackgroundColorClass = "bg-warning"
        if (e.response.data.detail === 'هیچ اکانت فعالی برای اطلاعات داده شده یافت نشد') {
          this.alertMessage = "کاربر فعالی یافت نشد..."
        } else {
          this.alertMessage = "مشکلی در ارسال داده رخ داده..."
        }
        this.showSubmitButton = true
      }
    }
  },
  mounted() {
    this.getSiteSetting()
  }
}
</script>