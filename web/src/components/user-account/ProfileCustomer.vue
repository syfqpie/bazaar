<template>
    <form @submit.prevent>
        <div class="mb-3">
            <label class="text-sm text-gray-700">
                Phone no.
            </label>
            <TheInput
                type="text"
                placeholder="Enter your phone no."
                v-model="customerForm.phoneNo"
                :class="{
                    '!border-red-400': v$.phoneNo.$dirty &&
                                         v$.phoneNo.$invalid 
                    
                }"
                @blur="v$.phoneNo.$touch" />
            <p
                v-for="error of v$.phoneNo.$errors"
                :key="error.$uid"
                class="mt-2 text-xs text-red-600">
                {{ error.$message }}
            </p>
        </div>

        <div class="mb-3">
            <label class="text-sm text-gray-700">
                Phone no.
            </label>

            <div class="flex flex-wrap mt-1">
                <div class="flex items-center mr-4">
                    <TheRadio
                        id="male-gender-radio"
                        name="gender-radio"
                        v-model="customerForm.gender"
                        :value="GenderType.MALE" />
                    <label
                        for="male-gender-radio"
                        class="ml-2 text-sm text-gray-900">
                        Male
                    </label>
                </div>

                <div class="flex items-center mr-4">
                    <TheRadio
                        id="female-gender-radio"
                        name="gender-radio"
                        v-model="customerForm.gender"
                        :value="GenderType.FEMALE" />
                    <label
                        for="female-gender-radio"
                        class="ml-2 text-sm text-gray-900">
                        Female
                    </label>
                </div>

                <div class="flex items-center mr-4">
                    <TheRadio
                        id="secret-gender-radio"
                        name="gender-radio"
                        v-model="customerForm.gender"
                        :value="GenderType.SECRET" />
                    <label
                        for="secret-gender-radio"
                        class="ml-2 text-sm text-gray-900">
                        Secret
                    </label>
                </div>
            </div>
        </div>

        <div class="flex items-center mb-4">
            <input
                type="checkbox"
                class="w-4 h-4 accent-indigo-600 focus:ring-1
                focus:ring-indigo-700 transition-all ease-in duration-150"
                v-model="customerForm.isNewsletterEnabled">
            <label
                for="default-checkbox"
                class="ml-2 text-sm text-gray-700">
                Receive newsletter email from us
            </label>
        </div>

        <TheButton
            @click="updateCustomer()"
            :disabled="isLoading || v$.$invalid">
            <span v-if="!isLoading">
                Save
            </span>
            <span v-else>
                <i class="fa-solid fa-circle-notch animate-spin"></i>
                Loading
            </span>
        </TheButton>
    </form>
</template>

<script lang="ts">
import { computed, defineComponent, onMounted, ref } from 'vue'

import TheButton from '@/components/basics/TheButton.vue'
import TheInput from '@/components/basics/TheInput.vue'
import TheRadio from '@/components/basics/TheRadio.vue'
import { phoneNoRegex } from '@/common/helpers'
import { GenderType } from '@/common/models/customer.model'
import { useAuthStore, useCustomerStore } from '@/stores'

import useVuelidate from '@vuelidate/core'
import { helpers, maxLength, minLength, required } from '@vuelidate/validators'
import { useToast } from 'vue-toastification'


export default defineComponent({
    name: 'ProfileCustomer',
    setup() {
        // Form
        const customerForm = ref({
            phoneNo: null as string | null,
            gender: GenderType.MALE as GenderType,
            dateOfBirth: null as string | null,
            isNewsletterEnabled: true
        })
        const validation = computed(() => ({
            phoneNo: { 
                required: helpers.withMessage(
                    'Phone no. is required',
                    required
                ),
                maxLength: helpers.withMessage(
                    'Maximum 30 characters only',
                    maxLength(30)
                ),
                minLength: helpers.withMessage(
                    'Mininum 10 characters ',
                    minLength(10)
                ),
                pattern: helpers.withMessage(
                    'Wrong pattern',
                    phoneNoRegex
                )
            },
            isNewsletterEnabled: { },
        }))
        const v$ = useVuelidate(validation, customerForm.value)

        // Checker
        const isLoading = ref(false)

        // Services
        const authStore = useAuthStore()
        const customerStore = useCustomerStore()
        const toast = useToast()

        onMounted(() => {
            // console.log('Mounted ProfileCustomer')
            getCustomerData()
        })

        /**
         * Get current customer data
         */
        const getCustomerData = () => {
            isLoading.value = true

            return customerStore.retrieve(authStore.customerId!)
                .then(data => {
                    isLoading.value = false

                    // Success toastr and set data
                    toast.success('Customer loaded')
                    setFormData()
                })
                .catch(err => {
                    isLoading.value = false
                    
                    toast.error('Customer not loaded')
                })
        }

        /**
         * Set form data after loaded
         * customer information
         */
        const setFormData = () => {
            if (customerStore.customer) {
                customerForm.value.phoneNo = customerStore.customer.phoneNo
                customerForm.value.gender = customerStore.customer.gender
                customerForm.value.dateOfBirth = customerStore.customer.dateOfBirth
                customerForm.value.isNewsletterEnabled = customerStore.customer.isNewsletterEnabled
            }
        }

        /**
         * Update customer information
         */
        const updateCustomer = () => {
            isLoading.value = true

            return customerStore.patch(authStore.customerId!, customerForm.value)
                .then(data => {
                    isLoading.value = false

                    // Success toastr and set data
                    toast.success('Customer information saved')
                    setFormData()
                })
                .catch(err => {
                    isLoading.value = false
                })
        }

        return {
            customerForm,
            v$,
            isLoading,
            updateCustomer,
            GenderType
        }
    },
    components: {
    TheButton,
    TheInput,
    TheRadio
}
})
</script>