<template>
    <div class="h-screen">
        <PublicNavbar />
        <RouterView />
    </div>
</template>


<script lang="ts">
import { onMounted, defineComponent } from 'vue'

import PublicNavbar from '@/components/navbars/PublicNavbar.vue'

export default defineComponent({
    name: 'PublicLayout',
    setup() {
        onMounted(() => {
            // console.log('Mounted PublicLayout')
        })

        return {}
    },
    components: {
        PublicNavbar
    }
})
</script>