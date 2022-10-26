<template>
    <div class="">
        <section class="container mx-auto py-12 
            max-w-7xl px-2 sm:px-6 lg:px-8">
            <div class="flex flex-row lg:space-x-6">
                <div class="basis-80">
                    <aside class="w-full" aria-label="Sidebar">
                        <div class="overflow-y-auto py-4 px-3 bg-transparent rounded">
                            <ul class="space-y-2">
                                <li>
                                    <button type="button" 
                                        class="flex items-center p-2 w-full text-sm font-medium
                                        text-gray-500 rounded-lg transition duration-100
                                        hover:bg-gray-100 hover:text-gray-800" 
                                        :attr.aria-controls="isAccountMenuActive" 
                                        data-collapse-toggle="my-dropdown"
                                        @click="isAccountMenuActive = !isAccountMenuActive"
                                        :class="{
                                            'text-gray-800': $route.path.startsWith(ACCOUNT_PATH)
                                        }">
                                        <i class="fa-solid fa-user"></i>

                                        <span sidebar-toggle-item=""
                                            class="flex-1 ml-3 text-left whitespace-nowrap">
                                            Account
                                        </span>

                                        <i class="fa-solid transition duration-1000"
                                            :class="{
                                                'fa-chevron-right': !isAccountMenuActive || !$route.path.startsWith(ACCOUNT_PATH),
                                                'fa-chevron-down': isAccountMenuActive || $route.path.startsWith(ACCOUNT_PATH)
                                            }"></i>
                                    </button>

                                    <ul id="my-dropdown"
                                        ref="accountMenu"
                                        class="py-2 space-y-2"
                                        :class="{ 'hidden': 
                                            !isAccountMenuActive && $route.path.startsWith(ACCOUNT_PATH) }">
                                        <li>
                                            <router-link id="profileLink"
                                                to="/user/account/profile"
                                                class="flex items-center p-2 pl-11 w-full text-sm
                                                font-medium text-gray-500 rounded-lg transition
                                                duration-100 group hover:bg-gray-100 hover:text-gray-800"
                                                active-class="text-green-400 hover:text-green-400">
                                                Profile
                                            </router-link>
                                        </li>
                                        <li>
                                            <router-link to="/user/account/address"
                                                class="flex items-center p-2 pl-11 w-full text-sm
                                                font-medium text-gray-500 rounded-lg transition
                                                duration-100 group hover:bg-gray-100 hover:text-gray-800"
                                                active-class="text-green-400 hover:text-green-400">
                                                Address
                                            </router-link>
                                        </li>
                                        <li>
                                            <router-link to="/user/account/change-password"
                                                class="flex items-center p-2 pl-11 w-full text-sm
                                                font-medium text-gray-500 rounded-lg transition
                                                duration-100 group hover:bg-gray-100 hover:text-gray-800"
                                                active-class="text-green-400 hover:text-green-400">
                                                Change password
                                            </router-link>
                                        </li>
                                    </ul>
                                </li>
                                <li>
                                    <a href="#" class="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg hover:bg-gray-100">
                                        <i class="fa-solid fa-life-ring text-gray-500 
                                            transition duration-75">
                                        </i>
                                    
                                        <span class="ml-3">Help</span>
                                    </a>
                                </li>
                            </ul>
                        </div>
                    </aside>
                </div>
                
                <div class="basis-full">
                    <RouterView />
                </div>
            </div>
        </section>
    </div>
</template>

<script lang="ts">
import { onMounted, defineComponent, ref } from 'vue'
import { useRoute } from 'vue-router'

const ACCOUNT_PATH = '/user/account'

export default defineComponent({
    name: 'Account',
    setup() {

        // Menu
        const isAccountMenuActive = ref(false)
        const route = useRoute()


        onMounted(() => {
            console.log('Mounted Account')
            isAccountMenuActive.value = route.path.startsWith(ACCOUNT_PATH)
        })


        return { 
            isAccountMenuActive,
            ACCOUNT_PATH
        }
    }
})
</script>