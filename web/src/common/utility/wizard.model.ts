/** Base interfce for Gandalf (the wizard) */
export interface GandalfItem {
    /** Item title */
    title: string,

    /** Item description */
    description?: string,

    /** Is item skippable? */
    isSkippable?: boolean
}

/** Interface for gandalf (the wizard) step */
export interface GandalfStep extends GandalfItem {
    /** Step index */
    idx: number,

    /** Is step visited? */
    isVisited: boolean,

    /** Is step completed? */
    isCompleted: boolean
}

/** Interface for gandalf (the wizard) config  */
export interface GandalfConfig {
    /** Current step index */
    current: number | null,

    /** Next step index */
    next: number | null,

    /** Previous step index */
    previous: number | null,

    /** First step index */
    first: number | null,

    /** Last step index */
    last: number | null,

    /** Total steps */
    total: number
}