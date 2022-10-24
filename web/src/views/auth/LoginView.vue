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
                        <label class="text-gray-700">Email</label>
                        <input type="email"
                            class="mt-1 block w-full rounded-md bg-gray-100
                            border-transparent px-3 py-2 focus:outline-none
                            focus:shadow-outline focus:ring-gray-500
                            focus:ring-1 focus:bg-white"
                            placeholder="Enter your email"
                            v-model="loginForm.username" />
                    </div>

                    <div>
                        <label class="text-gray-700">Password</label>
                        <input type="password"
                            class="mt-1 block w-full rounded-md bg-gray-100
                            border-transparent px-3 py-2 focus:outline-none
                            focus:shadow-outline focus:ring-gray-500
                            focus:ring-1 focus:bg-white"
                            placeholder="Enter your password"
                            v-model="loginForm.password" />
                    </div>

                    <div>
                        <button class="mt-1 group relative flex w-full justify-center
                            rounded-md border border-transparent bg-green-300
                            px-3 py-2 text-white enabled:bg-green-400
                            focus:outline-none focus:ring-2 focus:ring-green-200"
                            v-on:click="login()"
                            :disabled="isLoading || v$.$invalid">
                            Sign in
                        </button>
                    </div>

                    <div class="mt-2 mb-1 justify-self-center text-sm">
                        <p>or</p>
                    </div>

                    <div class="flex flex-col">
                        <div class="text-sm text-center">
                            <p class="text-gray-500">
                                Don't have an account?
                                <router-link :to="{ name: 'register' }"
                                    class="font-medium 
                                    text-green-400 hover:text-green-300">
                                    Sign up
                                </router-link>
                            </p>
                        </div>

                        <div class="text-sm text-center">
                            <p class="text-gray-500">
                                Forgot your password?
                                <router-link :to="{ name: 'reset' }"
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
import { onMounted, defineComponent, ref } from 'vue'

import type { LoginInput } from '@/common/models/auth.model'
import router from '@/router'
import { useAuthStore } from '@/stores'

import { email, helpers, required } from '@vuelidate/validators'
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
    const validation = {
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
            )
        }
    }
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
                router.push({ name: 'home' })
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
