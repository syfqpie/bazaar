<template>
    <aside
        class="w-64"
        :class="{ 'hidden': !isShow }">
        <div
            class="overflow-y-auto pt-3 pb-12 md:py-12 px-3 h-screen
            bg-gray-100 dark:bg-gray-800">
            <div class="grid grid-cols-2 pl-2 pr-4 mb-3 md:hidden">
                <div class="">
                    <img
                        class="block h-8 w-auto lg:hidden"
                        src="@/assets/img/default/trolley.png"
                        alt="Bazaar" />
                </div>

                <div class="flex">
                    <a
                        class="text-gray-300  my-auto ml-auto"
                        @click="toggleSidebar()">
                        <i class="fa-solid fa-bars"></i>
                    </a>
                </div>
            </div>

            <SidebarMenu
                :items="menuItems"
                class="pb-4 border-b border-gray-200
                dark:border-gray-700" />
        </div>
    </aside>
</template>

<script lang="ts">
import { onMounted, defineComponent, ref } from 'vue'

import { MenuType } from '@/common/utility/menu.model'
import type { MenuItem } from '@/common/utility/menu.model'
import SidebarMenu from './SidebarMenu.vue'

export default defineComponent({
    name: 'SidebarVendor',
    setup() {
        const isShow = ref(true)
        const menuItems = ref<MenuItem[]>([
            { 
                title: 'Product',
                type: MenuType.SUB,
                path: '/vendor/products',
                icon: 'fa-solid fa-boxes-stacked',
                subMenuItem: [
                    {
                        title: 'My products',
                        path: 'list'
                    },
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

        const toggleSidebar = () => {
            return isShow.value = !isShow.value
        }
        
        /**
         * TODO:
         *  - Add mobile screen size detection here.
         *  - For now, sidebar toggling should be only
         * visible for mobile. 
         */

        return {
            menuItems,
            isShow,
            toggleSidebar
        }
    },
    components: {
        SidebarMenu
    }
})
</script>