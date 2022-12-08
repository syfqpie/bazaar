<template>
    <button
        type="button" 
        class="flex items-center py-2 px-3 text-base
        font-normal rounded-lg w-full text-gray-900 
        hover:bg-gray-100 dark:hover:bg-gray-700
        transition duration-100 ease-out" 
        :class="{
            'dark:text-indigo-500 dark:bg-gray-700': 
                $route.path.startsWith(subItem.path),
            'dark:text-white': 
                !$route.path.startsWith(subItem.path)
        }"
        @click="isActive = !isActive">
        <i 
            class="fa-fw"
            :class="subItem.icon">
        </i>

        <span class="flex-1 ml-2 text-left whitespace-nowrap">
            {{ subItem.title }}
        </span>

        <i 
            class="fa-solid fa-chevron-right
            fa-fw transition-all duration-300"
            :class="{
                'rotate-0': !isActive,
                'rotate-90': isActive
            }"></i>
    </button>

    <Transition
        enter-from-class="h-0 py-0"
        enter-active-class="transition-all duration-300 overflow-hidden ease-in"
        enter-to-class="h-[2.5rem]"
        leave-from-class="h-[2.5rem]"
        leave-active-class="transition-all duration-300 overflow-hidden ease-out py-0"
        leave-to-class="h-0">
        <ul
            v-if="isActive"
            class="space-y-2 mt-2 mb-0 pl-7">
            <li v-for="sub of subItem.subMenuItem!"
                :key="`${subItem.path}/${sub.path}`"
                class="">
                <router-link
                    :to="`${subItem.path}/${sub.path}`"
                    class="flex items-center py-2 px-3 text-base
                    font-normal text-gray-900 rounded-lg w-full
                    dark:text-white hover:bg-gray-100 [&:last-child]:mb-0
                    dark:hover:bg-gray-700 transition duration-100 ease-out"
                    active-class="dark:text-indigo-500 dark:bg-gray-700">
                    <i class="fa-solid fa-minus fa-2xs"></i>
                    
                    <span class="flex-1 ml-2 text-left whitespace-nowrap">
                        {{ sub.title }}
                    </span>
                </router-link>
            </li>
        </ul>
    </Transition>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import type { MenuItem } from '@/common/utility/menu.model'

export default defineComponent({
    name: 'SidebarSubItem',
    setup(prop) {
        // Data
        const isActive = ref(false)

        // Services
        const route = useRoute()

        onMounted(() => {
            // console.log('Mounted SidebarSubItem')
            isActive.value = route.path.startsWith(prop.subItem.path)
        })

        return { 
            isActive
        }
    },
    props: {
        subItem: {
            type: Object as () => MenuItem,
            required: true
        }
    }
})
</script>