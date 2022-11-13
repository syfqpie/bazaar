<template>
    <TheConfirmDialog
        :title-text="'Confirm delete'"
        :message-text="'Do you confirm to delete this address?'"
        :is-loading="isLoading"
        @on-cancel="onCancel()"
        @on-confirm="onConfirm()" />
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue'

import type { CustomerAddress } from '@/common/models/address.model'
import TheConfirmDialog from '@/components/basics/TheConfirmDialog.vue'
import { useAddressStore } from '@/stores'

import { useToast } from 'vue-toastification'

export default defineComponent({
    name: 'DeleteAddressConfirmation',
    setup(props, context) {
        // Checker
        const isLoading = ref(false)

        // Services
        const addressStore = useAddressStore()
        const toast = useToast()

        onMounted(() => {
            // console.log('Mounted DeleteAddressConfirmation')
        })

        /**
         * Trigger delete address action
         */
        const onConfirm = () => {
            isLoading.value = true

            return addressStore.destroy(props.currentAddress.id)
                .then(data => {
                    isLoading.value = false

                    // Success toastr and close modal
                    toast.success('Address deleted')
                    onCancel()
                })
                .catch(err => {
                    isLoading.value = false

                    // Error toastr and close modal
                    toast.error('Error')
                    onCancel()
                })
        }

        /**
         * Emit on cancel signal to listener
         */
        const onCancel = () => {
            context.emit('onCancel')
        }

        return {
            isLoading,
            onConfirm,
            onCancel
        }
    },
    components: {
        TheConfirmDialog
    },
    props: {
        currentAddress: {
            type: Object as () => CustomerAddress,
            required: true
        }
    },
    emits: ['onCancel']
})
</script>