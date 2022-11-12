<template>
    <button
        class="font-medium text-center text-gray-900 
        border transition-all ease-in duration-150
        hover:text-white focus:outline focus:outline-2
        disabled:cursor-not-allowed"
        :class="{
            'w-full relative': isFull,
            'py-2 px-3': size === 'sm' || size === 'md',
            'p-3': size === 'lg',
            'text-xs': size === 'sm',
            'text-sm': size === 'md' || size === 'lg',
            'rounded-lg': !pill,
            'rounded-full': pill,
            'border-indigo-500 text-indigo-500 \
            hover:bg-indigo-500 focus:outline-indigo-300 \
            disabled:bg-indigo-300': color === BasicColor.DEFAULT,
            'border-green-500 text-green-500 \
            hover:bg-green-500 focus:outline-green-300 \
            disabled:bg-green-300': color === BasicColor.SUCCESS,
            'border-sky-500 text-sky-500 \
            hover:bg-sky-500 focus:outline-sky-300 \
            disabled:bg-sky-300': color === BasicColor.INFO,
            'border-yellow-500 text-yellow-500 \
            hover:bg-yellow-500 focus:outline-yellow-300 \
            disabled:bg-yellow-300': color === BasicColor.WARNING,
            'border-red-500 text-red-500 \
            hover:bg-red-500 focus:outline-red-300 \
            disabled:bg-red-300': color === BasicColor.DANGER,
        }">
        <slot>Button</slot>
    </button>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import { BasicColor } from '@/common/utility/basic.model'

export default defineComponent({
    name: 'TheOutlineButton',
    setup() {
        return {
            BasicColor
        }
    },
    props: {
        isFull: {
            type: Boolean,
            default: false
        },
        size: {
            type: String,
            default: 'md'
        },
        pill: {
            type: Boolean,
            default: false
        },
        color: {
            type: String,
            default: BasicColor.DEFAULT
        }
    }
})
</script>