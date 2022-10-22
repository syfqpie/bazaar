import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';

import LayoutPublic from '@/layouts/LayoutPublic.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'public',
    component: LayoutPublic,
    children: [
      {
        path: '/',
        name: 'home',
        component: () => import('../views/HomeView.vue')
      }
    ]
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
