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
            
            <button class="mt-1 group relative flex w-full justify-center
                rounded-lg p-2.5 border border-transparent outline-none
                font-medium text-sm shadow-none border-solid text-white 
                bg-green-400 border-green-400  active:bg-green-500 
                active:border-green-500 hover:shadow-md disabled:bg-green-300
                disabled:border-green-300 disabled:shadow-none
                disabled:cursor-not-allowed focus:outline-none focus:ring-2
                focus:ring-green-200 focus:hover:enabled:bg-green-500
                transition-all duration-150 ease-in-out"
                @click="cartStore.toggleOpen()">
                Proceed to checkout
            </button>
        </div>
    </div>
    
</template>

<script lang="ts">
import { onMounted, defineComponent, ref } from 'vue'

import { onClickOutside } from '@vueuse/core'

import { useCartStore } from '@/stores'

export default defineComponent({
    name: 'Drawer',
    setup() {
        // Component ref
        const cartDrawer = ref(null)

        // Services
        const cartStore = useCartStore()

        onMounted(() => {
            // console.log('Mounted Drawer')
        })

        // Event
        onClickOutside(cartDrawer, (event) => cartStore.toggleOpen())

        return {
            cartStore,
            cartDrawer
        }
    }
})
</script>