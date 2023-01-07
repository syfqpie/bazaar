import type { VariantInput } from './variant.model';

/** Base interface for Product  */
export interface ProductBase {
    /** Product's name */
    name: string | null,

    /** Product's description */
    description: string | null
}

/** Input interface for Product */
export interface ProductInput extends ProductBase {
    /** Product's categories */
    category: number[],

    /** Publish product and variants? */
    isPublish: boolean,

    /** Product's variants */
    variants: VariantInput[]
}

/** Core interface for Product */
export interface Product extends ProductBase {
    /** Product's db id */
    id: number,

    /** Product's name */
    name: string,

    /** Product's slug */
    slug: string,

    /** Product's description */
    description: string,

    /** Product's categories */
    category: number[],

    /** Product's rating */
    rating: number | null,

    /** Is product active? */
    isActive: boolean,

    /** Product's created datetime */
    createdAt: string,

    /** Product's last modified datetime */
    lastModifiedAt: string
}