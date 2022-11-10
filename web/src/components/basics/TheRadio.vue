<template>
    <input
        type="radio"
        class="w-4 h-4 accent-indigo-600 focus:ring-1 
        focus:ring-indigo-700 transition-all ease-in duration-150"
        id="{{ $attrs.id }}"
        name="{{ $attrs.name }}"
        :checked="$attrs.value === modelValue"
        :value="$attrs.value"
        @blur="$emit('blur')"
        @change="$emit('update:modelValue',
                      Number(($event.target as HTMLInputElement).value))" />
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
    name: 'TheRadio',
    setup() {
        return { }
    },
    props: ['modelValue']
})
</script>