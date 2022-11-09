<template>
    <button
        class="py-2 px-3 text-sm font-medium text-center
        text-white bg-indigo-500 rounded-lg hover:bg-indigo-700
        focus:outline focus:outline-2 focus:outline-none
        transition-all ease-in duration-150 disabled:bg-indigo-300
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