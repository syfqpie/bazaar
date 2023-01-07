<template>
    <section
        class="container mx-auto py-12 
        max-w-7xl px-2 sm:px-6 lg:px-8
        min-h-screen">
        <h5
            class="mb-0 text-base font-semibold 
            text-gray-900 md:text-xl">
            My product list
        </h5>

        <p
            class="text-sm font-normal text-gray-500
            dark:text-gray-400">
            List of all my saved products
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
import { useToast } from 'vue-toastification'

export default defineComponent({
    name: 'ProductList',
    setup() {
        // Checker
        const isLoading = ref(false)

        // Services
        const route = useRoute()
        const toast = useToast()
        const productStore = useProductStore()

        onMounted(() => {
            if (productStore.$state.products.length === 0) {
                getData()
            }
        })

        const getData = () => {
            isLoading.value = true
            productStore.list()
                        .then(() => {
                            isLoading.value = false
                            toast.info('Loaded products')
                            console.log(productStore.$state.products)
                        })
                        .catch(() => {
                            isLoading.value = false
                            toast.error('Error fetching products')
                        })
        }
        
        return {
            productStore
        }
    }
})
</script>