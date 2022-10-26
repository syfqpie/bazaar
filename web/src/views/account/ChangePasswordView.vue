<template>
    <div class="w-full">
        <div class="p-4 sm:p-6 md:p-8 w-full bg-white
            rounded-lg border border-gray-200 shadow-sm">
            <h5 class="mb-0 text-base font-semibold text-gray-900 md:text-xl">
                Change password
            </h5>
            <p class="text-sm font-normal text-gray-500 dark:text-gray-400 mb-3">
                For your account's security, do not share your password with anyone else
            </p>

            <div class="grid grid-cols-2">
                <form @submit.prevent>
                    <div class="mb-3">
                        <label class="text-sm text-gray-700">
                            Current password
                        </label>
                        <input type="password"
                            @blur="v$.oldPassword.$touch"
                            class="mt-1 block w-full rounded-lg bg-gray-50
                            border border-gray-300 text-gray-900
                            text-sm p-2.5 focus:outline-none
                            focus:shadow-outline"
                            :class="{
                                'border-red-400': v$.oldPassword.$dirty &&
                                                    v$.oldPassword.$invalid 
                                
                            }"
                            v-model="changeForm.oldPassword" />
                        <p v-for="error of v$.oldPassword.$errors"
                            :key="error.$uid"
                            class="mt-2 text-xs text-red-600 dark:text-red-500">
                            {{ error.$message }}
                        </p>
                    </div>

                    <div class="mb-3">
                        <label class="text-sm text-gray-700">
                            New password
                        </label>
                        <input type="password"
                            @blur="v$.newPassword1.$touch"
                            class="mt-1 block w-full rounded-lg bg-gray-50
                            border border-gray-300 text-gray-900
                            text-sm p-2.5 focus:outline-none
                            focus:shadow-outline"
                            :class="{
                                'border-red-400': v$.newPassword1.$dirty &&
                                                    v$.newPassword1.$invalid 
                                
                            }"
                            v-model="changeForm.newPassword1" />
                        <p v-for="error of v$.newPassword1.$errors"
                            :key="error.$uid"
                            class="mt-2 text-xs text-red-600 dark:text-red-500">
                            {{ error.$message }}
                        </p>
                    </div>

                    <div class="mb-3">
                        <label class="text-sm text-gray-700">
                            Confirm new password
                        </label>
                        <input type="password"
                            @blur="v$.newPassword2.$touch"
                            class="mt-1 block w-full rounded-lg bg-gray-50
                            border border-gray-300 text-gray-900
                            text-sm p-2.5 focus:outline-none
                            focus:shadow-outline"
                            :class="{
                                'border-red-400': v$.newPassword2.$dirty &&
                                                    v$.newPassword2.$invalid 
                                
                            }"
                            v-model="changeForm.newPassword2" />
                        <p v-for="error of v$.newPassword2.$errors"
                            :key="error.$uid"
                            class="mt-2 text-xs text-red-600 dark:text-red-500">
                            {{ error.$message }}
                        </p>
                    </div>

                    <button class="block rounded-lg border border-transparent 
                        bg-green-300 focus:hover:enabled:bg-green-500
                        px-3 py-2 text-white enabled:bg-green-400
                        focus:outline-none focus:ring-2 focus:ring-green-200
                        font-medium text-sm">
                        Confirm
                    </button>
                </form>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { onMounted, defineComponent, ref, computed } from 'vue'

import type { ChangePasswordInput } from '@/common/models/auth.model'
import { passwordRegex } from '@/common/helpers';
import { useAuthStore } from '@/stores'

import { helpers, required, sameAs } from '@vuelidate/validators'
import { useToast } from 'vue-toastification'
import useVuelidate from '@vuelidate/core'
import { useRoute } from 'vue-router'

export default defineComponent({
    name: 'ChangePassword',
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
                    'Minimum eight characters, at least one upper case letter,\
                    one lower case letter, one digit and one special character',
                    passwordRegex
                )
            },
            newPassword1: { 
                required: helpers.withMessage(
                    'New password is required',
                    required
                ),
                strength: helpers.withMessage(
                    'Minimum eight characters, at least one upper case letter,\
                    one lower case letter, one digit and one special character',
                    passwordRegex
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

        // Services
        const authStore = useAuthStore()
        const toast = useToast()
        const route = useRoute()

        onMounted(() => {
            // console.log('Mounted ChangePassword')
        })

        return {
            changeForm,
            v$,
            validation
        }
    }
})
</script>