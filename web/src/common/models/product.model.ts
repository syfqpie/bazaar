/** Base interface for variant input */
export interface VariantInput {
    /** Variant's name */
    name: string | null,

    /** Variant's price */
    price: number | null,

    /** Variant's quantity */
    quantity: number | null,

    /** Variant's sku no. */
    sku: string | null,

    /** Variant's  weight */
    weight: number | null,

    /** Variant's quantity limit for customer */
    customerQuantityLimit: number | null
}

/** Base interface for product input  */
export interface ProductInput {
    /** Product's name */
    name: string | null,

    /** Product's description */
    description: string | null,

    /** Product's categories */
    category: number[],

    /** Publish product and variants? */
    is_publish: boolean,

    /** Product's variants */
    variants: VariantInput[]
}