<template>
    <button
        type="button" 
        class="flex items-center px-3 py-2 w-full text-sm font-medium
        rounded-lg transition duration-100 hover:text-indigo-500" 
        :class="{
            'text-indigo-500 bg-gray-200 focus:outline \
            focus:outline-2 focus:outline-indigo-100': 
                $route.path.startsWith(subMenuItem.path),
            'text-gray-500 bg-gray-100 hover:bg-gray-100': 
                !$route.path.startsWith(subMenuItem.path)
        }"
        @click="isActive = !isActive">
        <i 
            class="fa-fw"
            :class="subMenuItem.icon">
        </i>

        <span class="flex-1 ml-2 text-left whitespace-nowrap">
            {{ subMenuItem.title }}
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
        enter-to-class="h-[8rem]"
        leave-from-class="h-[8rem]"
        leave-active-class="transition-all duration-300 overflow-hidden ease-out py-0"
        leave-to-class="h-0">
        <ul
            v-if="isActive"
            class="py-2 space-y-2 pl-2">
            <li v-for="sub of subMenuItem.subMenuItem!"
                :key="`${subMenuItem.path}/${sub.path}`">
                <router-link
                    :to="`${subMenuItem.path}/${sub.path}`"
                    class="flex items-center px-3 py-2 pl-[1.85rem] w-full text-sm
                    font-medium text-gray-500 max-h-full rounded-lg
                    transition-all duration-100 group hover:text-indigo-500"
                    active-class="!text-indigo-500 !bg-gray-200
                    focus:outline focus:outline-2 focus:outline-indigo-100">
                    {{ sub.title }}
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
    name: 'TheSubMenuItem',
    setup(prop) {
        // Data
        const isActive = ref(false)

        // Services
        const route = useRoute()

        onMounted(() => {
            // console.log('Mounted TheSubMenuItem')
            isActive.value = route.path.startsWith(prop.subMenuItem.path)
        })

        return { 
            isActive
        }
    },
    props: {
        subMenuItem: {
            type: Object as () => MenuItem,
            required: true
        }
    }
})
</script>