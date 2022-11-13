/** Interface for User model */
export interface User {
    /** Database ID */
    id: number

    /** User's first name */
    firstName: string

    /** User's last name */
    lastName: string

    /** User's email */
    email: string

    /** User's type */
    userType: UserType

    /** Is user active? */
    isActive: boolean

    /** Is user staff */
    isStaff: string

    /** Is user superuser? */
    isSuperuser: boolean

    /** Last login date and time */
    lastLogin: string

    /** Joined date and time */
    dateJoined: string

    /** Entry last modification date and time */
    lastModifiedAt: string
}

/** Enum for UserType */
export enum UserType {
    /** Admin user type */
    Admin = 1,
    
    /** Vendor user type */
    Vendor = 2,

    /** Customer user type */
    Customer = 3
}