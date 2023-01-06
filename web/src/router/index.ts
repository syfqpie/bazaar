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
      component: () => import('@/layouts/LayoutPublic.vue'),
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
          component: () => import('@/views/UserAccount.vue'),
          meta: { requiresAuth: true },
          children: [
            {
              path: 'account',
              name: 'userAccount',
              children: [
                {
                  path: 'profile',
                  name: 'userAccountProfile',
                  component: () => import('@/views/account/AccountProfile.vue'),
                  meta: { title: 'Profile' }
                },
                {
                  path: 'address',
                  name: 'userAccountAddress',
                  component: () => import('@/views/account/AccountAddress.vue'),
                  meta: { title: 'Address' }
                },
                {
                  path: 'change-password',
                  name: 'userAccountPasswordChange',
                  component: () => import('@/views/account/AccountPasswordChange.vue'),
                  meta: { title: 'Change password' }
                }
              ]
            },
            {
              path: 'system',
              name: 'userSystem',
              component: () => import('@/views/TheSystem.vue'),
              meta: { title: 'System' }
            }
          ]
        },
        {
          path: 'product-listing',
          name: 'productListing',
          component: () => import('@/views/ProductListingView.vue'),
          meta: { title: 'Product Listing' }
        }
      ]
    },
    {
      path: '/vendor',
      name: 'vendor',
      component: () => import('@/layouts/LayoutVendor.vue'),
      children: [
        {
          path: 'products',
          name: 'vendorProducts',
          children: [
            {
              path: 'add',
              name: 'vendorProductAdd',
              component: () => import('@/views/vendor/AddProduct.vue')
            }
          ]
        },
        {
          path: 'user',
          name: 'vendorUser',
          component: () => import('@/views/UserAccount.vue'),
          meta: { requiresAuth: true },
          children: [
            {
              path: 'account',
              name: 'vendorUserAccount',
              children: [
                {
                  path: 'profile',
                  name: 'vendorUserAccountProfile',
                  component: () => import('@/views/account/AccountProfile.vue'),
                  meta: { title: 'Profile' }
                },
                {
                  path: 'address',
                  name: 'vendorUserAccountAddress',
                  component: () => import('@/views/account/AccountAddress.vue'),
                  meta: { title: 'Address' }
                },
                {
                  path: 'change-password',
                  name: 'vendorUserAccountPasswordChange',
                  component: () => import('@/views/account/AccountPasswordChange.vue'),
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
      component: () => import('@/layouts/LayoutAuth.vue'),
      children: [
        {
          path: 'login',
          name: 'login',
          component: () => import('@/views/auth/TheLogin.vue'),
          meta: { title: 'Login' }
        },
        {
          path: 'registration/customer',
          name: 'registerCustomer',
          component: () => import('@/views/auth/RegisterCustomer.vue'),
          meta: { title: 'Customer registration' }
        },
        {
          path: 'registration/vendor',
          name: 'registerVendor',
          component: () => import('@/views/auth/RegisterVendor.vue'),
          meta: { title: 'Vendor registration' }
        },
        {
          path: 'registration/resend-verification',
          name: 'registerResendEmail',
          component: () => import('@/views/auth/RegisterResendEmail.vue'),
          meta: { title: 'Resend verification' }
        },
        {
          path: 'registration/verify',
          name: 'registerVerify',
          component: () => import('@/views/auth/RegisterVerify.vue'),
          meta: { title: 'Verify' }
        },
        {
          path: 'reset',
          name: 'resetRequest',
          component: () => import('@/views/auth/ResetRequest.vue'),
          meta: { title: 'Reset' }
        },
        {
          path: 'reset/confirm',
          name: 'resetConfirmation',
          component: () => import('@/views/auth/ResetConfirmation.vue'),
          meta: { title: 'Confirm reset' }
        },
      ]
    }
  ]
})

// RouteGuard
/**
 * there is an issue here
 * 
 * sometimes when login or logout
 * the url changed but somehow the page
 * doesnt reload
 */
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
