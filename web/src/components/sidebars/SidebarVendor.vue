<template>
    <aside class="w-64" aria-label="Sidebar">
        <div
            class="overflow-y-auto py-12 px-3 h-screen
            bg-gray-50 dark:bg-gray-800">
            <SidebarMenu
                :items="menuItems"
                class="pb-4 border-b border-gray-200
                dark:border-gray-700" />
        </div>
    </aside>
</template>

<script lang="ts">
import type { MenuItem } from '@/common/utility/menu.model'
import { onMounted, defineComponent, ref } from 'vue'
import SidebarMenu from './SidebarMenu.vue'
import { MenuType } from '@/common/utility/menu.model'

export default defineComponent({
    name: 'SidebarVendor',
    setup() {
        const menuItems = ref<MenuItem[]>([
            { 
                title: 'Product',
                type: MenuType.SUB,
                path: '/vendor/products',
                icon: 'fa-solid fa-boxes-stacked',
                subMenuItem: [
                    {
                        title: 'Add new',
                        path: 'add'
                    }
                ]
            },
            { 
                title: 'Settings',
                type: MenuType.MENU,
                path: '/vendor/user/account/profile',
                icon: 'fa-solid fa-wrench'
            }
        ])
        onMounted(() => {
            // console.log('Mounted SidebarVendor')
        })

        return {
            menuItems
        }
    },
    components: {
        SidebarMenu
    }
})
</script>