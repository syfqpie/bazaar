<template>
    <div class="w-full py-8 px-4 sm:px-12">
        <div>
            <img alt="Bazaar"
                class="mx-auto h-12 w-auto"
                src="@/assets/img/default/trolley.png" />

            <h2 class="mt-6 text-center text-3xl
                font-bold tracking-tight text-gray-900">
                Resend verification email
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
                            focus:shadow-outline focus:ring-gray-500
                            focus:ring-1"
                            v-model="resendForm.email" />
                    </div>

                    <div>
                        <button class="mt-1 group relative flex w-full justify-center
                            rounded-lg border border-transparent bg-green-300
                            p-2.5 text-white enabled:bg-green-400
                            focus:outline-none focus:ring-2 focus:ring-green-200
                            font-medium text-sm focus:hover:enabled:bg-green-500"
                            v-on:click="resend()"
                            :disabled="isLoading || v$.$invalid">
                            Resend email
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
import { onMounted, defineComponent, ref } from 'vue'

import type { EmailOnlyInput } from '@/common/models/auth.model'
import { useAuthStore } from '@/stores'

import { email, helpers, required } from '@vuelidate/validators'
import { useToast } from 'vue-toastification'
import useVuelidate from '@vuelidate/core'

export default defineComponent({
  name: 'ResendVerification',
  setup() {
    // Form
    const resendForm = ref<EmailOnlyInput>({
        email: null,
    })
    const validation = {
        email: { 
            required: helpers.withMessage(
                'Email is required',
                required
            ),
            email: helpers.withMessage(
                'Valid email is required',
                email
            )
        }
    }
    const v$ = useVuelidate(validation, resendForm.value)

    // Services
    const authStore = useAuthStore()
    const toast = useToast()

    // Checkers
    const isLoading = ref<boolean>(false)

    onMounted(() => {
        // console.log('Mounted ResendVerification')
    })

    const resend = () => {
        isLoading.value = true

        return authStore.resendVerification(resendForm.value)
            .then(data => {
                isLoading.value = false
                
                // Success toastr
                toast.success('Verification email has been resent')
            })
            .catch(() => {
                isLoading.value = false
            })
    }

    return {
        resendForm,
        resend,
        v$,
        isLoading
    }
  }
})
</script>
