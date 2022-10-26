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
                        <label class="text-sm text-gray-700">New password</label>
                        <input type="password"
                            class="mt-1 block w-full rounded-lg bg-gray-50
                            border border-gray-300 text-gray-900
                            text-sm p-2.5 focus:outline-none
                            focus:shadow-outline"
                            placeholder="Enter your new password"
                            :class="{
                                'border-red-400': v$.newPassword1.$dirty &&
                                                    v$.newPassword1.$invalid 
                                
                            }"
                            v-model="resetForm.newPassword1"
                            @blur="v$.newPassword1.$touch" />
                        
                        <p v-for="error of v$.newPassword1.$errors"
                            :key="error.$uid"
                            class="mt-2 text-xs text-red-600 dark:text-red-500">
                            {{ error.$message }}
                        </p>
                    </div>

                    <div>
                        <label class="text-sm text-gray-700">Confirm new password</label>
                        <input type="password"
                            class="mt-1 block w-full rounded-lg bg-gray-50
                            border border-gray-300 text-gray-900
                            text-sm p-2.5 focus:outline-none
                            focus:shadow-outline"
                            placeholder="Confirm your new password"
                            :class="{
                                'border-red-400': v$.newPassword2.$dirty &&
                                                    v$.newPassword2.$invalid 
                                
                            }"
                            v-model="resetForm.newPassword2"
                            @blur="v$.newPassword2.$touch" />

                        <p v-for="error of v$.newPassword2.$errors"
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
import { computed, defineComponent, onMounted, ref } from 'vue'

import type { ResetPasswordInput } from '@/common/models/auth.model'
import { passwordRegexMedium } from '@/common/helpers'
import router from '@/router'
import { useAuthStore } from '@/stores'

import { helpers, required, sameAs } from '@vuelidate/validators'
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
    const validation = computed(() => ({
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
                sameAs(resetForm.value.newPassword1)
            )
        }
    }))
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
                toast.success('Password reset been reset. Redirecting to /login')

                // Navigate home
                router.push({ path: '/auth/login' })
            })
            .catch((err) => {
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
        resetForm,
        confirmReset,
        v$,
        isLoading
    }
  }
})
</script>
