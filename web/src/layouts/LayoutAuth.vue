<template>
    <div class="h-screen bg-gray-100 px-4 sm:px-0">
        <div class="grid grid-cols-1 sm:grid-cols-6 sm:gap-0 h-full content-center">
            <div class="sm:col-start-2 sm:col-span-4">
                <div class="grid grid-cols-1 sm:grid-cols-2 bg-white
                    gap-0 rounded-lg overflow-hidden shadow-lg">
                    <div class="bg-indigo-500 hidden sm:block"></div>

                    <div>
                        <RouterView />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { onMounted, defineComponent } from 'vue'

export default defineComponent({
    name: 'LayoutAuth',
    setup() {
        onMounted(() => {
            // console.log('Mounted LayoutAuth')
        })

        return {}
    }
})
</script>