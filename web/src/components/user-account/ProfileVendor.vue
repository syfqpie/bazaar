<template>
    <form @submit.prevent>
        <div class="mb-3">
            <label class="text-sm text-gray-700">
                Name
            </label>
            <input
                type="text"
                class="mt-1 block w-full rounded-lg bg-gray-50
                border border-gray-300 text-gray-900
                text-sm p-2.5 focus:outline-none
                focus:shadow-outline"
                placeholder="Enter your name"
                v-model="vendorForm.name"
                :class="{
                    'border-red-400': v$.name.$dirty &&
                                        v$.name.$invalid 
                    
                }"
                @blur="v$.name.$touch" />
            <p
                v-for="error of v$.name.$errors"
                :key="error.$uid"
                class="mt-2 text-xs text-red-600 dark:text-red-500">
                {{ error.$message }}
            </p>
        </div>

        <div class="mb-3">
            <label class="text-sm text-gray-700">
                Description
            </label>
            <textarea
                type="text"
                class="mt-1 block w-full rounded-lg bg-gray-50
                border border-gray-300 text-gray-900
                text-sm p-2.5 focus:outline-none
                focus:shadow-outline"
                placeholder="Enter your description"
                v-model="vendorForm.description"
                :class="{
                    'border-red-400': v$.description.$dirty &&
                                        v$.description.$invalid 
                    
                }"
                @blur="v$.description.$touch" >
            </textarea>
        </div>

        <div class="mb-3">
            <label class="text-sm text-gray-700">
                Phone no.
            </label>
            <input
                type="text"
                class="mt-1 block w-full rounded-lg bg-gray-50
                border border-gray-300 text-gray-900
                text-sm p-2.5 focus:outline-none
                focus:shadow-outline"
                placeholder="Enter your phone no."
                v-model="vendorForm.phoneNo"
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

        <div class="mb-3">
            <label class="text-sm text-gray-700">
                Verification
            </label>
            <h5 class="mt-1 flex items-center text-sm font-extrabold">
                <span 
                    class="text-medium font-semibold px-2.5 py-0.5 rounded"
                    :class="{
                        'bg-pink-100 text-pink-800': !vendorStore.vendor?.isVerified,
                        'bg-indigo-100 text-indigo-800': vendorStore.vendor?.isVerified
                    }">
                    {{ vendorStore.vendor?.isVerified ? 'Verified'  : 'Not verified' }}
                </span>
            </h5>
        </div>

        <div class="flex items-center mb-4">
            <input
                type="checkbox"
                class="w-4 h-4 accent-green-500"
                v-model="vendorForm.isNewsletterEnabled">
            <label
                for="default-checkbox"
                class="ml-2 text-sm text-gray-700">
                Receive newsletter email from us
            </label>
        </div>

        <button
            class="block rounded-lg border border-transparent 
            bg-green-400 focus:hover:enabled:bg-green-500
            p-2.5 text-white enabled:bg-green-400
            focus:outline-none focus:ring-2 focus:ring-green-200
            font-medium text-sm disabled:bg-green-300
            disabled:border-green-300 disabled:shadow-none
            disabled:cursor-not-allowed"
            @click="updateVendor()"
            :disabled="isLoading || v$.$invalid">
            Save
        </button>
    </form>
</template>

<script lang="ts">
import { computed, defineComponent, onMounted, ref } from 'vue'

import { phoneNoRegex } from '@/common/helpers'
import { useAuthStore, useVendorStore } from '@/stores'

import useVuelidate from '@vuelidate/core'
import { helpers, maxLength, minLength, required } from '@vuelidate/validators'
import { useToast } from 'vue-toastification'

export default defineComponent({
    name: 'ProfileVendor',
    setup() {
        // Form
        const vendorForm = ref({
            name: null as string | null,
            description: undefined as string | undefined,
            phoneNo: null as string | null,
            isNewsletterEnabled: true
        })
        const validation = computed(() => ({
            name: { 
                required: helpers.withMessage(
                    'Name is required',
                    required
                ),
                maxLength: helpers.withMessage(
                    'Max length is 100',
                    maxLength(100)
                )
            },
            description: { },
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
        const v$ = useVuelidate(validation, vendorForm.value)

        // Checker
        const isLoading = ref(false)

        // Services
        const authStore = useAuthStore()
        const vendorStore = useVendorStore()
        const toast = useToast()

        onMounted(() => {
            // console.log('Mounted AccountProfile')
            getVendorData()
        })

        /** */
        const getVendorData = () => {
            isLoading.value = true

            return vendorStore.retrieve(authStore.vendorId!)
                .then(data => {
                    isLoading.value = false

                    // Success toastr and set data
                    toast.success('Vendor loaded')
                    setFormData()
                })
                .catch(err => {
                    isLoading.value = false
                    
                    toast.error('Vendor not loaded')
                })
        }

        /**
         * Set form data after loaded
         * vendor information
         */
        const setFormData = () => {
            if (vendorStore.vendor) {
                vendorForm.value.name = vendorStore.vendor.name
                vendorForm.value.description = vendorStore.vendor.description
                vendorForm.value.phoneNo = vendorStore.vendor.phoneNo
                vendorForm.value.isNewsletterEnabled = vendorStore.vendor.isNewsletterEnabled
            }
        }

        /**
         * Update vendor information
         */
        const updateVendor = () => {
            isLoading.value = true

            return vendorStore.patch(authStore.vendorId!, vendorForm.value)
                .then(data => {
                    isLoading.value = false

                    // Success toastr and set data
                    toast.success('Vendor information saved')
                    setFormData()
                })
                .catch(err => {
                    isLoading.value = false
                })
        }

        return {
            vendorStore,
            vendorForm,
            v$,
            validation,
            isLoading,
            updateVendor
        }
    }
})
</script>

<style scope>
input[type='checkbox']:checked:after {
  content: '✔';
  color: white !important;
}
input[type='checkbox']:checked:before {
  content: '✔';
  color: white !important;
}
</style>