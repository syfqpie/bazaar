<template>
    <TheModal
        :modal-size="ModalSize.MD"
        @on-click-external="onCancel()">
        <template #content>
            <div
                class="flex justify-between items-center
                py-4 px-6 rounded-t border-b">
                <h3 class="text-xl font-medium text-gray-900">
                    Add new address
                </h3>
                
                <button 
                    type="button" 
                    class="text-gray-400 bg-transparent 
                    hover:bg-gray-200 hover:text-gray-900
                    rounded-lg text-sm p-1.5 ml-auto inline-flex
                    items-center" 
                    @click="onCancel()">
                    <i class="fa-solid fa-xmark"></i>
                    <span class="sr-only">Close modal</span>
                </button>
            </div>
            
            <div class="px-6 py-4 space-y-6">
                <form @submit.prevent>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                        <div>
                            <label class="text-sm text-gray-700">
                                Receiver name
                            </label>
                            <TheInput
                                type="text"
                                placeholder="Enter receiver name"
                                v-model="addressForm.name"
                                :class="{
                                    '!border-red-400': v$.name.$dirty &&
                                                        v$.name.$invalid 
                                    
                                }"
                                @blur="v$.name.$touch" />
                            <p
                                v-for="error of v$.name.$errors"
                                :key="error.$uid"
                                class="mt-2 text-xs text-red-600">
                                {{ error.$message }}
                            </p>
                        </div>

                        <div>
                            <label class="text-sm text-gray-700">
                                Receiver phone no.
                            </label>
                            <TheInput
                                type="text"
                                placeholder="Enter receiver phone no."
                                v-model="addressForm.phoneNo"
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
                    </div>

                    <div class="my-3">
                        <label class="text-sm text-gray-700">
                            Address
                        </label>
                        <TheTextArea
                            type="text"
                            placeholder="Enter address"
                            v-model="addressForm.address"
                            :class="{
                                '!border-red-400': v$.address.$dirty &&
                                                    v$.address.$invalid 
                                
                            }"
                            @blur="v$.address.$touch" />
                        <p
                            v-for="error of v$.address.$errors"
                            :key="error.$uid"
                            class="mt-2 text-xs text-red-600">
                            {{ error.$message }}
                        </p>
                    </div>
                    
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                        <div>
                            <label class="text-sm text-gray-700">
                                Zipcode
                            </label>
                            <TheInput
                                type="text"
                                placeholder="Enter zipcode"
                                v-model="addressForm.zipcode"
                                :class="{
                                    '!border-red-400': v$.zipcode.$dirty &&
                                                        v$.zipcode.$invalid 
                                    
                                }"
                                @blur="v$.zipcode.$touch" />
                            <p
                                v-for="error of v$.zipcode.$errors"
                                :key="error.$uid"
                                class="mt-2 text-xs text-red-600">
                                {{ error.$message }}
                            </p>
                        </div>

                        <div>
                            <label class="text-sm text-gray-700">
                                City
                            </label>
                            <TheInput
                                type="text"
                                placeholder="Enter city"
                                v-model="addressForm.city"
                                :class="{
                                    '!border-red-400': v$.city.$dirty &&
                                                        v$.city.$invalid 
                                    
                                }"
                                @blur="v$.city.$touch" />
                            <p
                                v-for="error of v$.city.$errors"
                                :key="error.$uid"
                                class="mt-2 text-xs text-red-600">
                                {{ error.$message }}
                            </p>
                        </div>

                        <div>
                            <label class="text-sm text-gray-700">
                                State
                            </label>
                            <TheInput
                                type="text"
                                placeholder="Enter state"
                                v-model="addressForm.state"
                                :class="{
                                    '!border-red-400': v$.state.$dirty &&
                                                        v$.state.$invalid 
                                    
                                }"
                                @blur="v$.state.$touch" />
                            <p
                                v-for="error of v$.state.$errors"
                                :key="error.$uid"
                                class="mt-2 text-xs text-red-600">
                                {{ error.$message }}
                            </p>
                        </div>

                        <div>
                            <label class="text-sm text-gray-700">
                                Country
                            </label>
                            <TheInput
                                type="text"
                                :value="CountryList.MY "
                                disabled />
                        </div>
                    </div>

                    <div class="mt-3">
                        <label class="text-sm text-gray-700">
                            Instructions
                        </label>
                        <TheTextArea
                            type="text"
                            placeholder="Enter instructions, if any"
                            v-model="addressForm.instructions" />
                    </div>
                </form>
            </div>
            
            <div 
                class="flex items-center px-6 py-4 space-x-2
                rounded-b border-t border-gray-200">
                <TheButton
                    type="button"
                    @click="onSubmit()">
                    <span v-if="!isLoading">
                        Save
                    </span>
                    <span v-else>
                        <i class="fa-solid fa-circle-notch animate-spin"></i>
                        Loading
                    </span>
                </TheButton>
                
                <TheOutlineButton
                    type="button"
                    @click="onCancel()">
                    Cancel
                </TheOutlineButton>
            </div>
        </template>
    </TheModal>
