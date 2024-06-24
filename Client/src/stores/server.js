import {defineStore} from "pinia";
import axios from "axios";


export default defineStore('server', {
    state: () => ({
        serverDomain: "http://localhost:8000",

        username: null,

        siteName: null,
        siteDescription: null,
        howActiveUserAccount: null,
        siteBanners:null,
    }),
    actions: {
        async refreshToken() {
            const refresh = localStorage.getItem('refresh')
            let success = false
            if (refresh !== null) {
                await axios.post(`${this.serverDomain}/user/refresh/`, {
                    refresh: refresh
                }).then(async (response) => {
                    localStorage.setItem('access', response.data['access'])
                    await this.getUsername().then((res) => {
                        if (res) {
                            success = true
                        }
                    }).catch((error) => {
                        console.log(error)
                    })
                }).catch((error) => {
                    console.log(error)
                    this.username = null
                    localStorage.removeItem('access')
                    localStorage.removeItem('refresh')
                })
            } else {
                this.username = null
                localStorage.removeItem('access')
                localStorage.removeItem('refresh')
            }
            return success
        },
        async getUsername() {
            const access = localStorage.getItem('access')
            let success = false
            if (access !== null) {
                await axios.get(`${this.serverDomain}/user/`, {
                    headers: {
                        Authorization: `Bearer ${access}`
                    }
                }).then((response) => {
                    this.username = response.data.username
                    success = true
                }).catch(async (error) => {
                    if (error.response.data.code === 'token_not_valid') {
                        localStorage.removeItem('access')
                        await this.refreshToken().then((res) => {
                            if (res) {
                                success = true
                            }
                        }).catch((error) => {
                            console.log(error)
                        })
                    } else {
                        this.username = null
                        localStorage.removeItem('access')
                        localStorage.removeItem('refresh')
                    }
                })
            } else {
                this.username = null
                localStorage.removeItem('access')
                localStorage.removeItem('refresh')
            }
            return success
        },
        async getSiteSetting() {
            if (
                this.siteName === null ||
                this.siteDescription === null ||
                this.descriptionImg === null ||
                this.siteBanners === null ||
                this.howActiveUserAccount === null
            ) {
                await axios.get(`${this.serverDomain}/site-setting/`).then(
                    response => {
                        this.siteName = response.data.site_name
                        this.howActiveUserAccount = response.data.how_active_user_account
                        this.siteDescription = response.data.site_description
                        this.siteBanners = response.data.banners
                    }).catch(error => {
                    console.log(error)
                })
            }
        },
    }
})