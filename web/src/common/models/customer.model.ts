import type BaseModel from './base.model'

/** Interface for Customer model */
export interface Customer extends BaseModel {
    /** Customer's name */
    name: string

    /** Customer's phone no. */
    phoneNo: string

    /** Customer's gender */
    gender: string

    /** Customer's date of birth */
    dateOfBirth: string

    /** Customer's related user ID */
    user: number

    /** Is newletter enabled? */
    isNewsletterEnabled: boolean
}

/** Enum for GenderType */
export enum GenderType {
    /** Male gender type */
    MALE = 1,
    
    /** Female gender type */
    FEMALE = 2,
    
    /** Secret gender type */
    SECRET = 3
}