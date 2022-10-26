<template>
    <div class="w-full">
        <div class="p-4 sm:p-6 md:p-8 w-full bg-white
            rounded-lg border border-gray-200 shadow-sm">
            <h5 class="mb-0 text-base font-semibold text-gray-900 md:text-xl">
                Addresses
            </h5>
            <p class="text-sm font-normal text-gray-500 dark:text-gray-400 mb-3">
                Manage your saved addresses
            </p>

            <div class="grid grid-cols-2">
                <div class="p-4 w-full max-w-sm bg-white rounded-lg border shadow-sm sm:p-8">
                    <p class="font-semibold text-sm">John Doe</p>
                    <p class="text-sm font-light text-gray-500">+6018XXXXXXX</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { onMounted, defineComponent } from 'vue'

export default defineComponent({
    name: 'Address',
    setup() {
        onMounted(() => {
            // console.log('Mounted Address')
        })

        return {}
    }
})
</script>