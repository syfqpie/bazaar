import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import PublicLayoutVue from '@/layouts/PublicLayout.vue'
import AuthLayoutVue from '@/layouts/AuthLayout.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'public',
      component: PublicLayoutVue,
      children: [
        {
          path: 'home',
          name: 'home',
          component: HomeView
        }
      ]
    },
    {
      path: '/auth',
      name: 'authentication',
      component: AuthLayoutVue,
      children: [
        {
          path: 'login',
          name: 'login',
          component: () => import('../views/auth/LoginView.vue')
        },
        {
          path: 'register/customer',
          name: 'registerCustomer',
          component: () => import('../views/auth/RegistrationView.vue')
        },
        {
          path: 'register/vendor',
          name: 'registerVendor',
          component: () => import('../views/auth/VendorRegistrationView.vue')
        },
        {
          path: 'reset',
          name: 'reset',
          component: () => import('../views/auth/ResetView.vue')
        },
        {
          path: 'confirm-reset',
          name: 'confirm-reset',
          component: () => import('../views/auth/ConfirmResetView.vue')
        },
        {
          path: 'verify',
          name: 'verify',
          component: () => import('../views/auth/VerifyAccountView.vue')
        }
      ]
    }
  ]
})

export default router
