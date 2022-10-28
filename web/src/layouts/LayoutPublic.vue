<template>
    <div
        class="h-screen bg-neutral-100"
        :class="{
            'overflow-hidden': cartStore.isCartDrawerOpen
        }">
        
        <NavbarPublic />
        <RouterView />
        <FooterGeneral />

        <Transition
            enter-from-class="transition-transform translate-x-full"
            enter-active-class="duration-300"
            enter-to-class="transform-none"
            leave-from-class="transform-none"
            leave-active-class="duration-300"
            leave-to-class="transition-transform translate-x-full">
            <DrawerMenu v-if="cartStore.isCartDrawerOpen" />
        </Transition>

        <Transition
            enter-from-class="opacity-0"
            leave-to-class="opacity-0"
            enter-active-class="transition duration-300"
            leave-active-class="transition duration-300">
            <div v-if="cartStore.isCartDrawerOpen"
                class="bg-gray-900 bg-opacity-50 fixed
                inset-0 z-30 transform-none">
            </div>
        </Transition>
    </div>
</template>


<script lang="ts">
import { onMounted, defineComponent } from 'vue'

import DrawerMenu from '@/components/DrawerMenu.vue'
import FooterGeneral from '@/components/footers/FooterGeneral.vue'
import NavbarPublic from '@/components/navbars/NavbarPublic.vue'
import { useCartStore } from '@/stores'

export default defineComponent({
    name: 'LayoutPublic',
    setup() {
        const cartStore = useCartStore()

        onMounted(() => {
            // console.log('Mounted LayoutPublic')
        })

        return {
            cartStore
        }
    },
    components: {
        DrawerMenu,
        FooterGeneral,
        NavbarPublic
    }
})
</script>