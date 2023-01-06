export const VendorRoute = [
    {
        path: 'products',
        name: 'vendorProducts',
        children: [
            {
                path: 'list',
                name: 'vendorProductList',
                component: () => import('@/views/vendor/ProductList.vue')
            },
            {
                path: ':id/details',
                name: 'vendorProductDetails',
                component: () => import('@/views/vendor/ProductDetails.vue')
            },
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