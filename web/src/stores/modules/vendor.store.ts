import { defineStore } from 'pinia'

import { APIService } from '@/common/api'
import type { Vendor } from '@/common/models/vendor.model'
import { V1_PREFIX } from './prefix';

const BASE_ENDPOINT = `${ V1_PREFIX }/vendors`

export const useVendorStore = defineStore('vendor', {
    state: () => ({
        vendor: null as Vendor | null,
        vendors: [] as Vendor[]
    }),
    actions: {
        /**
         * List vendors
         * 
         * @param query - query paramaters
         * 
         * @return list of vendors
        */
        list(query: string | null = null): Promise<Vendor[]> {
            return new Promise((resolve, reject) => {
                APIService.get(`${ BASE_ENDPOINT }`, query)
                    .then(({ data }) => {
                        resolve(data)

                        this.vendors = data
                    })
                    .catch(err => {
                        reject(err)
                    })
            })
        },
        /**
         * Retrieve a vendor
         * 
         * @param id - vendor ID
         * 
         * @return a vendor
        */
        retrieve(id: number): Promise<Vendor> {
            return new Promise((resolve, reject) => {
                APIService.get(`${ BASE_ENDPOINT }/${ id }`)
                    .then(({ data }) => {
                        resolve(data)

                        this.vendor = data
                    })
                    .catch(err => {
                        reject(err)
                    })
            })
        },
        /**
         * Patch a vendor
         * 
         * @param id - vendor ID
         * @param payload - payload
         * 
         * @return an updated vendor
        */
        patch(id: number, payload: any): Promise<Vendor> {
            return new Promise((resolve, reject) => {
                APIService.patch(`${ BASE_ENDPOINT }/${ id }`, payload)
                    .then(({ data }) => {
                        resolve(data)

                        this.vendor = data
                    })
                    .catch(err => {
                        reject(err)
                    })
            })
        }
    }
})