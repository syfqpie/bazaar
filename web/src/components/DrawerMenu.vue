<template>
    <div ref="cartDrawer"
        tabindex="-1"
        class="fixed z-40 h-screen overflow-y-hidden p-4 lg:p-6
        bg-white w-11/12 lg:w-[28rem] right-0 top-0">
        <h5 id="drawer-label" 
            class="inline-flex items-center mb-6 text-base font-semibold 
            text-gray-500 uppercase">
            Shopping cart
        </h5>
        <button type="button"
            class="text-gray-400 bg-transparent hover:bg-gray-200 
            hover:text-gray-900 rounded-lg text-sm p-3 absolute
            top-2 right-2 lg:top-4 lg:right-4 inline-flex items-center"
            @click="cartStore.toggleOpen()">
            <i class="fa-solid fa-xmark"></i>
            <span class="sr-only">Close menu</span>
        </button>

        <div class="flex h-[calc(100vh-14rem)] align-middle items-center justify-center">
            <img src="@/assets/img/icons/shopping-cart.png"
                class="h-auto w-32 opacity-40"
                alt="Empty" />
        </div>

        <div class="sticky top-[100vh] py-4 lg:py-6">
            <div class="flex justify-between text-sm font-medium mb-3">
                <span>Total (0 item):</span>
                <span>RM0.00</span>
            </div>

            <TheButton 
                :size="'lg'"
                :is-full="true"
                @click="cartStore.toggleOpen()"> 
                Process to checkout
            </TheButton>
        </div>
    </div>
</template>

<script lang="ts">
import { onMounted, defineComponent, ref } from 'vue'

import TheButton from './basics/TheButton.vue'
import { useCartStore } from '@/stores'

import { onClickOutside } from '@vueuse/core'

export default defineComponent({
    name: 'DrawerMenu',
    setup() {
        // Component ref
        const cartDrawer = ref(null)

        // Services
        const cartStore = useCartStore()

        onMounted(() => {
            // console.log('Mounted DrawerMenu')
        })

        // Event
        onClickOutside(cartDrawer, (event) => cartStore.toggleOpen())

        return {
            cartStore,
            cartDrawer
        }
    },
    components: { TheButton }
})
</script>