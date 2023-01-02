import { defineStore } from 'pinia'

import { APIService } from '@/common/api'
import type { ProductInput } from '@/common/models/product.model'
import type { Variant, VariantInput } from '@/common/models/variant.model'
import { V1_PREFIX } from './prefix'

const BASE_ENDPOINT = `${ V1_PREFIX }/products`

/**
 * Product store
 */
export const useProductStore = defineStore('product', {
    state: () => ({
        product: null as  Variant | null,
        products: [] as Variant[],
        isAddDrawerOpen: false
    }),
    getters: { },
    actions: {
        /** Toggle add product drawer */
        toggleAddOpen() {
            return this.isAddDrawerOpen = !this.isAddDrawerOpen
        },
        /** Return generic product */
        getGenericProduct(): VariantInput {
            return {
                name: null,
                price: 0,
                quantity: 0,
                sku: null,
                weight: null,
                customerQuantityLimit: null
            }
        },
        /** Create new product */
        create(payload: ProductInput): Promise<Variant> {
            return new Promise((resolve, reject) => {
                APIService.post(BASE_ENDPOINT, payload)
                    .then(({ data }) => {
                        resolve(data)

                        this.$state.product = data
                    })
                    .catch(err => {
                        reject(err)
                    })
            })
        },
    }
})