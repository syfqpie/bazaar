<template>
    <div class="w-full py-8 px-4 sm:px-12">
        <div>
            <img
                src="@/assets/img/default/trolley.png"
                class="mx-auto h-12 w-auto"
                alt="Bazaar" />

            <h2
                class="mt-6 text-center text-3xl
                font-bold tracking-tight text-gray-900">
                Sign in to your account
            </h2>
        </div>

        <form @submit.prevent>
            <div class="mt-8 max-w-md">
                <div class="grid grid-cols-1 gap-3">
                    <div>
                        <label class="text-sm text-gray-700">Email</label>
                        <TheInput
                            type="email"
                            placeholder="Enter your email"
                            v-model="loginForm.username"
                            :class="{
                                'border-red-400': v$.username.$dirty &&
                                                    v$.username.$invalid 
                                
                            }"
                            @blur="v$.username.$touch" />
                        <p
                            v-for="error of v$.username.$errors"
                            :key="error.$uid"
                            class="mt-2 text-xs text-red-600 dark:text-red-500">
                            {{ error.$message }}
                        </p>
                    </div>

                    <div>
                        <label class="text-sm text-gray-700">Password</label>
                        <TheInput
                            type="password"
                            placeholder="Enter your password"
                            v-model="loginForm.password"
                            :class="{
                                'border-red-400': v$.password.$dirty &&
                                                    v$.password.$invalid 
                                
                            }"
                            @blur="v$.password.$touch" />

                        <p
                            v-for="error of v$.password.$errors"
                            :key="error.$uid"
                            class="mt-2 text-xs text-red-600 dark:text-red-500">
                            {{ error.$message }}
                        </p>
                    </div>

                    <div>
                        <TheButton 
                            @click="login()"
                            :size="'lg'"
                            :is-full="true"
                            :disabled="isLoading || v$.$invalid">
                            <span v-if="!isLoading">
                                Sign in
                            </span>
                            <span v-else>
                                <i class="fa-solid fa-circle-notch animate-spin"></i>
                                Loading
                            </span>
                        </TheButton>
                    </div>

                    <div class="mt-2 mb-1 justify-self-center text-sm">
                        <p>or</p>
                    </div>

                    <div class="flex flex-col">
                        <div class="text-center">
                            <p class="text-sm text-gray-500">
                                Don't have an account?
                                <router-link
                                    :to="{ path: '/auth/registration/customer' }"
                                    class="font-medium 
                                    text-indigo-500 hover:text-indigo-600">
                                    Sign up
                                </router-link>
                            </p>
                        </div>

                        <div class="text-center">
                            <p class="text-sm text-gray-500">
                                Forgot your password?
                                <router-link
                                    :to="{ path: '/auth/reset' }"
                                    class="font-medium 
                                    text-indigo-500 hover:text-indigo-600">
                                    Reset
                                </router-link>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </form>
    </div>
</template>

<script lang="ts">
import { computed, defineComponent, onMounted, ref } from 'vue'

import type { LoginInput } from '@/common/models/auth.model'
import TheButton from '@/components/basics/TheButton.vue'
import TheInput from '@/components/basics/TheInput.vue'
import router from '@/router'
import { useAuthStore } from '@/stores'

import useVuelidate from '@vuelidate/core'
import { email, helpers, minLength, required } from '@vuelidate/validators'
import { useToast } from 'vue-toastification'
import { UserType } from '@/common/models/user.model'

export default defineComponent({
  name: 'TheLogin',
  setup() {
    // Form
    const loginForm = ref<LoginInput>({
        username: null,
        password: null
    })
    const validation = computed(() => ({
        username: { 
            required: helpers.withMessage(
                'Email is required',
                required
            ),
            email: helpers.withMessage(
                'Valid email is required',
                email
            )
        },
        password: { 
            required: helpers.withMessage(
                'Password is required',
                required
            ),
            minLength: helpers.withMessage(
                'Min length is 8 characters',
                minLength(8)
            )
        }
    }))
    const v$ = useVuelidate(validation, loginForm.value)

    // Checkers
    const isLoading = ref<boolean>(false)

    // Services
    const authStore = useAuthStore()
    const toast = useToast()

    onMounted(() => {
        // console.log('Mounted TheLogin')
    })

    /**
     * Make http request to API to login
     */
    const login = () => {
        isLoading.value = true

        return authStore.login(loginForm.value)
            .then(data => {
                isLoading.value = false

                // Success toastr
                toast.success('Success. Redirecting...')
                
                // Navigate home
                const nextRoute = router.currentRoute.value.query['redirectTo'] ?
                    String(router.currentRoute.value.query['redirectTo']) :
                    authStore.$state.userType === UserType.Vendor ?
                    '/vendor/products/add' :
                    '/home'
                
                router.push({ path: nextRoute })
            })
            .catch(err => {
                isLoading.value = false
                
                // If username / password error
                if (err['status'] === 400 && 'nonFieldErrors' in err['data']) {
                    toast.error(err['data']['nonFieldErrors'][0])
                }
            })
    }

    return {
        loginForm,
        login,
        v$,
        isLoading
    }
  },
  components: {
    TheButton,
    TheInput
  }
})
</script>
