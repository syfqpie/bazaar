<template>
    <div class="w-full py-8 px-4 sm:px-12">
        <div>
            <img alt="Bazaar"
                class="mx-auto h-12 w-auto"
                src="@/assets/img/default/trolley.png" />

            <h2 class="mt-6 text-center text-3xl
                font-bold tracking-tight text-gray-900">
                Sign in to your account
            </h2>
        </div>

        <form @submit.prevent>
            <div class="mt-8 max-w-md">
                <div class="grid grid-cols-1 gap-3">
                    <div>
                        <label class="text-sm text-gray-700">Email</label>
                        <input type="email"
                            class="mt-1 block w-full rounded-lg bg-gray-50
                            border border-gray-300 text-gray-900
                            text-sm p-2.5 focus:outline-none
                            focus:shadow-outline"
                            placeholder="Enter your email"
                            :class="{
                                'border-red-400': v$.username.$dirty &&
                                                    v$.username.$invalid 
                                
                            }"
                            v-model="loginForm.username"
                            @blur="v$.username.$touch" />
                        <p v-for="error of v$.username.$errors"
                            :key="error.$uid"
                            class="mt-2 text-xs text-red-600 dark:text-red-500">
                            {{ error.$message }}
                        </p>
                    </div>

                    <div>
                        <label class="text-sm text-gray-700">Password</label>
                        <input type="password"
                            class="mt-1 block w-full rounded-lg bg-gray-50
                            border border-gray-300 text-gray-900
                            text-sm p-2.5 focus:outline-none
                            focus:shadow-outline"
                            placeholder="Enter your password"
                            :class="{
                                'border-red-400': v$.password.$dirty &&
                                                    v$.password.$invalid 
                                
                            }"
                            v-model="loginForm.password"
                            @blur="v$.password.$touch" />

                        <p v-for="error of v$.password.$errors"
                            :key="error.$uid"
                            class="mt-2 text-xs text-red-600 dark:text-red-500">
                            {{ error.$message }}
                        </p>
                    </div>

                    <div>
                        <button class="mt-1 group relative flex w-full justify-center
                            rounded-lg p-2.5 border border-transparent outline-none
                            font-medium text-sm shadow-none border-solid text-white 
                            bg-green-400 border-green-400  active:bg-green-500 
                            active:border-green-500 hover:shadow-md disabled:bg-green-300
                            disabled:border-green-300 disabled:shadow-none
                            disabled:cursor-not-allowed focus:outline-none focus:ring-2
                            focus:ring-green-200 focus:hover:enabled:bg-green-500
                            transition-all duration-150 ease-in-out"
                            v-on:click="login()"
                            :disabled="isLoading || v$.$invalid">
                            Sign in
                        </button>
                    </div>

                    <div class="mt-2 mb-1 justify-self-center text-sm">
                        <p>or</p>
                    </div>

                    <div class="flex flex-col">
                        <div class="text-center">
                            <p class="text-sm text-gray-500">
                                Don't have an account?
                                <router-link :to="{ path: '/auth/registration/customer' }"
                                    class="font-medium 
                                    text-green-400 hover:text-green-300">
                                    Sign up
                                </router-link>
                            </p>
                        </div>

                        <div class="text-center">
                            <p class="text-sm text-gray-500">
                                Forgot your password?
                                <router-link :to="{ path: '/auth/reset' }"
                                    class="font-medium 
                                    text-green-400 hover:text-green-300">
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
import router from '@/router'
import { useAuthStore } from '@/stores'

import { email, helpers, minLength, required } from '@vuelidate/validators'
import { useToast } from 'vue-toastification'
import useVuelidate from '@vuelidate/core'

export default defineComponent({
  name: 'Login',
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

    // Services
    const authStore = useAuthStore()
    const toast = useToast()

    // Checkers
    const isLoading = ref<boolean>(false)

    onMounted(() => {
        // console.log('Mounted Login')
    })

    // Login
    const login = () => {
        isLoading.value = true

        return authStore.login(loginForm.value)
            .then(data => {
                isLoading.value = false

                // Success toastr
                toast.success('Success. Redirecting to /home')
                
                // Navigate home
                router.push({ path: '/home' })
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
  }
})
</script>
