import { APIService } from '@/common/api'
import type {
    ChangePassword,
    DetailResponse,
    EmailOnly,
    LoginInput,
    LoginResponse,
    ResetPassword,
    TokenOnly } from '@/common/models/auth/auth.model'
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
        /**
         * Resend verification email
         * 
         * @param payload - payload
         * @param payload.email - user's email
         * @returns Detail message
         */
        resendVerification(payload: EmailOnly): Promise<DetailResponse> {
            return new Promise((resolve, reject) => {
                APIService.post(`${ BASE_PREFIX }/resend-verification`, payload)
                    .then(({ data }) => {
                        resolve(data)
                    })
                    .catch(err => {
                        reject(err)
                    })
            })
        },
        /**
         * Resend verification email
         * 
         * @param payload - payload
         * @param payload.token - received token
         * @returns Detail message
         */
        verifyAccount(payload: TokenOnly): Promise<DetailResponse> {
            return new Promise((resolve, reject) => {
                APIService.post(`${ BASE_PREFIX }/verify-email`, payload)
                    .then(({ data }) => {
                        resolve(data)
                    })
                    .catch(err => {
                        reject(err)
                    })
            })
        },
        /**
         * Change account password
         * 
         * @param payload - payload
         * @param payload.newPassword1 - new password
         * @param payload.newPassword2 - confirm new password
         * @returns Detail message
         */
        changePassword(payload: ChangePassword): Promise<DetailResponse> {
            return new Promise((resolve, reject) => {
                APIService.post(`${ BASE_PREFIX }/password/change`, payload)
                    .then(({ data }) => {
                        resolve(data)
                    })
                    .catch(err => {
                        reject(err)
                    })
            })
        },
        /**
         * Request reset account password
         * 
         * @param payload - payload
         * @param payload.email - user's email
         * @returns Detail message
         */
        requestReset(payload: EmailOnly): Promise<DetailResponse> {
            return new Promise((resolve, reject) => {
                APIService.post(`${ BASE_PREFIX }/password/reset`, payload)
                    .then(({ data }) => {
                        resolve(data)
                    })
                    .catch(err => {
                        reject(err)
                    })
            })
        },
        /**
         * Reset account password
         * 
         * @param payload - payload
         * @param payload.newPassword1 - new password
         * @param payload.newPassword2 - confirm new password
         * @param payload.uid - received uid
         * @param payload.token - received token
         * @returns Detail message
         */
        resetPassword(payload: ResetPassword): Promise<DetailResponse> {
            return new Promise((resolve, reject) => {
                APIService.post(`${ BASE_PREFIX }/password/reset/confirm`, payload)
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