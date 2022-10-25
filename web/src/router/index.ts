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
          path: 'registration/customer',
          name: 'registerCustomer',
          component: () => import('../views/auth/RegistrationView.vue')
        },
        {
          path: 'registration/vendor',
          name: 'registerVendor',
          component: () => import('../views/auth/VendorRegistrationView.vue')
        },
        {
          path: 'registration/resend-verification',
          name: 'resendVerification',
          component: () => import('../views/auth/ResendVerificationView.vue')
        },
        {
          path: 'registration/verify',
          name: 'verify',
          component: () => import('../views/auth/VerifyAccountView.vue')
        },
        {
          path: 'reset',
          name: 'reset',
          component: () => import('../views/auth/ResetView.vue')
        },
        {
          path: 'reset/confirm',
          name: 'confirmReset',
          component: () => import('../views/auth/ConfirmResetView.vue')
        },
      ]
    }
  ]
})

export default router
