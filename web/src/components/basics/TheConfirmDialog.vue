<template>
    <TheModal
        :modal-size="size"
        @on-click-external="onCancel()">
        <template #content>
            <div
                class="flex justify-between items-center
                py-4 px-6 rounded-t">
                <h5 class="text-base font-medium text-gray-900">
                    {{ titleText }}
                </h5>
                
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

            <div class="px-6 pb-4 space-y-6">
                <p class="text-sm leading-relaxed text-gray-500">
                    {{ messageText }}
                </p>
            </div>

            <div 
                class="flex items-center px-6 py-4 space-x-2
                rounded-b border-gray-200">
                <TheButton
                    type="button"
                    :disabled="isLoading"
                    @click="onConfirm()">
                    <span v-if="!isLoading">
                        {{ confirmText }}
                    </span>
                    <span v-else>
                        <i class="fa-solid fa-circle-notch animate-spin"></i>
                        Loading
                    </span>
                </TheButton>
                
                <TheOutlineButton
                    type="button"
                    :disabled="isLoading"
                    @click="onCancel()">
                    {{ cancelText }}
                </TheOutlineButton>
            </div>
        </template>
    </TheModal>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import { BasicColor, ModalSize } from '@/common/utility/basic.model'
import TheButton from '@/components/basics/TheButton.vue'
import TheModal from '@/components/basics/TheModal.vue'
import TheOutlineButton from '@/components/basics/TheOutlineButton.vue'

export default defineComponent({
    name: 'TheConfirmDialog',
    setup(props, context) {
        /**
         * Emit on confirm signal to listener
         */
        const onConfirm = () => {
            context.emit('onConfirm')
        }

        /**
         * Emit on cancel signal to listener
         */
        const onCancel = () => {
            context.emit('onCancel')
        }

        return {
            BasicColor,
            ModalSize,
            onConfirm,
            onCancel
        }
    },
    components: {
        TheButton,
        TheModal,
        TheOutlineButton
    },
    props: {
        size: {
            type: String,
            default: ModalSize.SS
        },
        isLoading: {
            type: Boolean,
            default: false
        },
        titleText: {
            type: String,
            default: 'Confirmation'
        },
        messageText: {
            type: String,
            default: 'Confirm to proceed?'
        },
        confirmText: {
            type: String,
            default: 'Confirm'
        },
        cancelText: {
            type: String,
            default: 'Cancel'
        }
    },
    emits: [
        'onConfirm',
        'onCancel'
    ]
})
</script>