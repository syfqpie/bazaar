<template>
    <input
        type="checkbox"
        class="w-4 h-4 accent-indigo-600 focus:ring-1 
        focus:ring-indigo-700 transition-all ease-in duration-150"
        :checked="$attrs.value === modelValue"
        :value="$attrs.value"
        @blur="$emit('blur')"
        @change="$emit('update:modelValue',
                      Boolean(($event.target as HTMLInputElement).checked))" />
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
    name: 'TheCheckbox',
    setup() {
        return { }
    },
    props: ['modelValue']
})
</script>