export interface GandalfItem {
    title: string,
    description?: string,
    isSkippable?: boolean
}

export interface GandalfInternal extends GandalfItem {
    idx: number | null,
    isVisited: boolean,
    isCompleted: boolean,
}

export interface GandalfConfig {
    current: number | null,
    next: number | null,
    previous: number | null,
    first: number | null,
    last: number | null,
    total: number
}