<template>
    <div class="w-full">
        <div
            class="p-4 sm:p-6 md:p-8 w-full bg-white
            rounded-lg border border-gray-200 shadow-sm">
            <div class="grid grid-cols-2 mb-3">
                <div>
                    <h5
                        class="mb-0 text-base font-semibold 
                        text-gray-900 md:text-xl">
                        Addresses
                    </h5>
                    <p
                        class="text-sm font-normal text-gray-500
                        dark:text-gray-400">
                        Manage your saved addresses
                    </p>
                </div>

                <div class="text-right">
                    <TheOutlineButton
                        :size="ModalSize.SM"
                        @click="toggleAddModal()">
                        <i class="fa-solid fa-plus"></i>
                        Add new
                    </TheOutlineButton>
                </div>
            </div>

            <div class="grid grid-cols-2 gap-3">
                <CustomerAddressCard
                    v-for="address in addressStore.addresses"
                    :key="address.id"
                    :address="address" />
            </div>
        </div>
        
        <AddAddressModal 
            v-if="isAddAddress"
            @on-cancel="toggleAddModal()" />
    </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref} from 'vue'

import { ModalSize } from '@/common/utility/basic.model'
import TheOutlineButton from '@/components/basics/TheOutlineButton.vue'
import AddAddressModal from '@/components/user-account/AddAddressModal.vue'
import CustomerAddressCard from '@/components/user-account/CustomerAddressCard.vue'
import { useAddressStore } from '@/stores'

import { useToast } from 'vue-toastification'

/**
 * TODO:
 *      - This component should be  visible and accessible only by CUSTOMER
 */
export default defineComponent({
    name: 'AccountAddress',
    setup() {
        // Checker
        const isLoading = ref(false)
        const isAddAddress = ref(false)

        // Services
        const addressStore = useAddressStore()
        const toast = useToast()

        onMounted(() => {
            // console.log('Mounted AccountAddress')
            if (addressStore.addresses.length === 0) {
                getData()
            }
        })

        /**
         * Trigger API call to get current
         * user's addresses
         */
        const getData = () => {
            isLoading.value = true

            return addressStore.list()
                .then(data => {
                    isLoading.value = false
                })
                .catch(err => {
                    isLoading.value = false
                    toast.error('Error fetching data')
            })
        }

        /**
         * Toggle add address modal
         */
        const toggleAddModal = () => {
            return isAddAddress.value = !isAddAddress.value
        }

        return {
            ModalSize,
            addressStore,
            isAddAddress,
            getData,
            toggleAddModal
        }
    },
    components: {
        TheOutlineButton,
        AddAddressModal,
        CustomerAddressCard
    }
})
</script>