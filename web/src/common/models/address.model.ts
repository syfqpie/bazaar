import type BaseModel from './base.model';

/** Interface for CustomerAddress */
export interface CustomerAddress extends BaseModel {
    /** Related customer ID */
    customer: number,

    /** Receiver's name */
    name: string,

    /** Receiver's phone no. */
    phoneNo: string,

    /** Address */
    address: string,

    /** District */
    district: string,

    /** Zipcode */
    zipcode: string,

    /** City */
    city: string,

    /** State */
    state: string,

    /** Country */
    country: string
}