<template>
    <div class="w-full py-8 px-4 sm:px-12">
        <div>
            <img alt="Bazaar"
                class="mx-auto h-12 w-auto"
                src="@/assets/img/default/trolley.png" />

            <h2 class="mt-6 text-center text-3xl
                font-bold tracking-tight text-gray-900">
                Create your account
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
                            focus:shadow-outline"
                            placeholder="Enter your email"
                            :class="{
                                'border-red-400': v$.username.$dirty &&
                                                    v$.username.$invalid 
                                
                            }"
                            v-model="registerForm.username"
                            @blur="v$.username.$touch" />
                        <p v-for="error of v$.username.$errors"
                            :key="error.$uid"
                            class="mt-2 text-xs text-red-600 dark:text-red-500">
                            {{ error.$message }}
                        </p>
                    </div>

                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                        <div>
                            <label class="text-sm text-gray-700">First name</label>
                            <input type="text"
                                class="mt-1 block w-full rounded-lg bg-gray-50
                                border border-gray-300 text-gray-900
                                text-sm p-2.5 focus:outline-none
                                focus:shadow-outline"
                                placeholder="Enter your first name"
                                :class="{
                                    'border-red-400': v$.firstName.$dirty &&
                                                        v$.firstName.$invalid 
                                    
                                }"
                                v-model="registerForm.firstName"
                                @blur="v$.firstName.$touch" />
                            <p v-for="error of v$.firstName.$errors"
                                :key="error.$uid"
                                class="mt-2 text-xs text-red-600 dark:text-red-500">
                                {{ error.$message }}
                            </p>
                        </div>
                        <div>
                            <label class="text-sm text-gray-700">Last name</label>
                            <input type="text"
                                class="mt-1 block w-full rounded-lg bg-gray-50
                                border border-gray-300 text-gray-900
                                text-sm p-2.5 focus:outline-none
                                focus:shadow-outline"
                                placeholder="Enter your last name"
                                :class="{
                                    'border-red-400': v$.lastName.$dirty &&
                                                        v$.lastName.$invalid 
                                    
                                }"
                                v-model="registerForm.lastName"
                                @blur="v$.lastName.$touch" />
                            <p v-for="error of v$.lastName.$errors"
                                :key="error.$uid"
                                class="mt-2 text-xs text-red-600 dark:text-red-500">
                                {{ error.$message }}
                            </p>
                        </div>
                    </div>

                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                        <div>
                            <label class="text-sm text-gray-700">Phone no.</label>
                            <input type="text"
                                class="mt-1 block w-full rounded-lg bg-gray-50
                                border border-gray-300 text-gray-900
                                text-sm p-2.5 focus:outline-none
                                focus:shadow-outline"
                                placeholder="Enter your phone no."
                                :class="{
                                    'border-red-400': v$.phoneNo.$dirty &&
                                                        v$.phoneNo.$invalid 
                                    
                                }"
                                v-model="registerForm.phoneNo"
                                @blur="v$.phoneNo.$touch" />
                            <p v-for="error of v$.phoneNo.$errors"
                                :key="error.$uid"
                                class="mt-2 text-xs text-red-600 dark:text-red-500">
                                {{ error.$message }}
                            </p>
                        </div>

                        <div>
                            <label class="text-sm text-gray-700">Date of birth</label>
                            <input type="date"
                                class="mt-1 block w-full rounded-lg bg-gray-50
                                border border-gray-300 text-gray-900
                                text-sm p-2.5 focus:outline-none
                                focus:shadow-outline"
                                :class="{
                                    'border-red-400': v$.dateOfBirth.$dirty &&
                                                        v$.dateOfBirth.$invalid 
                                    
                                }"
                                placeholder="Select date of birth"
                                v-model="registerForm.dateOfBirth"
                                @blur="v$.dateOfBirth.$touch" />
                        </div>
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
                            v-on:click="register()"
                            :disabled="isLoading || v$.$invalid">
                            Join as vendor
                        </button>
                    </div>

                    <div class="mt-2 mb-1 justify-self-center text-sm">
                        <p>or</p>
                    </div>

                    <div class="flex flex-col">
                        <div class="text-center">
                            <p class="text-sm text-gray-500">
                                Want to be a vendor?
                                <router-link :to="{ path: '/auth/registration/vendor' }"
                                    class="font-medium 
                                    text-green-400 hover:text-green-300">
                                    Join
                                </router-link>
                            </p>
                        </div>
                        
                        <div class="text-center">
                            <p class="text-sm text-gray-500">
                                Already have an account?
                                <router-link :to="{ path: '/auth/login' }"
                                    class="font-medium 
                                    text-green-400 hover:text-green-300">
                                    Sign in
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

import type { RegisterCustomerInput } from '@/common/models/auth.model'
import router from '@/router'
import { useAuthStore } from '@/stores'

import { email, helpers, required } from '@vuelidate/validators'
import { useToast } from 'vue-toastification'
import useVuelidate from '@vuelidate/core'

export default defineComponent({
  name: 'CustomerRegistration',
  setup() {
    // Form
    const registerForm = ref<RegisterCustomerInput>({
        username: null,
        firstName: null,
        lastName: null,
        phoneNo: null,
        dateOfBirth: null
    })
    const validation = computed(() => ({
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
        firstName: { 
            required: helpers.withMessage(
                'First name is required',
                required
            )
        },
        lastName: { 
            required: helpers.withMessage(
                'Last name is required',
                required
            )
        },
        phoneNo: { 
            required: helpers.withMessage(
                'Phone no. is required',
                required
            )
        },
        dateOfBirth: {}
    }))
    const v$ = useVuelidate(validation, registerForm.value)

    // Services
    const authStore = useAuthStore()
    const toast = useToast()

    // Checkers
    const isLoading = ref<boolean>(false)

    onMounted(() => {
      // console.log('Mounted CustomerRegistration')
    })

    // Register
    const register = () => {
        isLoading.value = true
        
        return authStore.registerCustomer(registerForm.value)
            .then(data => {
                isLoading.value = false

                // Success toastr
                toast.success(data.detail)
                
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
        registerForm,
        register,
        v$,
        isLoading
    }
  }
})
</script>
