/** Interface for change password input */
export interface ChangePasswordInput {
    /** New password */
    newPassword1: string | null,

    /** Confirm new password */
    newPassword2: string | null
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
export interface ResetPasswordInput extends ChangePasswordInput {
    /** Received uid */
    uid: number | null,

    /** Received token */
    token: string | null
}

/** Interface for verify account input */
export interface VerifyAccountInput extends ChangePasswordInput {
    /** Received token */
    key: string | null
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