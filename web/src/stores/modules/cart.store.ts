import { defineStore } from 'pinia'

/**
 * Cart store
 */
export const useCartStore = defineStore('cart', {
    state: () => ({
        isCartDrawerOpen: false
    }),
    getters: { },
    actions: {
        /** Toggle cart */
        toggleOpen() {
            return this.isCartDrawerOpen = !this.isCartDrawerOpen
        }
    }
})