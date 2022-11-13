<template>
    <div class="w-full">
        <div
            class="p-4 sm:p-6 md:p-8 w-full bg-white
            rounded-lg border border-gray-200 shadow-sm">
            <h5 class="mb-0 text-base font-semibold text-gray-900 md:text-xl">
                Change password
            </h5>
            <p class="text-sm font-normal text-gray-500 dark:text-gray-400 mb-3">
                For your account's security, do not share your password with anyone else
            </p>

            <div class="grid grid-cols-1 lg:grid-cols-2">
                <form @submit.prevent>
                    <div class="mb-3">
                        <label class="text-sm text-gray-700">
                            Current password
                        </label>
                        <TheInput
                            type="password"
                            placeholder="Enter your old password"
                            v-model="changeForm.oldPassword"
                            :class="{
                                'border-red-400': v$.oldPassword.$dirty &&
                                                    v$.oldPassword.$invalid 
                                
                            }"
                            @blur="v$.oldPassword.$touch" />
                        <p
                            v-for="error of v$.oldPassword.$errors"
                            :key="error.$uid"
                            class="mt-2 text-xs text-red-600 dark:text-red-500">
                            {{ error.$message }}
                        </p>
                    </div>

                    <div class="mb-3">
                        <label class="text-sm text-gray-700">
                            New password
                        </label>
                        <TheInput
                            type="password"
                            placeholder="Enter your new password"
                            v-model="changeForm.newPassword1"
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

                    <div class="mb-3">
                        <label class="text-sm text-gray-700">
                            Confirm new password
                        </label>
                        <TheInput
                            type="password"
                            placeholder="Confirm your new password"
                            v-model="changeForm.newPassword2"
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

                    <TheButton
                        :disabled="v$.$invalid"
                        @click="changePassword()">
                        <span v-if="!isLoading">
                            Confirm
                        </span>
                        <span v-else>
                            <i class="fa-solid fa-circle-notch animate-spin"></i>
                            Loading
                        </span>
                    </TheButton>
                </form>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { computed, defineComponent, onMounted, ref  } from 'vue'
import { useRoute } from 'vue-router'

import TheButton from '@/components/basics/TheButton.vue'
import TheInput from '@/components/basics/TheInput.vue'
import type { ChangePasswordInput } from '@/common/models/auth.model'
import { passwordRegexMedium } from '@/common/helpers'
import { useAuthStore } from '@/stores'

import useVuelidate from '@vuelidate/core'
import { helpers, required, sameAs } from '@vuelidate/validators'
import { useToast } from 'vue-toastification'

export default defineComponent({
    name: 'AccountPasswordChange',
    setup() {
        // Form
        const changeForm = ref<ChangePasswordInput>({
            oldPassword: null,
            newPassword1: null,
            newPassword2: null
        })
        const validation = computed(() => ({
            oldPassword: { 
                required: helpers.withMessage(
                    'Old password is required',
                    required
                ),
                strength: helpers.withMessage(
                    'Minimum eight characters, at least one any case letter\
                    and one digit',
                    passwordRegexMedium
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
                    sameAs(changeForm.value.newPassword1)
                )
            }
        })) 
        const v$ = useVuelidate(validation, changeForm.value)

        // Checker
        const isLoading = ref(false)

        // Services
        const authStore = useAuthStore()
        const toast = useToast()
        const route = useRoute()

        onMounted(() => {
            // console.log('Mounted ChangePassword')
        })

        /**
         * Make http request to API to change password
         */
        const changePassword = () => {
            isLoading.value = true

            return authStore.changePassword(changeForm.value)
            .then(data => {
                isLoading.value = false

                // Success toastr
                toast.success('New password saved!')
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
            changeForm,
            v$,
            validation,
            isLoading,
            changePassword
        }
    },
    components: {
        TheButton,
        TheInput
    }
})
</script>