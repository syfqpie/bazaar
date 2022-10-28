<template>
    <nav class="bg-white border-b">
        <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
            <div class="relative flex h-16 items-center justify-between">
                <div class="absolute inset-y-0 left-0 flex items-center sm:hidden">
                    <!-- Mobile menu button-->
                    <button
                        type="button"
                        class="inline-flex items-center justify-center
                        rounded-lg p-2 text-gray-400 hover:bg-gray-700
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
                        <svg
                            class="block h-6 w-6" 
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
                        <svg
                            class="hidden h-6 w-6"
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
                        <img
                            class="block h-8 w-auto lg:hidden"
                            src="@/assets/img/default/trolley.png"
                            alt="Bazaar" />
                        <img
                            class="hidden h-8 w-auto lg:block"
                            src="@/assets/img/default/trolley.png"
                            alt="Bazaar" />
                    </div>

                    <div class="hidden sm:ml-6 sm:block">
                        <div class="flex space-x-4">
                            <router-link
                                to="/home"
                                class="bg-transparent px-3 py-2 text-sm
                                font-medium text-gray-300 hover:text-green-500"
                                active-class="!text-green-400">
                                Home
                            </router-link>

                            <router-link
                                to="/explore"
                                class="bg-transparent px-3 py-2 text-sm
                                font-medium text-gray-300 hover:text-green-400"
                                active-class="!text-green-400">
                                Explore
                            </router-link>

                            <router-link
                                to="/faq"
                                class="bg-transparent px-3 py-2 text-sm
                                font-medium text-gray-300 hover:text-green-400"
                                active-class="!text-green-400">
                                FAQ
                            </router-link>
                        </div>
                    </div>
                </div>

                <div
                    class="absolute inset-y-0 right-0 flex items-center pr-2
                    sm:static sm:inset-auto sm:ml-6 sm:pr-0">    
                    <button
                        class="bg-transparent px-3 py-2 text-sm
                        font-medium text-gray-300 hover:text-gray-400"
                        @click="cartStore.toggleOpen()">
                        <i class="fa-solid fa-bag-shopping fa-xl mr-2"></i>
                    </button>
                    <!-- Profile dropdown -->
                    <div
                        v-if="!authStore.isAuthenticated"
                        class="hidden sm:block">
                        <router-link
                            to="/auth/login"
                            v-slot="{href, navigate}">
                            <button
                                :href="href"
                                @click="navigate"
                                class="text-white bg-green-400 px-3 py-2 
                                rounded-lg text-sm font-medium border
                                border-transparent hover:bg-green-500
                                focus:outline-none focus:ring-2 
                                focus:ring-green-200 mr-2">
                                Join as vendor
                            </button>
                        </router-link>

                        <router-link
                            to="/auth/login"
                            v-slot="{href, navigate}">
                            <button
                                :href="href"
                                @click="navigate"
                                class="bg-transparent px-3 py-2 text-sm
                                font-medium text-gray-300 hover:text-gray-400">
                                <i class="fa-solid fa-circle-user fa-xl"></i>
                            </button>
                        </router-link>
                    </div>
                    
                    <div 
                        v-else-if="authStore.isAuthenticated"
                        ref="menuBar"
                        class="relative ml-3">
                        <div>
                            <button 
                                ype="button"
                                class="flex rounded-full bg-transparent text-sm
                                focus:outline-none font-medium text-gray-300
                                hover:text-gray-400"
                                id="user-menu-button"
                                aria-expanded="false"
                                aria-haspopup="true"
                                @click="toggleMenu()">
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

                        <div
                            v-if="isMenuOpen" 
                            role="menu"
                            tabindex="-1"
                            aria-orientation="vertical"
                            aria-labelledby="user-menu-button"
                            class="absolute right-0 z-10 mt-2 w-48 origin-top-right
                            rounded-lg bg-white shadow-lg ring-1 ring-black
                            ring-opacity-5 focus:outline-none text-sm overflow-hidden">
                            <div class="py-2 px-4 font-medium text-center"
                                :class="userBgColor">
                                <p class="mt-2 my-1"
                                    :class="userTextColor">
                                    <i class="fa-solid fa-user-secret fa-2xl"></i>
                                </p>
                                <p class="text-sm"
                                    :class="userTextColor">
                                    {{ authStore.getUserTypeNormal }}
                                </p>
                            </div>

                            <div class="py-3 px-4 text-gray-900">
                                <div class="truncate"
                                    :title="authStore.email">
                                    {{ authStore.email }}
                                </div>
                            </div>

                            <router-link
                                to="/user/account/profile"
                                class="block py-2 px-4 hover:bg-gray-100"
                                active-class="bg-gray-100"
                                @click="toggleMenu()">
                                Your profile
                            </router-link>

                            <a
                                href="#"
                                class="block py-2 px-4 hover:bg-gray-100">
                                Settings
                            </a>
                            <a 
                                class="block py-2 px-4 hover:bg-gray-100 cursor-pointer"
                                @click="authStore.logout()">
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
                <a
                    href="#"
                    class="bg-green-400 text-white block px-3
                    py-2 rounded-lg text-base font-medium"
                    aria-current="page">
                    Home
                </a>

                <a
                    href="#"
                    class="text-gray-300 hover:bg-gray-700 hover:text-white
                    block px-3 py-2 rounded-lg text-base font-medium">
                    Explore
                </a>

                <a
                    href="#"
                    class="text-gray-300 hover:bg-gray-700 hover:text-white
                    block px-3 py-2 rounded-lg text-base font-medium">
                    FAQ
                </a>
            </div>
        </div>
    </nav>
</template>

<script lang="ts">
import { computed, defineComponent, onMounted, ref } from 'vue'

import { onClickOutside } from '@vueuse/core'

import { useAuthStore, useCartStore } from '@/stores'
import { UserType } from '@/common/models/user.model'

export default defineComponent({
    name: 'NavbarPublic',
    setup() {
        // Component ref
        const menuBar = ref(null)

        // Services
        const authStore = useAuthStore()
        const cartStore = useCartStore()

        // Checkers
        const isMenuOpen = ref<boolean>(false)
        const isLoading = ref<boolean>(false)
        
        onMounted(() => {
            // console.log('Mounted NavbarPublic')
            if (!authStore.isAuthenticated && authStore.accessToken) {
                verifyToken()
            }
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

        // Event
        onClickOutside(menuBar, (event) => {
            if(isMenuOpen.value){ toggleMenu() }
        })

        // const logout = async () => {
        //     return authStore.logout()
        // }

        const toggleMenu = () => {
            isMenuOpen.value = !isMenuOpen.value
        }

        // Class
        const userTextColor = computed(() => ({
            'text-gray-800': authStore.userType === UserType.Admin,
            'text-pink-800': authStore.userType === UserType.Vendor,
            'text-indigo-800': authStore.userType === UserType.Customer
        }))
        const userBgColor = computed(() => ({
            'bg-gray-100': authStore.userType === UserType.Admin,
            'bg-pink-100': authStore.userType === UserType.Vendor,
            'bg-indigo-100': authStore.userType === UserType.Customer
        }))

        return {
            isMenuOpen,
            authStore,
            cartStore,
            menuBar,
            UserType,
            toggleMenu,
            userTextColor,
            userBgColor
        }
    }
})
</script>