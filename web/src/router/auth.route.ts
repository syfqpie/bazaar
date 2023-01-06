export const AuthRoute = [
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