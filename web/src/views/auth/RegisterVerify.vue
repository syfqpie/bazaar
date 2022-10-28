<template>
    <div class="w-full py-8 px-12">
        <div>
            <img
                src="@/assets/img/default/trolley.png"
                class="mx-auto h-12 w-auto"
                alt="Bazaar" />

            <h2
                class="mt-6 text-center text-3xl
                font-bold tracking-tight text-gray-900">
                Verify your account with Bazaar
            </h2>
        </div>

        <form @submit.prevent>
            <div class="mt-8 max-w-md">
                <div class="grid grid-cols-1 gap-3">
                    <div>
                        <label class="text-sm text-gray-700">New password</label>
                        <input
                            type="password"
                            class="mt-1 block w-full rounded-lg bg-gray-50
                            border border-gray-300 text-gray-900
                            text-sm p-2.5 focus:outline-none
                            focus:shadow-outline"
                            placeholder="Enter your new password"
                            v-model="verifyForm.newPassword1"
                            :class="{
                                'border-red-400': v$.newPassword1.$dirty &&
                                                    v$.newPassword1.$invalid 
                                
                            }"
                            @blur="v$.newPassword1.$touch" />
                        <p
                            v-for="error of v$.newPassword1.$errors"
                            :key="error.$uid"
                            class="mt-2 text-xs text-red-600 dark:text-red-500">
                            {{ error.$message }}
                        </p>
                    </div>

                    <div>
                        <label class="text-sm text-gray-700">Confirm new password</label>
                        <input
                            type="password"
                            class="mt-1 block w-full rounded-lg bg-gray-50
                            border border-gray-300 text-gray-900
                            text-sm p-2.5 focus:outline-none
                            focus:shadow-outline"
                            placeholder="Enter your confirm new password"
                            v-model="verifyForm.newPassword2"
                            :class="{
                                'border-red-400': v$.newPassword2.$dirty &&
                                                    v$.newPassword2.$invalid 
                                
                            }"
                            @blur="v$.newPassword2.$touch" />
                        <p
                            v-for="error of v$.newPassword2.$errors"
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
                            v-on:click="verify()"
                            :disabled="isLoading || v$.$invalid">
                            Verify account
                        </button>
                    </div>
                </div>
            </div>
        </form>
    </div>
</template>

<script lang="ts">
import { onMounted, defineComponent, ref, computed } from 'vue'
import { useRoute } from 'vue-router'

import type { VerifyAccountInput } from '@/common/models/auth.model'
import { passwordRegexMedium } from '@/common/helpers'
import router from '@/router'
import { useAuthStore } from '@/stores'

import useVuelidate from '@vuelidate/core'
import { helpers, required, sameAs } from '@vuelidate/validators'
import { useToast } from 'vue-toastification'

const TOKEN_KEY = 'key'

export default defineComponent({
    name: 'RegisterVerify',
    setup() {
        // Form
        const verifyForm = ref<VerifyAccountInput>({
            key: null,
            newPassword1: null,
            newPassword2: null
        })
        const validation = computed(() => ({
            key: { 
                required: helpers.withMessage(
                    'Token is required',
                    required
                )
            },
            newPassword1: { 
                required: helpers.withMessage(
                    'New password is required',
                    required
                ),
                strength: helpers.withMessage(
                    'Minimum eight characters, at least one any case letter\
                    and one digit',
                    passwordRegexMedium
                )
            },
            newPassword2: { 
                required: helpers.withMessage(
                    'Confirm new password is required',
                    required
                ),
                sameAsNewPassword1: helpers.withMessage(
                    'New password does not match',
                    sameAs(verifyForm.value.newPassword1)
                )
            }
        }))
        const v$ = useVuelidate(validation, verifyForm.value)

        // Checkers
        const isLoading = ref<boolean>(false)

        // Services
        const authStore = useAuthStore()
        const toast = useToast()
        const route = useRoute()

        onMounted(() => {
            queryParamChecker()
        })

        /**
         * Check for any query parameters in path
         * 
         * This component requires key paramxw
         */
        const queryParamChecker = () => {
            if (TOKEN_KEY in route.query) {
                // Append query parameter value to form
                verifyForm.value.key = String(route.query[TOKEN_KEY])
            } else {
                // Warning
                toast.warning('Query params not found')
            }
        }

        /**
         * Make http request to API to verify account
         */
        const verify = () => {
            isLoading.value = true

            return authStore.verifyAccount(verifyForm.value)
                .then(data => {
                    isLoading.value = false

                    // Success toastr
                    toast.success('Success. Redirecting to /login')
                    
                    // Navigate login
                    router.push({ path: '/auth/login' })
                })
                .catch(err => {
                    isLoading.value = false
                    
                    if (err['status'] === 400 && 'nonFieldErrors' in err['data']) {
                        // Non field errors
                        toast.error(err['data']['nonFieldErrors'][0])
                    } else if (err['status'] === 400 && 'nonFieldErrors' in err['data'] === false) {
                        // Field errors
                        for (var prop in err['data']) {
                            for (var i=0; i<err['data'][prop].length; i++)
                            toast.error(err['data'][prop][i])
                        }
                    }
                })
        }

        return {
            verifyForm,
            verify,
            v$,
            isLoading
        }
    }
})
</script>
