import { defineStore } from 'pinia'

import { APIService } from '@/common/api'
import type { CustomerAddress } from '@/common/models/address.model'
import { V1_PREFIX } from './prefix';

const BASE_ENDPOINT = `${ V1_PREFIX }/addresses`

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
        /**
         * Create address
         * 
         * @param payload - payload
         * 
         * @return new created address
         */
        create(payload: any): Promise<CustomerAddress> {
            return new Promise((resolve, reject) => {
                APIService.post(`${ BASE_ENDPOINT }`, payload)
                    .then(({ data }) => {
                        resolve(data)
                        this.address = data

                        // Append value to state.
                        // Adding this response to the state
                        // rather than fetching all data again
                        // to avoid API called too many times.
                        // Cost saving?
                        this.addresses.unshift(this.address!)
                    })
                    .catch(err => {
                        reject(err)
                    })
            })
        },
        /**
         * List addresses
         * 
         * @param query - query paramaters
         * 
         * @return list of addresses
         */
        list(query: string | null = null): Promise<CustomerAddress[]> {
            return new Promise((resolve, reject) => {
                APIService.get(`${ BASE_ENDPOINT }`, query)
                    .then(({ data }) => {
                        resolve(data)

                        this.addresses = data
                    })
                    .catch(err => {
                        reject(err)
                    })
            })
        },
    }
})