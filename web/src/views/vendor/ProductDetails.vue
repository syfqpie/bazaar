<template>
    <section
        class="container mx-auto py-12 
        max-w-7xl px-2 sm:px-6 lg:px-8
        min-h-screen">
        <h5
            class="mb-0 text-base font-semibold 
            text-gray-900 md:text-xl">
            Product details: 
            <!-- <span class="font-bold">
                {{  productStore.$state.product?.name  }}
            </span> -->
        </h5>

        <p
            class="text-sm font-normal text-gray-500
            dark:text-gray-400">
            Configure your product and variants here
        </p>

        <div
            class="flex flex-row align-middle items-center py-5">
            <div class="basis-full">
                <img
                    src="@/assets/img/icons/work-in-progress.png"
                    class="h-auto w-3/12 mx-auto opacity-60"
                    alt="Empty" />
            </div>
        </div>
    </section>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import { useProductStore } from '@/stores'

export default defineComponent({
    name: 'ProductDetails',
    setup() {
        // Data
        const productId = ref<number | null>(null)

        // Checker
        const isLoading = ref(false)

        // Services
        const route = useRoute()
        const productStore = useProductStore()

        onMounted(() => {
            productId.value = route.params['id'] ? Number(route.params['id']) : null

            const isProductFetched = productStore.$state.product &&
                                     productStore.$state.product.id === productId.value
            
            if (productId && !isProductFetched) {
                getData()
            }
        })

        const getData = () => {
            isLoading.value = true
            productStore.retrieve(productId.value!)
                        .then(() => {
                            isLoading.value = false
                            console.log(productStore.$state.product)
                        })
                        .catch(() => {
                            isLoading.value = false
                        })
        }
        
        return {
            productStore
        }
    }
})
</script>