<template>
    <textarea
        class="mt-1 block w-full rounded-lg bg-gray-50
        border border-gray-300 text-gray-900
        text-sm p-2.5 focus:outline focus:outline-2
        focus:outline-indigo-200 focus:outline-offset-0
        focus:border-indigo-700"
        :class="$attrs.class"
        type="{{ $attrs.type }}"
        :value="modelValue" 
        @blur="$emit('blur')"
        @input="$emit('update:modelValue',
                      ($event.target as HTMLInputElement).value)"
    ></textarea>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
    name: 'TheTextArea',
    setup() {
        return { }
    },
    props: ['modelValue']
})
</script>