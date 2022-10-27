<template>
    <div class="h-screen bg-neutral-100"
        :class="{
            'overflow-hidden': cartStore.isCartDrawerOpen
        }">
        
        <PublicNavbar />
        <RouterView />
        <GeneralFooter />

        <Transition enter-from-class="transition-transform translate-x-full"
            enter-active-class="duration-300"
            enter-to-class="transform-none"
            leave-from-class="transform-none"
            leave-active-class="duration-300"
            leave-to-class="transition-transform translate-x-full" >
            <Drawer v-if="cartStore.isCartDrawerOpen" />
        </Transition>

        <Transition
            enter-from-class="opacity-0"
            leave-to-class="opacity-0"
            enter-active-class="transition duration-300"
            leave-active-class="transition duration-300">
            <div v-if="cartStore.isCartDrawerOpen"
                class="bg-gray-900 bg-opacity-50 dark:bg-opacity-80 fixed inset-0 z-30 transform-none">
            </div>
        </Transition>
    </div>
</template>


<script lang="ts">
import { onMounted, defineComponent } from 'vue'

import Drawer from '@/components/Drawer.vue'
import GeneralFooter from '@/components/footers/GeneralFooter.vue'
import PublicNavbar from '@/components/navbars/PublicNavbar.vue'
import { useCartStore } from '@/stores'

export default defineComponent({
    name: 'PublicLayout',
    setup() {
        const cartStore = useCartStore()

        onMounted(() => {
            // console.log('Mounted PublicLayout')
        })

        return {
            cartStore
        }
    },
    components: {
        Drawer,
        GeneralFooter,
        PublicNavbar
    }
})
</script>