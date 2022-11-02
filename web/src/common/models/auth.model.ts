import type { UserType } from './user.model'

/** Base interface for change password */
export interface ChangePasswordBaseInput {
    /** New password */
    newPassword1: string | null,

    /** Confirm new password */
    newPassword2: string | null
}

/** Interface for change password input */
export interface ChangePasswordInput extends ChangePasswordBaseInput {
    /** Old password */
    oldPassword: string | null
}

/** Interface for email only input */
export interface EmailOnlyInput {
    /** Related email */
    email: string | null
}

/** Interface for login input */
export interface LoginInput {
    /** Username or email of user */
    username: string | null,

    /** User's password */
    password: string | null
}

/** Interface for refresh token input */
export interface RefreshTokenInput {
    /** Current refresh token */
    refresh: string | null
}

/** Interface for register customer input */
export interface RegisterCustomerInput {
    /** Related email */
    username: string | null,

    /** Customer first name */
    firstName: string | null,

    /** Customer last name */
    lastName: string | null,

    /** Customer phone number */
    phoneNo: string | null,

    /** Customer date of birth */
    dateOfBirth: string | null
}

/** Interface for register vendor input */
export interface RegisterVendorInput {
    /** Related email */
    username: string | null,

    /** Vendor name */
    name: string | null,

    /** Vendor phone number */
    phoneNo: string | null
}

/** Interface for confirm reset password input */
export interface ResetPasswordInput extends ChangePasswordBaseInput {
    /** Received uid */
    uid: number | null,

    /** Received token */
    token: string | null
}

/** Interface for verify account input */
export interface VerifyAccountInput extends ChangePasswordBaseInput {
    /** Received token */
    key: string | null
}

export enum TokenType {
    Access = 'access',
    Refresh = 'refresh'
}

/** Interface for decoded token */
export interface TokenDecoded {
    /** Type of token  */
    tokenType?: TokenType,

    /** Token expiration unix timestamp  */
    exp?: number,

    /** Token issued unix timestamp  */
    iat?: number,

    /** Token unique identifier */
    jti?: string,

    /** User ID  */
    id?: number,

    /** User username  */
    username?: string,

    /** User email  */
    email?: string,

    /** User type */
    userType?: UserType,

    /** Related customer ID if any */
    customerId?: number,

    /** Related vendor ID if any */
    vendorId?: number
}

/** Interface for token refresh */
export interface TokenRefresh {
    /** New access token */
    access: string,

    /** New refresh token */
    refresh: string,

    /** New access token expiration date */
    accessTokenExpiration: string
}

/** Interface for login response */
export interface LoginResponse {
    /** Generated access token */
    accessToken: string,

    /** Generated refresh token */
    refreshToken: string,

    /** Short user information */
    user: AuthUser
}

/** Interface for detail response */
export interface DetailResponse {
    /** Detail */
    detail: string
}

/** Interface for auth user */
export interface AuthUser {
    /** User's database ID */
    pk: number,

    /** User's username or password */
    username: string,

    /** User's first name */
    firstName: string,

    /** User's last name */
    lastName: string
}
