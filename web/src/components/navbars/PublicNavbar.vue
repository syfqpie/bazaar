<template>
    <nav class="bg-white border-b">
        <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
            <div class="relative flex h-16 items-center justify-between">
                <div class="absolute inset-y-0 left-0 flex items-center sm:hidden">
                    <!-- Mobile menu button-->
                    <button type="button"
                        class="inline-flex items-center justify-center
                            rounded-md p-2 text-gray-400 hover:bg-gray-700
                            hover:text-white focus:outline-none focus:ring-2
                            focus:ring-inset focus:ring-white"
                        aria-controls="mobile-menu" 
                        aria-expanded="false">
                        <span class="sr-only">Open main menu</span>
                        <!--
                            Icon when menu is closed.

                            Heroicon name: outline/bars-3

                            Menu open: "hidden", Menu closed: "block"
                        -->
                        <svg class="block h-6 w-6" 
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none" viewBox="0 0 24 24"
                            stroke-width="1.5"
                            stroke="currentColor"
                            aria-hidden="true">
                            <path stroke-linecap="round"
                                stroke-linejoin="round"
                                d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
                        </svg>
                        <!--
                            Icon when menu is open.

                            Heroicon name: outline/x-mark

                            Menu open: "block", Menu closed: "hidden"
                        -->
                        <svg class="hidden h-6 w-6"
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none" viewBox="0 0 24 24"
                            stroke-width="1.5"
                            stroke="currentColor"
                            aria-hidden="true">
                            <path stroke-linecap="round"
                                stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>
                </div>

                <div class="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start">
                    <div class="flex flex-shrink-0 items-center">
                        <img class="block h-8 w-auto lg:hidden"
                            src="@/assets/img/default/trolley.png"
                            alt="Bazaar">
                        <img class="hidden h-8 w-auto lg:block"
                            src="@/assets/img/default/trolley.png"
                            alt="Bazaar">
                    </div>

                    <div class="hidden sm:ml-6 sm:block">
                        <div class="flex space-x-4">
                            <router-link to="/home"
                                class="bg-transparent px-3 py-2 text-sm
                                font-medium text-gray-300 hover:text-green-400"
                                active-class="text-green-400">
                                Home
                            </router-link>

                            <router-link to="/"
                                class="bg-transparent px-3 py-2 text-sm
                                font-medium text-gray-300 hover:text-green-400"
                                active-class="text-green-400">
                                Explore
                            </router-link>

                            <router-link to="/"
                                class="bg-transparent px-3 py-2 text-sm
                                font-medium text-gray-300 hover:text-green-400"
                                active-class="text-green-400">
                                FAQ
                            </router-link>
                        </div>
                    </div>
                </div>

                <div class="absolute inset-y-0 right-0 flex items-center pr-2
                    sm:static sm:inset-auto sm:ml-6 sm:pr-0">    
                    <button class="bg-transparent px-3 py-2 text-sm
                        font-medium text-gray-300 hover:text-gray-400">
                        <i class="fa-solid fa-bag-shopping fa-xl mr-2"></i>
                    </button>
                    <!-- Profile dropdown -->
                    <div v-if="!authStore.isAuthenticated"
                        class="hidden sm:block">
                        <router-link to="/auth/login"
                            v-slot="{href, navigate}">
                            <button :href="href"
                                @click="navigate"
                                class="text-white bg-green-400 px-3 py-2 
                                rounded-md text-sm font-medium border
                                border-transparent hover:bg-green-500
                                focus:outline-none focus:ring-2 
                                focus:ring-green-200 mr-2">
                                Join as vendor
                            </button>
                        </router-link>

                        <router-link to="/auth/login"
                            v-slot="{href, navigate}">
                            <button :href="href"
                                @click="navigate"
                                class="bg-transparent px-3 py-2 text-sm
                                font-medium text-gray-300 hover:text-gray-400">
                                <i class="fa-solid fa-circle-user fa-xl"></i>
                            </button>
                        </router-link>
                    </div>
                    
                    <div class="relative ml-3" v-else-if="authStore.isAuthenticated">
                        <div>
                            <button type="button"
                                class="flex rounded-full bg-transparent text-sm
                                    focus:outline-none font-medium text-gray-300
                                    hover:text-gray-400"
                                id="user-menu-button"
                                aria-expanded="false"
                                aria-haspopup="true"
                                @click="isMenuOpen = !isMenuOpen">
                                <i class="fa-solid fa-circle-user fa-xl"></i>
                            </button>
                        </div>

                        <!--
                            Dropdown menu, show/hide based on menu state.

                            Entering: "transition ease-out duration-100"
                            From: "transform opacity-0 scale-95"
                            To: "transform opacity-100 scale-100"
                            Leaving: "transition ease-in duration-75"
                            From: "transform opacity-100 scale-100"
                            To: "transform opacity-0 scale-95"
                        -->
                        <div class="absolute right-0 z-10 mt-2 w-48 origin-top-right
                            rounded-md bg-white py-1 shadow ring-1 ring-black
                            ring-opacity-5 focus:outline-none"
                            v-if="isMenuOpen"
                            role="menu"
                            aria-orientation="vertical"
                            aria-labelledby="user-menu-button"
                            tabindex="-1">
                            <!-- Active: "bg-gray-100", Not Active: "" -->
                            <router-link to="/"
                                class="block px-4 py-2 text-sm text-gray-700"
                                active-class="bg-gray-100">
                                Your profile
                            </router-link>
                            <a href="#" class="block px-4 py-2 text-sm text-gray-700"
                                role="menuitem"
                                tabindex="-1"
                                id="user-menu-item-1">
                                Settings
                            </a>
                            <a href="#" class="block px-4 py-2 text-sm text-gray-700"
                                role="menuitem"
                                tabindex="-1"
                                id="user-menu-item-2">
                                Sign out
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Mobile menu, show/hide based on menu state. -->
        <div class="sm:hidden" id="mobile-menu">
            <div class="space-y-1 px-2 pt-2 pb-3">
                <!-- Current: "bg-gray-900 text-white", Default: "text-gray-300 hover:bg-gray-700 hover:text-white" -->
                <a href="#" class="bg-green-400 text-white block px-3
                    py-2 rounded-md text-base font-medium"
                    aria-current="page">
                    Home
                </a>

                <a href="#"
                    class="text-gray-300 hover:bg-gray-700 hover:text-white
                        block px-3 py-2 rounded-md text-base font-medium">
                    Explore
                </a>

                <a href="#"
                    class="text-gray-300 hover:bg-gray-700 hover:text-white
                    block px-3 py-2 rounded-md text-base font-medium">
                    FAQ
                </a>
            </div>
        </div>
    </nav>
</template>

<script lang="ts">
import { useAuthStore } from '@/stores'
import { onMounted, defineComponent, ref } from 'vue'

export default defineComponent({
    name: 'PublicNavbar',
    setup() {
        // Services
        const authStore = useAuthStore()

        // Checkers
        const isMenuOpen = ref<boolean>(false)
        const isLoading = ref<boolean>(false)
        
        onMounted(() => {
            // console.log('Mounted PublicNavbar')
            verifyToken()
        })

        const verifyToken = () => {
            return authStore.verifyToken()
                .then(data => {
                    isLoading.value = false
                })
                .catch(err => {
                    isLoading.value = false
                })
        }

        return {
            isMenuOpen,
            authStore 
        }
    }
})
</script>