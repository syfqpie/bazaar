import type BaseModel from './base.model'

/** Interface for Category model */
export interface Category extends BaseModel {
    /** Category's name */
    name: string

    /** Category's slug */
    slug: string

    /** Category's description */
    description: string

    /** Category's parent ID */
    parent: number
}