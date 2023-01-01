/** Base interface for Variant */
export interface VariantBase {
    /** Variant's sku no. */
    sku: string | null,
    
    /** Variant's name */
    name: string | null,

    /** Variant's price */
    price: number | null,

    /** Variant's  weight */
    weight: number | null,

    /** Variant's quantity limit for customer */
    customerQuantityLimit: number | null
}

/** Input interface for Variant */
export interface VariantInput extends VariantBase {
    /** Inventory quantity */
    quantity: number | null
}

/** Core interface for Variant */
export interface Variant extends VariantBase {
    /** Variant's db id */
    id: number,

    /** Variant's name */
    name: string,

    /** Variant's parent Product id */
    product: number,

    /** Variant's price */
    price: number,

    /** Is variant active? */
    isActive: boolean,

    /** Variant's created datetime */
    createdAt: string,

    /** Variant's last modified datetime */
    lastModifiedAt: string
}