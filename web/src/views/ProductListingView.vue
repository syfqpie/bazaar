<template>
    <div class="w-full">
        <p>Product Listing</p>
    </div>
</template>

<script lang="ts">
import { onMounted, defineComponent } from 'vue'

export default defineComponent({
    name: 'ProductListing',
    setup() {
        onMounted(() => {
            // console.log('Mounted ProductListing')
        })

        return {}
    }
})
</script>