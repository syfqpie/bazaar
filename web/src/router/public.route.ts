export const PublicRoute = [
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
    }
]