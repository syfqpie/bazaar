<template>
    <div>
        <NavbarPublic />
        <RouterView />
        <!-- <GeneralFooter /> -->
    </div>
</template>


<script lang="ts">
import { onMounted, defineComponent } from 'vue'

import NavbarPublic from '@/components/navbars/PublicNavbar.vue'
// import GeneralFooter from '@/components/footers/GeneralFooter.vue'

export default defineComponent({
    name: 'PublicLayout',
    setup() {
        onMounted(() => {
            // console.log('Mounted PublicLayout')
        })

        return {}
    },
    components: {
        NavbarPublic,
        // GeneralFooter
    }
})
</script>