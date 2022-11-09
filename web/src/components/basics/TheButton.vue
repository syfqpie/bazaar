<template>
    <button 
        class="block rounded-lg border border-transparent 
        bg-green-400 focus:hover:enabled:bg-green-500
        p-2.5 text-white enabled:bg-green-400
        focus:outline-none focus:ring-2 focus:ring-green-200
        font-medium text-sm disabled:bg-green-300
        disabled:border-green-300 disabled:shadow-none
        disabled:cursor-not-allowed">
        <slot>Button</slot>
    </button>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
    name: 'TheButton',
    setup() {

        return { }
    }
})
</script>