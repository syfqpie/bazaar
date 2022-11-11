<template>
    <div class="w-full">
        <div
            class="grid place-items-center min-h-[30rem]
            p-4 sm:p-6 md:p-8 rounded-lg border bg-white
            border-gray-200 shadow-sm">
            <p
                class="text-sm font-normal text-gray-500
                dark:text-gray-400 mb-3 align-middle">
                System info goes here
            </p>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent, onMounted } from 'vue'

export default defineComponent({
    name: 'TheSystem',
    setup() {
        onMounted(() => {
            // console.log('Mounted TheSystem')
        })

        return {}
    }
})
</script>