import { createRouter, createWebHistory } from 'vue-router'

import { useAuthStore } from '@/stores'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'public',
      component: () => import('@/layouts/PublicLayout.vue'),
      children: [
        {
          path: 'home',
          name: 'home',
          component: () => import('@/views/HomeView.vue')
        }
      ]
    },
    {
      path: '/auth',
      name: 'authentication',
      component: () => import('@/layouts/AuthLayout.vue'),
      children: [
        {
          path: 'login',
          name: 'login',
          component: () => import('@/views/auth/LoginView.vue')
        },
        {
          path: 'registration/customer',
          name: 'registerCustomer',
          component: () => import('@/views/auth/RegistrationView.vue')
        },
        {
          path: 'registration/vendor',
          name: 'registerVendor',
          component: () => import('@/views/auth/VendorRegistrationView.vue')
        },
        {
          path: 'registration/resend-verification',
          name: 'resendVerification',
          component: () => import('@/views/auth/ResendVerificationView.vue')
        },
        {
          path: 'registration/verify',
          name: 'verify',
          component: () => import('@/views/auth/VerifyAccountView.vue')
        },
        {
          path: 'reset',
          name: 'reset',
          component: () => import('@/views/auth/ResetView.vue')
        },
        {
          path: 'reset/confirm',
          name: 'confirmReset',
          component: () => import('@/views/auth/ConfirmResetView.vue')
        },
      ]
    }
  ]
})

// AuthGuard
router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore()

  if (authStore.$state.accessToken && to.path.startsWith('/auth')) {
    return next({ path: '/home' })
  }

  return next()
})

export default router
