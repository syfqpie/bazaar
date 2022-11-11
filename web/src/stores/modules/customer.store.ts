import { defineStore } from 'pinia'

import { APIService } from '@/common/api'
import type { Customer } from '@/common/models/customer.model'
import { V1_PREFIX } from './prefix';

const BASE_ENDPOINT = `${ V1_PREFIX }/customers`

export const useCustomerStore = defineStore('customer', {
    state: () => ({
        customer: null as Customer | null,
        customers: [] as Customer[]
    }),
    actions: {
        /**
         * List customers
         * 
         * @param query - query paramaters
         * 
         * @return list of customers
        */
        list(query: string | null = null): Promise<Customer[]> {
            return new Promise((resolve, reject) => {
                APIService.get(`${ BASE_ENDPOINT }`, query)
                    .then(({ data }) => {
                        resolve(data)

                        this.customers = data
                    })
                    .catch(err => {
                        reject(err)
                    })
            })
        },
        /**
         * Retrieve a customer
         * 
         * @param id - customer ID
         * 
         * @return a customer
        */
        retrieve(id: number): Promise<Customer> {
            return new Promise((resolve, reject) => {
                APIService.get(`${ BASE_ENDPOINT }/${ id }`)
                    .then(({ data }) => {
                        resolve(data)

                        this.customer = data
                    })
                    .catch(err => {
                        reject(err)
                    })
            })
        },
        /**
         * Patch a customer
         * 
         * @param id - customer ID
         * @param payload - payload
         * 
         * @return an updated customer
        */
        patch(id: number, payload: any): Promise<Customer> {
            return new Promise((resolve, reject) => {
                APIService.patch(`${ BASE_ENDPOINT }/${ id }`, payload)
                    .then(({ data }) => {
                        resolve(data)

                        this.customer = data
                    })
                    .catch(err => {
                        reject(err)
                    })
            })
        }
    }
})