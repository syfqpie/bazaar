import { defineStore } from 'pinia'

import { APIService } from '@/common/api'
import type { Category } from '@/common/models/category.model'
import { V1_PREFIX } from './prefix';

const BASE_ENDPOINT = `${ V1_PREFIX }/categories`

export const useCategoryStore = defineStore('category', {
    state: () => ({
        category: null as Category | null,
        categorys: [] as Category[]
    }),
    actions: {
        /**
         * List categorys
         * 
         * @param query - query paramaters
         * 
         * @return list of categorys
        */
        list(query: string | null = null): Promise<Category[]> {
            return new Promise((resolve, reject) => {
                APIService.get(`${ BASE_ENDPOINT }`, query)
                    .then(({ data }) => {
                        resolve(data)

                        this.categorys = data
                    })
                    .catch(err => {
                        reject(err)
                    })
            })
        },
        /**
         * Retrieve a category
         * 
         * @param id - category ID
         * 
         * @return a category
        */
        retrieve(id: number): Promise<Category> {
            return new Promise((resolve, reject) => {
                APIService.get(`${ BASE_ENDPOINT }/${ id }`)
                    .then(({ data }) => {
                        resolve(data)

                        this.category = data
                    })
                    .catch(err => {
                        reject(err)
                    })
            })
        },
        /**
         * Patch a category
         * 
         * @param id - category ID
         * @param payload - payload
         * 
         * @return an updated category
        */
        patch(id: number, payload: any): Promise<Category> {
            return new Promise((resolve, reject) => {
                APIService.patch(`${ BASE_ENDPOINT }/${ id }`, payload)
                    .then(({ data }) => {
                        resolve(data)

                        this.category = data
                    })
                    .catch(err => {
                        reject(err)
                    })
            })
        }
    }
})