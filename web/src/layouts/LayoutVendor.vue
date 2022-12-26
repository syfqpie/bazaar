<template>
    <div class="min-h-screen bg-gray-100">
        <div class="flex">
            <SidebarVendor class="flex-none sticky top-0 h-screen" />
            <div class="flex-auto bg-white">
                <RouterView />
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { onMounted, defineComponent } from 'vue'

import SidebarVendor from '@/components/sidebars/SidebarVendor.vue'

export default defineComponent({
    name: 'LayoutVendor',
    setup() {
        onMounted(() => {
            // console.log('Mounted LayoutVendor')
        })

        return {}
    },
    components: {
        SidebarVendor
    }
})
</script>