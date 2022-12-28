<template>
    <ul class="space-y-2">
        <li
            v-for="item of items"
            :key="item.path">
            <SidebarMenuItem
                v-if="item.type === MenuType.MENU"
                :menu-item="item" />
            
            <SidebarSubItem
                v-else-if="item.type === MenuType.SUB"
                :sub-item="item" />
        </li>
    </ul>
</template>

<script lang="ts">
import { onMounted, defineComponent } from 'vue'

import SidebarMenuItem from '@/components/sidebars/SidebarMenuItem.vue'
import SidebarSubItem from '@/components/sidebars/SidebarSubItem.vue'

import { MenuType, type MenuItem } from '@/common/utility/menu.model'

export default defineComponent({
    name: 'SidebarMenu',
    setup() { 
        onMounted(() => {
            // console.log('Mounted SidebarMenu')
        })

        return {
            MenuType
        }
    },
    props: {
        items: {
            type: Array as () => MenuItem[],
            default: []
        }
    },
    components: {
        SidebarMenuItem,
        SidebarSubItem
    }
})
</script>