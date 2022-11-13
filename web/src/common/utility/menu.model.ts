/** Interface for sub menu item  */
export interface SubMenuItem {
    /** Item title */
    title: string,

    /** Item path */
    path: string
}

/** Interface for menu item */
export interface MenuItem {
    /** Menu item title */
    title: string

    /** Menu item type */
    type: MenuType

    /** Menu item path */
    path: string,

    /** Menu item icon */
    icon: string

    /** Submenu item(s) */
    subMenuItem?: SubMenuItem[]
}

/** Enum for GenderType */
export enum MenuType {
    /** Menu menu type */
    MENU = 1,

    /** Submenu menu type */
    SUB = 2
}