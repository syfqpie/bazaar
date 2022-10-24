<template>
    <div class="w-full py-8 px-12">
        <div>
            <img alt="Bazaar"
                class="mx-auto h-12 w-auto"
                src="@/assets/img/default/trolley.png" />

            <h2 class="mt-6 text-center text-3xl
                font-bold tracking-tight text-gray-900">
                Verify your account with Bazaar
            </h2>
        </div>

        <form @submit.prevent>
            <div class="mt-8 max-w-md">
                <div class="grid grid-cols-1 gap-3">
                    <div>
                        <label class="text-gray-700">New password</label>
                        <input type="password"
                            class="mt-1 block w-full rounded-md bg-gray-100
                            border-transparent px-3 py-2 focus:outline-none
                            focus:shadow-outline focus:ring-gray-500
                            focus:ring-1 focus:bg-white"
                            placeholder="Enter your new password"
                            v-model="verifyForm.newPassword1" />
                    </div>

                    <div>
                        <label class="text-gray-700">Confirm new password</label>
                        <input type="password"
                            class="mt-1 block w-full rounded-md bg-gray-100
                            border-transparent px-3 py-2 focus:outline-none
                            focus:shadow-outline focus:ring-gray-500
                            focus:ring-1 focus:bg-white"
                            placeholder="Enter your confirm new password"
                            v-model="verifyForm.newPassword2" />
                    </div>

                    <div>
                        <button class="mt-1 group relative flex w-full justify-center
                            rounded-md border border-transparent bg-green-300
                            px-3 py-2 text-white enabled:bg-green-400
                            focus:outline-none focus:ring-2 focus:ring-green-200"
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
import { onMounted, defineComponent, ref } from 'vue'

import type { VerifyAccountInput } from '@/common/models/auth.model'
import router from '@/router'
import { useAuthStore } from '@/stores'

import { helpers, required } from '@vuelidate/validators'
import { useToast } from 'vue-toastification'
import useVuelidate from '@vuelidate/core'
import { useRoute } from 'vue-router'

const TOKEN_KEY = 'key'

export default defineComponent({
    name: 'VerifyAccount',
    setup() {
        // Form
        const verifyForm = ref<VerifyAccountInput>({
            key: null,
            newPassword1: null,
            newPassword2: null
        })
        const validation = {
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
                )
            },
            newPassword2: { 
                required: helpers.withMessage(
                    'Confirm new password is required',
                    required
                )
            }
        }
        const v$ = useVuelidate(validation, verifyForm.value)

        // Services
        const authStore = useAuthStore()
        const toast = useToast()
        const route = useRoute()

        // Checkers
        const isLoading = ref<boolean>(false)

        onMounted(() => {
            queryParamChecker()
        })

        const queryParamChecker = () => {
            if (TOKEN_KEY in route.query) {
                // Append query parameter value to form
                verifyForm.value.key = String(route.query[TOKEN_KEY])
            } else {
                // Warning
                toast.warning('Query params not found')
            }
        }

        // Verify
        const verify = () => {
            isLoading.value = true

            return authStore.verifyAccount(verifyForm.value)
                .then(data => {
                    isLoading.value = false

                    // Success toastr
                    toast.success('Success. Redirecting to /login')
                    
                    // Navigate login
                    router.push({ name: 'login' })
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
