/** Base interface for variant input */
export interface VariantBaseInput {
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

/** Input interface for add variant list */
export interface AddVariantList extends VariantBaseInput {
    /** List index */
    idx: number
}