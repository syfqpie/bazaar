<template>
    <div
        class="overflow-y-auto overflow-x-hidden fixed top-0
        right-0 left-0 z-50 w-full md:inset-0 h-modal md:h-full
        justify-center items-center flex">
        <div 
            class="relative p-2.5 w-full h-full md:h-auto"
            :class="{
                'max-w-md': modalSize === ModalSize.SM,
                'max-w-lg': modalSize === ModalSize.MD,
                'max-w-4xl': modalSize === ModalSize.LG,
                'max-w-7xl': modalSize === ModalSize.XL
            }">
            <div
                ref="modalRef"
                class="relative bg-white rounded-lg shadow">
                <slot name="content">
                    <!-- This is fallback content -->
                    <div class="h-10">
                        <p class="italic">
                            Placeholder text...
                        </p>
                    </div>
                </slot>
            </div>
        </div>
    </div>

    <div class="bg-gray-900 bg-opacity-50 fixed inset-0 z-40"></div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

import { ModalSize } from '@/common/utility/basic.model'

import { onClickOutside } from '@vueuse/core'

export default defineComponent({
    name: 'TheModal',
    setup(props, context) {
        // Component ref
        const modalRef = ref(null)

        // Event
        onClickOutside(modalRef, (event) => {
            context.emit('onClickExternal')
        })

        return {
            ModalSize,
            modalRef
        }
    },
    props: {
        modalSize: {
            type: String,
            default: ModalSize.SM
        }
    },
    emits: ['onClickExternal']
})
</script>
