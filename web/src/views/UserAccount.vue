<template>
    <section
        class="container mx-auto py-12 
        max-w-7xl px-2 sm:px-6 lg:px-8">
        <div class="flex flex-row lg:space-x-6">
            <div class="basis-80">
                <TheMenu :menu-items="menuItems" />
            </div>
            
            <div class="basis-full">
                <RouterView />
            </div>
        </div>
    </section>
</template>

<script lang="ts">
import { onMounted, defineComponent, ref } from 'vue'

import TheMenu from '@/components/basics/menu/TheMenu.vue'
import { MenuType, type MenuItem } from '@/common/utility/menu.model'

export default defineComponent({
    name: 'UserAccount',
    setup() {
        // Data
        const menuItems = ref<MenuItem[]>([
            {
                title: 'Account',
                type: MenuType.SUB,
                path: '/user/account',
                icon: 'fa-solid fa-user',
                subMenuItem: [
                    {
                        title: 'Profile',
                        path: 'profile'
                    },
                    {
                        title: 'Address',
                        path: 'address'
                    },
                    {
                        title: 'Change password',
                        path: 'change-password'
                    }
                ]
            },
            {
                title: 'System',
                type: MenuType.MENU,
                path: '/user/system',
                icon: 'fa-solid fa-robot'
            }
        ])
        
        onMounted(() => {
            // console.log('Mounted UserAccount')
        })

        return {
            menuItems
        }
    },
    components: { TheMenu }
})
</script>
