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
                Reset your password with Bazaar
            </h2>
        </div>

        <form @submit.prevent>
            <div class="mt-8 max-w-md">
                <div class="grid grid-cols-1 gap-3">
                    <div>
                        <label class="text-sm text-gray-700">New password</label>
                        <TheInput
                            type="password"
                            placeholder="Enter your new password"
                            v-model="resetForm.newPassword1"
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
                        <TheInput
                            type="password"
                            placeholder="Confirm your new password"
                            v-model="resetForm.newPassword2"
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
                        <TheButton 
                            @click="confirmReset()"
                            :size="'lg'"
                            :is-full="true"
                            :disabled="isLoading || v$.$invalid">
                            <span v-if="!isLoading">
                                Reset password
                            </span>
                            <span v-else>
                                <i class="fa-solid fa-circle-notch animate-spin"></i>
                                Loading
                            </span>
                        </TheButton>
                    </div>
                </div>
            </div>
        </form>
    </div>
</template>

<script lang="ts">
import { computed, defineComponent, onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import type { ResetPasswordInput } from '@/common/models/auth.model'
import { passwordRegexMedium } from '@/common/helpers'
import TheButton from '@/components/basics/TheButton.vue'
import TheInput from '@/components/basics/TheInput.vue'
import router from '@/router'
import { useAuthStore } from '@/stores'

import useVuelidate from '@vuelidate/core'
import { helpers, required, sameAs } from '@vuelidate/validators'
import { useToast } from 'vue-toastification'

const UID_KEY = 'uid'
const TOKEN_KEY = 'key'

export default defineComponent({
  name: 'ResetConfirmation',
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
     * This component requires uid and key params
     */
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

    /**
     * Make http request to API to confirm reset password
     */
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
  },
  components: {
    TheButton,
    TheInput
  }
})
</script>