</template>

<script lang="ts">
import { computed, defineComponent, onMounted, ref } from 'vue'

import { CountryList } from '@/common/country.enum'
import { phoneNoRegex } from '@/common/helpers'
import { ModalSize } from '@/common/utility/basic.model'
import TheButton from '@/components/basics/TheButton.vue'
import TheInput from '@/components/basics/TheInput.vue'
import TheModal from '@/components/basics/TheModal.vue'
import TheOutlineButton from '@/components/basics/TheOutlineButton.vue'
import TheTextArea from '@/components/basics/TheTextArea.vue'
import { useAddressStore } from '@/stores'

import useVuelidate from '@vuelidate/core'
import { helpers, maxLength, minLength, required } from '@vuelidate/validators'
import { useToast } from 'vue-toastification'

export default defineComponent({
    name: 'AddAddressModal',
    setup(props, context) {
        // Form
        const addressForm = ref({
            name: null as string | null,
            phoneNo: null as string | null,
            instructions: null as string | null,
            address: null as string | null,
            zipcode: null as string | null,
            city: null as string | null,
            state: null as string | null
        })
        const validation = computed(() => ({
            name: {
                required: helpers.withMessage(
                    'Name is required',
                    required
                )
            },
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
            address: {
                required: helpers.withMessage(
                    'Address is required',
                    required
                )
            },
            zipcode: {
                required: helpers.withMessage(
                    'Zipcode is required',
                    required
                )
            },
            city: {
                required: helpers.withMessage(
                    'City is required',
                    required
                )
            },
            state: {
                required: helpers.withMessage(
                    'State is required',
                    required
                )
            }
        }))
        const v$ = useVuelidate(validation, addressForm.value)

        // Checker
        const isLoading = ref(false)
        const toast = useToast()

        // Services
        const addressStore = useAddressStore()

        onMounted(() => {
            // console.log('Mounted AddAddressModal')
        })

        // Methods
        /**
         * Emit on cancel signal to listener
         */
        const onCancel = () => {
            // Adding a on-cancel listener to the component
            context.emit('onCancel')
        }

        /**
         * Submit form to add address
         */
        const onSubmit = () => {
            isLoading.value = true
            return addressStore.create(addressForm.value)
                .then(data => {
                    isLoading.value = false

                    // Success toastr and close modal
                    toast.success('New address saved')
                    onCancel()
                })
                .catch(err => {
                    isLoading.value = false

                    // Error toastr
                    toast.error('Error')
                })
        }

        return {
            ModalSize,
            CountryList,
            isLoading,
            onCancel,
            onSubmit,
            addressForm,
            v$
        }
    },
    components: { 
        TheButton,
        TheInput,
        TheModal,
        TheOutlineButton,
        TheTextArea
    },
    emits: ['onCancel']
})
</script>