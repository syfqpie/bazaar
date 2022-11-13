import { defineStore } from 'pinia'

import { APIService } from '@/common/api'
import type { User } from '@/common/models/user.model'
import { AUTH_PREFIX } from './prefix';

const BASE_ENDPOINT = `${ AUTH_PREFIX }/users`

export const useUserStore = defineStore('user', {
    state: () => ({
        user: null as User | null,
        users: [] as User[]
    }),
    getters: {
        user: (state) => state.user,
        users: (state) => state.users
    },
    actions: {
        /**
         * List users
         * 
         * @param query - query paramaters
         * 
         * @return list of users
        */
        list(query: string | null = null): Promise<User> {
            return new Promise((resolve, reject) => {
                APIService.get(`${ BASE_ENDPOINT }`, query)
                    .then(({ data }) => {
                        resolve(data)
                    })
                    .catch(err => {
                        reject(err)
                    })
            })
        },
        /**
         * Retrieve a user
         * 
         * @param id - user ID
         * 
         * @return a user
        */
        retrieve(id: number): Promise<User> {
            return new Promise((resolve, reject) => {
                APIService.get(`${ BASE_ENDPOINT }/${ id }`)
                    .then(({ data }) => {
                        resolve(data)
                    })
                    .catch(err => {
                        reject(err)
                    })
            })
        },

    }
})