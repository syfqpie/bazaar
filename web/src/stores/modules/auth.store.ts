import { APIService } from '@/common/api'
import type {
    ChangePasswordInput,
    EmailOnlyInput,
    LoginInput,
    RegisterCustomerInput,
    RegisterVendorInput,
    ResetPasswordInput,
    VerifyAccountInput,
    DetailResponse,
    LoginResponse } from '@/common/models/auth.model'
import { defineStore } from 'pinia'

const BASE_PREFIX = 'auth'
const BASE_REGISTRATION = `${ BASE_PREFIX }/registration`
const BASE_PASSWORD = `${ BASE_PREFIX }/password`

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
         * Register vendor
         * 
         * @param payload - payload
         * @param payload.username - vendor's email or username
         * @param payload.name - vendor's name
         * @param payload.phoneNo - vendor's phone no.
         * @returns Detail message
         */
        registerVendor(payload: RegisterVendorInput): Promise<DetailResponse> {
            return new Promise((resolve, reject) => {
                APIService.post(`${ BASE_REGISTRATION }/vendor`, payload)
                    .then(({ data }) => {
                        resolve(data)
                    })
                    .catch(err => {
                        reject(err)
                    })
            })
        },
        /**
         * Register customer
         * 
         * @param payload - payload
         * @param payload.username - customer's email or username
         * @param payload.firstName - customer's first name
         * @param payload.lastName - customer's last name
         * @param payload.phoneNo - customer's phone no.
         * @param payload.dateOfBirth - customer's date of birth
         * @returns Detail message
         */
         registerCustomer(payload: RegisterCustomerInput): Promise<DetailResponse> {
            return new Promise((resolve, reject) => {
                APIService.post(`${ BASE_REGISTRATION }/customer`, payload)
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
        resendVerification(payload: EmailOnlyInput): Promise<DetailResponse> {
            return new Promise((resolve, reject) => {
                APIService.post(`${ BASE_REGISTRATION }/resend-verification`, payload)
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
         * @param payload.key - received token
         * @param payload.newPassword1 - new password
         * @param payload.newPassword2 - confirm new password
         * @returns Detail message
         */
        verifyAccount(payload: VerifyAccountInput): Promise<DetailResponse> {
            return new Promise((resolve, reject) => {
                APIService.post(`${ BASE_REGISTRATION }/verify-email`, payload)
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
        changePassword(payload: ChangePasswordInput): Promise<DetailResponse> {
            return new Promise((resolve, reject) => {
                APIService.post(`${ BASE_PASSWORD }/change`, payload)
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
        requestReset(payload: EmailOnlyInput): Promise<DetailResponse> {
            return new Promise((resolve, reject) => {
                APIService.post(`${ BASE_PASSWORD }/reset`, payload)
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
        resetPassword(payload: ResetPasswordInput): Promise<DetailResponse> {
            return new Promise((resolve, reject) => {
                APIService.post(`${ BASE_PASSWORD }/reset/confirm`, payload)
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