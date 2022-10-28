import { defineStore } from 'pinia'

import type { CustomerAddress } from '@/common/models/address.model'

/**
 * CustomerAddress store
*/
export const useAddressStore = defineStore('address', {
    state: () => ({
        address: null as CustomerAddress | null,
        addresses: [] as CustomerAddress[]
    }),
    getters: {},
    actions: {
        list() {}
    }
})