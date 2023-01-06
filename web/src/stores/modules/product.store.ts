import { defineStore } from 'pinia'

import type { AddVariantList, VariantBaseInput } from '@/common/models/product.model'

/**
 * Product store
 */
export const useProductStore = defineStore('product', {
    state: () => ({
        isAddDrawerOpen: false
    }),
    getters: { },
    actions: {
        /** Toggle add product drawer */
        toggleAddOpen() {
            return this.isAddDrawerOpen = !this.isAddDrawerOpen
        },
        /** Save new variant to add variant list */
        saveToArray(payload: VariantBaseInput, nextIndex: number): AddVariantList {
            const index = { idx: nextIndex }
            const newVariant = {
                ...index,
                ...payload
            }

            return newVariant
        }
    }
})