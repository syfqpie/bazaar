import { createRouter, createWebHistory } from 'vue-router'

import { useAuthStore } from '@/stores'
import { AuthRoute } from './auth.route'
import { PublicRoute } from './public.route'
import { VendorRoute } from './vendor.router'

const ROOT_ROUTE = '/home'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/home',
      name: 'public',
      component: () => import('@/layouts/LayoutPublic.vue'),
      children: PublicRoute
    },
    {
      path: '/vendor',
      name: 'vendor',
      component: () => import('@/layouts/LayoutVendor.vue'),
      children: VendorRoute
    },
    {
      path: '/auth',
      name: 'authentication',
      component: () => import('@/layouts/LayoutAuth.vue'),
      children: AuthRoute
    }
  ]
})

/**
 * RouteGuard
 * 
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
