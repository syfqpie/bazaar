import { APIService } from '@/common/api'
import type { LoginInput, LoginResponse } from '@/common/models/auth/auth.model'
import { defineStore } from 'pinia'

const BASE_PREFIX = 'auth'

/**
 * Authentication store
 */
export const useAuthStore = defineStore('auth', {
    state: () => ({}),
    getters: {},
    actions: {
        /**
         * Login to system
         * 
         * @param payload - payload
         * @param payload.username - user's email or username
         * @param payload.password - user's password
         * @returns Token
         */
        login(payload: LoginInput): Promise<LoginResponse> {
            return new Promise((resolve, reject) => {
                APIService.post(`${ BASE_PREFIX }/login`, payload)
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