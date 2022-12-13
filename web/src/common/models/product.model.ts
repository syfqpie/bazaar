/** Base interface for variant input */
export interface VariantBaseInput {
    /** Variant's name */
    name: string | null,

    /** Variant's price */
    price: number,

    /** Variant's quantity */
    quantity?: number,

    /** Variant's sku no. */
    sku?: string,

    /** Variant's  weight */
    weight?: number,

    /** Variant's quantity limit for customer */
    customerQuantityLimit?: number
}

/** Input interface for add variant list */
export interface AddVariantList extends VariantBaseInput {
    /** List index */
    idx: number
}