import { createApp } from 'vue'
import { createPinia } from 'pinia'
import Toast from 'vue-toastification'
import { POSITION } from 'vue-toastification'
import type { PluginOptions } from 'vue-toastification'
import 'vue-toastification/dist/index.css'

import App from './App.vue'
import router from './router'

import './assets/main.css'

import { APIService } from '@/common/api'

APIService.init()

const app = createApp(App)

app.use(createPinia())
app.use(router)

// Vue toastification options
const options: PluginOptions = {
    position: POSITION.BOTTOM_CENTER,
    transition: 'Vue-Toastification__fade',
    maxToasts: 5,
    newestOnTop: true,
    timeout: 5000,
    closeOnClick: true,
    pauseOnFocusLoss: true,
    pauseOnHover: true,
    draggable: true,
    draggablePercent: 0.6,
    showCloseButtonOnHover: false,
    hideProgressBar: true,
    closeButton: 'button',
    icon: true,
    rtl: false
}
app.use(Toast, options)

app.mount('#app')
