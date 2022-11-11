<template>
    <button
        class="font-medium text-center text-white 
        bg-indigo-500 hover:bg-indigo-700 focus:outline
        focus:outline-2 focus:outline-indigo-300 transition-all
        ease-in duration-150 disabled:bg-indigo-300
        disabled:cursor-not-allowed"
        :class="{
            'w-full relative': isFull,
            'py-2 px-3': size === 'sm' || size === 'md',
            'p-3': size === 'lg',
            'text-xs': size === 'sm',
            'text-sm': size === 'md' || size === 'lg',
            'rounded-lg': !pill,
            'rounded-full': pill
        }">
        <slot>Button</slot>
    </button>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
    name: 'TheButton',
    setup() {
        return { }
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
        }
    }
})
</script>