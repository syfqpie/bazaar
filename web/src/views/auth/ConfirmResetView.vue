<template>
    <div class="w-full py-8 px-12">
        <div>
            <img alt="Bazaar"
                class="mx-auto h-12 w-auto"
                src="@/assets/img/default/trolley.png" />

            <h2 class="mt-6 text-center text-3xl
                font-bold tracking-tight text-gray-900">
                Reset your password with Bazaar
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
                            v-model="resetForm.newPassword1" />
                    </div>

                    <div>
                        <label class="text-gray-700">Confirm new password</label>
                        <input type="password"
                            class="mt-1 block w-full rounded-md bg-gray-100
                            border-transparent px-3 py-2 focus:outline-none
                            focus:shadow-outline focus:ring-gray-500
                            focus:ring-1 focus:bg-white"
                            placeholder="Confirm your new password"
                            v-model="resetForm.newPassword2" />
                    </div>

                    <div>
                        <button class="mt-1 group relative flex w-full justify-center
                            rounded-md border border-transparent bg-green-300
                            px-3 py-2 text-white enabled:bg-green-400
                            focus:outline-none focus:ring-2 focus:ring-green-200"
                            v-on:click="confirmReset()"
                            :disabled="isLoading || v$.$invalid">
                            Reset password
                        </button>
                    </div>
                </div>
            </div>
        </form>
    </div>
</template>

<script lang="ts">
import { onMounted, defineComponent, ref } from 'vue'

import type { ResetPasswordInput } from '@/common/models/auth.model'
import { useAuthStore } from '@/stores'

import { helpers, required } from '@vuelidate/validators'
import { useToast } from 'vue-toastification'
import useVuelidate from '@vuelidate/core'
import { useRoute } from 'vue-router'

const UID_KEY = 'uid'
const TOKEN_KEY = 'key'

export default defineComponent({
  name: 'ConfirmReset',
  setup() {
    // Form
    const resetForm = ref<ResetPasswordInput>({
        uid: null,
        token: null,
        newPassword1: null,
        newPassword2: null
    })
    const validation = {
        uid: { 
            required: helpers.withMessage(
                'UID is required',
                required
            )
        },
        token: { 
            required: helpers.withMessage(
                'Token is required',
                required
            )
        },
        newPassword1: { 
            required: helpers.withMessage(
                'Password is required',
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
    const v$ = useVuelidate(validation, resetForm.value)

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
        if (UID_KEY in route.query && TOKEN_KEY in route.query) {
            // Append query parameter value to form
            resetForm.value.uid = Number(route.query[UID_KEY])
            resetForm.value.token = String(route.query[TOKEN_KEY])
        } else {
            // Warning
            toast.warning('Query params not found')
        }
    }

    const confirmReset = () => {
        isLoading.value = true

        return authStore.resetPassword(resetForm.value)
            .then(data => {
                isLoading.value = false
                
                // Success toastr
                // toast.success('Password reset email has been sent')
            })
            .catch(() => {
                isLoading.value = false
            })
    }

    return {
        resetForm,
        confirmReset,
        v$,
        isLoading
    }
  }
})
</script>
