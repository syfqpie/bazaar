import type BaseModel from './base.model';

/** Interface for CustomerAddress */
export interface CustomerAddress extends BaseModel {
    /** Related customer ID */
    customer: number,

    /** Receiver's name */
    name: string,

    /** Receiver's phone no. */
    phoneNo: string,

    /** Is address default? */
    isDefault: boolean,

    /** Instructions */
    instructions: string,

    /** Address */
    address: string,

    /** Zipcode */
    zipcode: string,

    /** City */
    city: string,

    /** State */
    state: string,

    /** Country */
    country: string
}