/** Interface for login input */
export interface LoginInput {
    /** Username or email of user */
    username: string | null,

    /** User's password */
    password: string | null
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