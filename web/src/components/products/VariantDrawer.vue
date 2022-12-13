<template>
    <div
        ref="variantDrawer"
        tabindex="-1"
        class="fixed z-40 h-screen overflow-y-hidden p-4 lg:p-6
        bg-white w-11/12 lg:w-[26rem] right-0 top-0">
        <h5 id="drawer-label" 
            class="inline-flex items-center mb-6 text-base font-semibold 
            text-gray-500 uppercase">
            {{  !isEdit ? 'New' : 'Edit' }} variant
        </h5>
        <button type="button"
            class="text-gray-400 bg-transparent hover:bg-gray-200 
            hover:text-gray-900 rounded-lg text-sm p-3 absolute
            top-2 right-2 lg:top-4 lg:right-4 inline-flex items-center"
            @click="emitToggle()">
            <i class="fa-solid fa-xmark"></i>
            <span class="sr-only">Close menu</span>
        </button>

        <div>
            <div class="mb-3">
                <label class="text-sm text-gray-700">
                    Variant name
                </label>
                <TheInput
                    type="text"
                    placeholder="Enter variant name" />
            </div>

            <div class="mb-3">
                <label class="text-sm text-gray-700">
                    SKU no.
                </label>
                <TheInput
                    type="text"
                    placeholder="Enter variant sku no." />
            </div>

            <div class="mb-3 grid grid-cols-2 gap-4">
                <div class="col-span-1">
                    <label class="text-sm text-gray-700">
                        Price
                    </label>
                    <TheInput
                        type="text"
                        :class="'p-2'"
                        placeholder="0.00" />
                </div>

                <div class="col-span-1">
                    <label class="text-sm text-gray-700">
                        Qty.
                    </label>
                    <TheInput
                        :type="'number'"
                        :class="'p-2'"
                        placeholder="0" />
                </div>
            </div>

            <div class="mb-3 grid grid-cols-2 gap-4">
                <div class="col-span-1">
                    <label class="text-sm text-gray-700">
                        Limit per customer
                    </label>
                    <TheInput
                        :type="'number'"
                        :class="'p-2'"
                        placeholder="0" />
                </div>

                <div class="col-span-1">
                    <label class="text-sm text-gray-700">
                        Weight
                    </label>
                    <TheInput
                        :type="'number'"
                        :class="'p-2'"
                        placeholder="0" />
                </div>
            </div>
        </div>

        <div class="sticky top-[90vh] py-4 lg:py-6">
            <TheButton 
                v-if="!isEdit"
                :size="'lg'"
                :is-full="true"
                @click="emitSave()"> 
                Save
            </TheButton>
        </div>
    </div>
</template>

<script lang="ts">
import { onMounted, defineComponent, ref } from 'vue'

import TheButton from '@/components/basics/TheButton.vue'
import TheInput from '@/components/basics/TheInput.vue'

import { onClickOutside } from '@vueuse/core'

export default defineComponent({
    name: 'VariantDrawer',
    setup(props, context) {
        // Component ref
        const variantDrawer = ref(null)

        onMounted(() => {
            // console.log('Mounted VariantDrawer')
        })

        const toSaveVariant = () => {
            const defVariant = {
                name: null,
                price: 0,
                quantity: 0,
                sku: undefined,
                weight: undefined,
                customerQuantityLimit: undefined
            }
            return defVariant
        }

        const emitSave = () => {
            context.emit('onSave', toSaveVariant())
        }

        const emitToggle = () => {
            context.emit('onToggle')
        }

        // Event
        onClickOutside(variantDrawer, (event) => {
            emitToggle()
        })

        return {
            variantDrawer,
            emitToggle,
            emitSave
        }
    },
    components: { TheButton, TheInput },
    props: {
        isEdit: {
            type: Boolean,
            default: false
        }
    },
    emits: ['onToggle', 'onSave']
})
</script>