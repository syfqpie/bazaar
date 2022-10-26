<template>
    <div class="h-screen">
        <PublicNavbar />
        <RouterView />
        <GeneralFooter />
    </div>
</template>


<script lang="ts">
import { onMounted, defineComponent } from 'vue'

import PublicNavbar from '@/components/navbars/PublicNavbar.vue'
import GeneralFooter from '@/components/footers/GeneralFooter.vue'

export default defineComponent({
    name: 'PublicLayout',
    setup() {
        onMounted(() => {
            // console.log('Mounted PublicLayout')
        })

        return {}
    },
    components: {
        PublicNavbar,
        GeneralFooter
    }
})
</script>