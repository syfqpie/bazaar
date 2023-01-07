<template>
    <router-link
        :to="menuItem.path"
        class="flex items-center py-2 px-3 text-base
        font-normal rounded-lg text-gray-900
        hover:bg-gray-200 dark:text-gray-300 
        dark:hover:bg-gray-700 transition duration-100 ease-out"
        active-class="!text-indigo-500 dark:bg-gray-800">
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

import type { MenuItem } from '@/common/utility/menu.model'

export default defineComponent({
    name: 'SidebarMenuItem',
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