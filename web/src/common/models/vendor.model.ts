import type BaseModel from './base.model'

/** Interface for Vendor model */
export interface Vendor extends BaseModel {
    /** Vendor's name */
    name: string

    /** Vendor's description */
    description: string

    /** Vendor's phone no. */
    phoneNo: string

    /** Is vendor verified? */
    isVerified: string

    /** Vendor's related user ID */
    user: number

    /** Is newletter enabled? */
    isNewsletterEnabled: boolean
}