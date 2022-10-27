import { createRouter, createWebHistory } from 'vue-router'

import { useAuthStore } from '@/stores'

const ROOT_ROUTE = '/home'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/home',
      name: 'public',
      component: () => import('@/layouts/PublicLayout.vue'),
      children: [
        {
          path: 'home',
          name: 'home',
          component: () => import('@/views/HomeView.vue'),
          meta: { title: 'Home' }
        },
        {
          path: 'explore',
          name: 'explore',
          component: () => import('@/views/ExploreView.vue'),
          meta: { title: 'Explore' }
        },
        {
          path: 'faq',
          name: 'faq',
          component: () => import('@/views/FaqView.vue'),
          meta: { title: 'FAQ' }
        },
        {
          path: 'user',
          name: 'user',
          component: () => import('@/views/AccountView.vue'),
          meta: { requiresAuth: true },
          children: [
            {
              path: 'account',
              name: 'userAccount',
              children: [
                {
                  path: 'profile',
                  name: 'userAccountProfile',
                  component: () => import('@/views/account/ProfileView.vue'),
                  meta: { title: 'Profile' }
                },
                {
                  path: 'address',
                  name: 'userAccountAddress',
                  component: () => import('@/views/account/AddressView.vue'),
                  meta: { title: 'Address' }
                },
                {
                  path: 'change-password',
                  name: 'userAccountChangePassword',
                  component: () => import('@/views/account/ChangePasswordView.vue'),
                  meta: { title: 'Change password' }
                }
              ]
            }
          ]
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
          component: () => import('@/views/auth/LoginView.vue'),
          meta: { title: 'Login' }
        },
        {
          path: 'registration/customer',
          name: 'registerCustomer',
          component: () => import('@/views/auth/RegistrationView.vue'),
          meta: { title: 'Customer registration' }
        },
        {
          path: 'registration/vendor',
          name: 'registerVendor',
          component: () => import('@/views/auth/VendorRegistrationView.vue'),
          meta: { title: 'Vendor registration' }
        },
        {
          path: 'registration/resend-verification',
          name: 'resendVerification',
          component: () => import('@/views/auth/ResendVerificationView.vue'),
          meta: { title: 'Resend verification' }
        },
        {
          path: 'registration/verify',
          name: 'verify',
          component: () => import('@/views/auth/VerifyAccountView.vue'),
          meta: { title: 'Verify' }
        },
        {
          path: 'reset',
          name: 'reset',
          component: () => import('@/views/auth/ResetView.vue'),
          meta: { title: 'Reset' }
        },
        {
          path: 'reset/confirm',
          name: 'confirmReset',
          component: () => import('@/views/auth/ConfirmResetView.vue'),
          meta: { title: 'Confirm reset' }
        },
      ]
    }
  ]
})

// RouteGuard
router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore()

  if (!authStore.$state.isAuthenticated && authStore.$state.accessToken) {
    // Verify token if there is any
    await authStore.verifyToken()
      .catch(err => {
        // If error will be redirected to login
        return next({ path: '/auth/login' })
      })
  }

  if (authStore.$state.isAuthenticated && to.path.startsWith('/auth')) {
    if (from.path === ROOT_ROUTE) {
      // If same path as root, don't do anything
      return next(false)
    }
    // Browser with access token cannot go to auth pages
    return next({ path: ROOT_ROUTE })
  } else if (!authStore.$state.isAuthenticated && to.path.startsWith('/user')) {
    // Browser without access token cannot go to users pages
    return next({ path: '/auth/login', query: { redirectTo: to.path }})
  }

  return next()
})

router.afterEach((to, from, failure) => {
  if (to.meta.title && failure?.from.path !== ROOT_ROUTE) {
    // Only update page title if no failure
    document.title = `Bazaar - ${ to.meta.title }`
  }
})

export default router
