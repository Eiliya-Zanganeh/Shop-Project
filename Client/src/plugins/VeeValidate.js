import {Form as VeeForm, Field as VeeField, defineRule, ErrorMessage as VeeErrorMessage, configure} from "vee-validate";
import {required, min, max, alpha_spaces, email, confirmed, numeric} from "@vee-validate/rules";
import {config} from "@vue/test-utils";

export default {
    install(app) {
        app.component('VeeForm', VeeForm)
        app.component('VeeField', VeeField)
        app.component('VeeErrorMessage', VeeErrorMessage)

        defineRule('required', required)
        defineRule('email', email)
        defineRule('min', min)
        defineRule('max', max)
        defineRule('numeric', numeric)
        defineRule('confirmed', confirmed)

        configure({
            generateMessage:(context) => {
                const messages = {
                    required : "فیلد نمی تواند خالی باشد.",
                    email: "ایمیل را به درستی وارد نکرده اید.",
                    min: `اندازه ورودی نمی تواند کمتر از ${context.rule.params} کاراکتر باشد.`,
                    max: `اندازه ورودی نمی تواند بیشتر از ${context.rule.params} کاراکتر باشد.`,
                    numeric: 'نمی توان داده غیر عدد وارد کرد.',
                    confirmed: 'رمز عبور با تکرار رمز عبور مقایرت دارد.'
                }
                return messages[context.rule.name] ? messages[context.rule.name] : "در وارد کردن داده دقت فرمایید"
            },
            validateOnBlur: true,
            validateOnChange: true,
            validateOnInput: true,
            validateOnModelUpdate: true
        })
    }
}