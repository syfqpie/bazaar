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
          component: () => import('../views/LoginView.vue')
        }
      ]
    }
  ]
})

export default router
