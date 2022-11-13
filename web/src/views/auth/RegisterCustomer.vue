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
                Create your account
            </h2>
        </div>

        <form @submit.prevent>
            <div class="mt-8 max-w-md">
                <div class="grid grid-cols-1 gap-3">
                    <div>
                        <label class="text-sm text-gray-700">Email</label>
                        <TheInput
                            type="email"
                            placeholder="Enter your email"
                            v-model="registerForm.username"
                            :class="{
                                'border-red-400': v$.username.$dirty &&
                                                    v$.username.$invalid 
                                
                            }"
                            @blur="v$.username.$touch" />
                        <p
                            v-for="error of v$.username.$errors"
                            :key="error.$uid"
                            class="mt-2 text-xs text-red-600 dark:text-red-500">
                            {{ error.$message }}
                        </p>
                    </div>

                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                        <div>
                            <label class="text-sm text-gray-700">First name</label>
                            <TheInput
                                type="text"
                                placeholder="Enter your first name"
                                v-model="registerForm.firstName"
                                :class="{
                                    'border-red-400': v$.firstName.$dirty &&
                                                        v$.firstName.$invalid 
                                    
                                }"
                                @blur="v$.firstName.$touch" />
                            <p
                                v-for="error of v$.firstName.$errors"
                                :key="error.$uid"
                                class="mt-2 text-xs text-red-600 dark:text-red-500">
                                {{ error.$message }}
                            </p>
                        </div>
                        <div>
                            <label class="text-sm text-gray-700">Last name</label>
                            <TheInput
                                type="text"
                                placeholder="Enter your last name"
                                v-model="registerForm.lastName"
                                :class="{
                                    'border-red-400': v$.lastName.$dirty &&
                                                        v$.lastName.$invalid 
                                    
                                }"
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
                            <TheInput
                                type="text"
                                placeholder="Enter your phone no."
                                v-model="registerForm.phoneNo"
                                :class="{
                                    'border-red-400': v$.phoneNo.$dirty &&
                                                        v$.phoneNo.$invalid 
                                    
                                }"
                                @blur="v$.phoneNo.$touch" />
                            <p
                                v-for="error of v$.phoneNo.$errors"
                                :key="error.$uid"
                                class="mt-2 text-xs text-red-600 dark:text-red-500">
                                {{ error.$message }}
                            </p>
                        </div>

                        <div>
                            <label class="text-sm text-gray-700">Date of birth</label>
                            <TheInput
                                type="date"
                                placeholder="Select date of birth"
                                v-model="registerForm.dateOfBirth"
                                :class="{
                                    'border-red-400': v$.dateOfBirth.$dirty &&
                                                        v$.dateOfBirth.$invalid 
                                    
                                }"
                                @blur="v$.dateOfBirth.$touch" />
                        </div>
                    </div>

                    <div>
                        <TheButton 
                            @click="register()"
                            :size="'lg'"
                            :is-full="true"
                            :disabled="isLoading || v$.$invalid">
                            <span v-if="!isLoading">
                                Register
                            </span>
                            <span v-else>
                                <i class="fa-solid fa-circle-notch animate-spin"></i>
                                Loading
                            </span>
                        </TheButton>
                    </div>

                    <div class="mt-2 mb-1 justify-self-center text-sm">
                        <p>or</p>
                    </div>

                    <div class="flex flex-col">
                        <div class="text-center">
                            <p class="text-sm text-gray-500">
                                Want to be a vendor?
                                <router-link
                                    :to="{ path: '/auth/registration/vendor' }"
                                    class="font-medium 
                                    text-indigo-500 hover:text-indigo-600">
                                    Join
                                </router-link>
                            </p>
                        </div>
                        
                        <div class="text-center">
                            <p class="text-sm text-gray-500">
                                Already have an account?
                                <router-link
                                    :to="{ path: '/auth/login' }"
                                    class="font-medium 
                                    text-indigo-500 hover:text-indigo-600">
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
import TheButton from '@/components/basics/TheButton.vue'
import TheInput from '@/components/basics/TheInput.vue'
import router from '@/router'
import { useAuthStore } from '@/stores'

import useVuelidate from '@vuelidate/core'
import { email, helpers, required } from '@vuelidate/validators'
import { useToast } from 'vue-toastification'

export default defineComponent({
  name: 'RegisterCustomer',
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

    // Checkers
    const isLoading = ref<boolean>(false)
    
    // Services
    const authStore = useAuthStore()
    const toast = useToast()

    onMounted(() => {
      // console.log('Mounted RegisterCustomer')
    })

    /**
     * Make http request to API to register as customer
     */
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
  },
  components: {
    TheButton,
    TheInput
  }
})
</script>
