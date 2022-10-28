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
                Resend verification email
            </h2>
        </div>

        <form @submit.prevent>
            <div class="mt-8 max-w-md">
                <div class="grid grid-cols-1 gap-3">
                    <div>
                        <label class="text-sm text-gray-700">Email</label>
                        <input
                            type="email"
                            class="mt-1 block w-full rounded-lg bg-gray-50
                            border border-gray-300 text-gray-900
                            text-sm p-2.5 focus:outline-none
                            focus:shadow-outline"
                            placeholder="Enter your email"
                            v-model="resendForm.email"
                            :class="{
                                'border-red-400': v$.email.$dirty &&
                                                    v$.email.$invalid 
                                
                            }"
                            @blur="v$.email.$touch" />
                        <p
                            v-for="error of v$.email.$errors"
                            :key="error.$uid"
                            class="mt-2 text-xs text-red-600 dark:text-red-500">
                            {{ error.$message }}
                        </p>
                    </div>

                    <div>
                        <button
                            class="mt-1 group relative flex w-full justify-center
                            rounded-lg p-2.5 border border-transparent outline-none
                            font-medium text-sm shadow-none border-solid text-white 
                            bg-green-400 border-green-400  active:bg-green-500 
                            active:border-green-500 hover:shadow-md disabled:bg-green-300
                            disabled:border-green-300 disabled:shadow-none
                            disabled:cursor-not-allowed focus:outline-none focus:ring-2
                            focus:ring-green-200 focus:hover:enabled:bg-green-500
                            transition-all duration-150 ease-in-out"
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
                                <router-link
                                    :to="{ path: '/auth/registration/customer' }"
                                    class="font-medium 
                                    text-green-400 hover:text-green-300">
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

import type { EmailOnlyInput } from '@/common/models/auth.model'
import { useAuthStore } from '@/stores'

import useVuelidate from '@vuelidate/core'
import { email, helpers, required } from '@vuelidate/validators'
import { useToast } from 'vue-toastification'

const VERIFIED_MESSAGE = 'This email address is verified'

export default defineComponent({
  name: 'RegisterResendEmail',
  setup() {
    // Form
    const resendForm = ref<EmailOnlyInput>({
        email: null,
    })
    const validation = computed(() => ({
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
    }))
    const v$ = useVuelidate(validation, resendForm.value)

    // Checkers
    const isLoading = ref<boolean>(false)

    // Services
    const authStore = useAuthStore()
    const toast = useToast()

    onMounted(() => {
        // console.log('Mounted RegisterResendEmail')
    })

    /**
     * Make http request to API to resend verification email
     */
    const resend = () => {
        isLoading.value = true

        return authStore.resendVerification(resendForm.value)
            .then(data => {
                isLoading.value = false
                
                // Success toastr
                toast.success('Verification email has been resent')
            })
            .catch((err) => {
                isLoading.value = false

                if (err['status'] === 400 && 'detail' in err['data'] &&
                    err['data']['detail'] === VERIFIED_MESSAGE) {
                    toast.info(VERIFIED_MESSAGE)
                }
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