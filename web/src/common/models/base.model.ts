/**  Base interface for any model */
export default interface BaseModel {
    /** Database ID */
    id: number

    /** Is entry active? */
    isActive: boolean

    /** Entry creation date and time */
    createdAt: string

    /** Entry last modification date and time */
    lastModifiedAt: string
}