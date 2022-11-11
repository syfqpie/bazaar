<template>
    <router-link
        :to="menuItem.path"
        class="flex items-center px-3 py-2 w-full text-sm font-medium
        rounded-lg transition duration-100 text-gray-500
        hover:text-indigo-500"
        active-class="text-indigo-500 bg-gray-200 hover:bg-gray-200">
        <i 
            class="fa-fw"
            :class="menuItem.icon">
        </i>
    
        <span class="flex-1 ml-2 text-left whitespace-nowrap">
            {{ menuItem.title }}
        </span>
    </router-link>
</template>

<script lang="ts">
import { defineComponent, onMounted } from 'vue'

import type { MenuItem } from '@/common/models/utility.model'

export default defineComponent({
    name: 'TheMenuItem',
    setup(prop) {
        onMounted(() => {
        })

        return { }
    },
    props: {
        menuItem: {
            type: Object as () => MenuItem,
            required: true
        }
    }
})
</script>