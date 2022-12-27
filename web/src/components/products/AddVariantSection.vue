<template>
    <div class="mb-3">
        <div
            v-for="(item, index) in variants"
            :key="item.idx"
            class="p-2 bg-white
            border-[1px] mb-2 rounded-lg">
            <div
                class="grid grid-cols-12 gap-4
                text-gray-500">
                <div class="col-start-1 col-span-9 my-auto">
                    <p class="text-sm">
                        {{ index + 1 }}.
                        <span class="italic">
                            <span v-if="item.name">
                                {{ item.name }}
                            </span>

                            <span v-else>
                                Name not available
                                <span class="text-sm font-extralight">
                                    *will use product name as default
                                </span>
                            </span>
                        </span>
                    </p>
                </div>

                <div class="col-span-3">
                    <div class="flex-auto text-end">
                        <i
                            v-if="!item.name && !item.price"
                            class="fa-solid mr-3 text-sm
                            fa-triangle-exclamation">
                        </i>

                        <div
                            role="group"
                            class="inline-flex rounded-md
                            shadow-sm">
                            <TheOutlineButton
                                class="rounded-r-none"
                                size="sm"
                                :color="BasicColor.LIGHT"
                                @click="toggleDrawer(true, item)">
                                <i
                                    class="fa-solid
                                    fa-up-right-and-down-left-from-center">
                                </i>
                            </TheOutlineButton>

                            <TheOutlineButton
                                class="rounded-l-none border-l-0"
                                size="sm"
                                :color="BasicColor.LIGHT"
                                :disabled="(index === 0)"
                                @click="onRemoveVariant(index)">
                                <i class="fa-regular fa-trash-can"></i>
                            </TheOutlineButton>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <TheOutlineButton
            class="mt-1"
            :size="'sm'"
            @click="toggleDrawer()"> 
            <i class="fa-solid fa-circle-plus"></i>
            Add more
        </TheOutlineButton>

        <Transition
            enter-from-class="transition-transform translate-x-full"
            enter-active-class="duration-300"
            enter-to-class="transform-none"
            leave-from-class="transform-none"
            leave-active-class="duration-300"
            leave-to-class="transition-transform translate-x-full">
            <VariantDrawer 
                v-if="isDrawerOpen"
                :is-edit="isDrawerEdit"
                :variant-item="selectedItem"
                @on-toggle="toggleDrawer()"
                @on-save="onAddVariant"
                @on-update="onUpdateVariant" />
        </Transition>

        <Transition
            enter-from-class="opacity-0"
            leave-to-class="opacity-0"
            enter-active-class="transition duration-300"
            leave-active-class="transition duration-300">
            <div
                v-if="isDrawerOpen"
                class="bg-gray-900 bg-opacity-50 fixed
                inset-0 z-30 transform-none">
            </div>
        </Transition>
    </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue'

import TheInput from '@/components/basics/TheInput.vue'
import TheOutlineButton from '@/components/basics/TheOutlineButton.vue'
import VariantDrawer from './VariantDrawer.vue'
import { BasicColor } from '@/common/utility/basic.model'
import type { AddVariantList, VariantBaseInput } from '@/common/models/product.model'
import { useProductStore } from '@/stores'

export default defineComponent({
    name: 'AddVariantSection',
    setup() {
        // Data
        const variants = ref<AddVariantList[]>([])
        const selectedItem = ref<AddVariantList | null>(null)

        // Checker
        const isDrawerOpen = ref(false)
        const isDrawerEdit = ref(false)

        onMounted(() => {
            // console.log('Mounted AddVariantSection')
            addDefault()
        })

        // Services
        const productStore = useProductStore()

        /**
         * Add default variant.
         * Product need to have at least
         * one variant.
         */
        const addDefault = () => {
            const defVariant = {
                name: null,
                price: 0,
                quantity: 0,
                sku: null,
                weight: null,
                customerQuantityLimit: null
            }
            return variants.value.push(
                productStore.saveToArray(
                    defVariant,
                    variants.value.length
                )
            )
        }

        /**
         * Toggle drawer for edit or create
         * 
         * @param isEdit is drawer open to edit or no (create)?
         * @param current selected variant to edit
         */
        const toggleDrawer = (isEdit: boolean = false,
                              current: AddVariantList | null = null) => {
            // Pre toggle
            if (!isDrawerOpen.value) {
                isDrawerEdit.value = isEdit
                if (current) {
                    selectedItem.value = current
                }
            }

            // Toggle
            isDrawerOpen.value = !isDrawerOpen.value

            // Post toggle
            if (!isDrawerOpen.value) {
                isDrawerEdit.value = false
                selectedItem.value = null
            }
        }

        /**
         * Update variant
         * 
         * Replace current variant to new variant value in array
         * and toggle drawer
         * 
         * @param draftVariant variant new update
         * @param idx variant id
         */
        const onUpdateVariant = (draftVariant: VariantBaseInput, idx: number) => {
            variants.value.splice(idx, 1, { ...draftVariant, ...{ idx: idx } })
            toggleDrawer()
        }

        /**
         * Add new variant to array and
         * toggle drawer
         * 
         * @param draftVariant variant to add
         */
        const onAddVariant = (draftVariant: VariantBaseInput) => {
            variants.value.push(
                productStore.saveToArray(
                    draftVariant,
                    variants.value.length
                )
            )

            toggleDrawer()
        }

        /**
         * Remove variant
         * 
         * Remove variant from array and
         * trigger update list id
         * 
         * @param idx variant id
         */
        const onRemoveVariant = (idx: number) => {
            variants.value.splice(idx, 1)
            variants.value = updateListIdx()
        }

        /**
         * Update list id
         * 
         * Remap variant list ids
         */
        const updateListIdx = () => {
            return variants.value.map(
                (item, index) => {
                    return {
                        ...item,
                        ...{ idx: index }
                    }
                }
            )
        }

        return {
            BasicColor,
            variants,
            selectedItem,
            isDrawerOpen,
            isDrawerEdit,
            toggleDrawer,
            onUpdateVariant,
            onAddVariant,
            onRemoveVariant
        }
    },
    components: { 
        TheInput,
        TheOutlineButton,
        VariantDrawer
    }
})
</script>