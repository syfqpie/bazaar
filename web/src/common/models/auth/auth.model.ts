/** Interface for login input */
export interface LoginInput {
    /** Username or email of user */
    username: string | null,

    /** User's password */
    password: string | null
}

/** Interface for email only input */
export interface EmailOnly {
    /** Related email */
    email: string | null
}

/** Interface for token only input */
export interface TokenOnly {
    /** Received token */
    token: string | null
}

/** Interface for change password input */
export interface ChangePassword {
    /** New password */
    newPassword1: string | null,

    /** Confirm new password */
    newPassword2: string | null
}

/** Interface for confirm reset password input */
export interface ResetPassword {
    /** New password */
    newPassword1: string | null,

    /** Confirm new password */
    newPassword2: string | null

    /** Received uid */
    id: number | null,

    /** Received token */
    token: string | null
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