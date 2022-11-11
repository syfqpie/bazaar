<template>
    <aside
        class="w-full"
        aria-label="Menu">
        <div class="overflow-y-auto py-4 px-3 bg-transparent rounded">
            <ul class="space-y-2">
                <li v-for="item of menuItems"
                    :key="item.path">
                    <TheMenuItem
                        v-if="item.type === MenuType.MENU"
                        :menu-item="item" />

                    <TheSubMenuItem
                        v-else-if="item.type === MenuType.SUB"
                        :sub-menu-item="item" />
                </li>
            </ul>
        </div>
    </aside>
</template>

<script lang="ts">
import { defineComponent, onMounted } from 'vue'

import { MenuType, type MenuItem } from '@/common/models/utility.model'
import TheMenuItem from './TheMenuItem.vue'
import TheSubMenuItem from './TheSubMenuItem.vue'

export default defineComponent({
    name: 'TheMenu',
    setup(prop) {
        onMounted(() => {
            // console.log('Mounted TheMenu')
        })

        return {
            MenuType
        }
    },
    components: { 
        TheMenuItem,
        TheSubMenuItem
    },
    props: {
        menuItems: {
            type: Array as () => MenuItem[],
            required: true
        }
    }
})
</script>