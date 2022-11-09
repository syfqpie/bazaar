<template>
    <input
        type="checkbox"
        class="w-4 h-4 accent-indigo-600 focus:ring-1 
        focus:ring-indigo-700 transition-all ease-in duration-150" />
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
    name: 'TheCheckbox',
    setup() {
        return { }
    }
})
</script>