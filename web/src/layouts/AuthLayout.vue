<template>
    <div class="h-screen bg-gray-100">
        <div class="grid grid-cols-6 gap-0 h-full content-center">
            <div class="col-start-2 col-span-4">
                <div class="grid grid-cols-1 sm:grid-cols-2 bg-white
                    gap-0 rounded-lg overflow-hidden shadow-lg">
                    <div class="bg-green-400 hidden sm:block"></div>

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
    name: 'AuthLayout',
    setup() {
        onMounted(() => {
            // console.log('Mounted AuthLayout')
        })

        return {}
    }
})
</script>