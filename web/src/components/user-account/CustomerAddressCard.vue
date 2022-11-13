<template>
    <div
        class="p-4 w-full bg-white rounded-lg border shadow-sm">
        <div class="flex flex-row">
            <div class="flex-1">
                <h1 class="truncate font-semibold text-gray-700">
                    {{ address.name }}
                </h1>
            </div>
            <div
                ref="optionMenu"
                class="flex-none relative">
                <button
                    type="button"
                    class="text-indigo-500 hover:bg-gray-100
                    rounded-lg text-sm px-1 py-0"
                    @click="toggleOption()">
                    <span class="sr-only">Open option</span>
                    <i class="fa-solid fa-bars-progress"></i>
                </button>

                <Transition
                    enter-from-class="transform opacity-0 scale-95"
                    enter-active-class="transition ease-out duration-100"
                    enter-to-class="transform opacity-100 scale-100"
                    leave-from-class="transform opacity-100 scale-100"
                    leave-active-class="transition ease-in duration-75"
                    leave-to-class="transform opacity-0 scale-95">
                    <div
                        v-if="isOptionOpen"
                        class="z-20 absolute w-44 text-base list-none right-0
                        bg-white rounded-lg divide-y divide-gray-100 shadow-lg
                        ring-1 ring-black ring-opacity-5 overflow-hidden">
                        <ul class="py-0">
                            <li>
                                <button
                                    class="block w-full py-2 px-4 text-left
                                    text-sm text-gray-700 hover:bg-gray-100"
                                    @click="makeDefault(1)">
                                    Make default
                                </button>
                            </li>
                            <li>
                                <button
                                    class="block w-full py-2 px-4 text-left
                                    text-sm text-gray-700 hover:bg-gray-100"
                                    @click="toggleEditModal()">
                                    Edit
                                </button>
                            </li>
                            <li>
                                <button
                                    class="block w-full py-2 px-4 text-left
                                    text-sm text-red-700 hover:bg-gray-100"
                                    @click="toggleDeleteConfirmation()">
                                    Delete
                                </button>
                            </li>
                        </ul>
                    </div>
                </Transition>
            </div>
        </div>
        
        <p class="font-semibold text-sm text-gray-700 mb-3">
            {{ address.phoneNo }}
        </p>
        <p class="text-sm font-light text-gray-500 line-clamp-2">
            {{
                `${ address.address }, ${ address.zipcode } ${ address.city }`
            }}
        </p>

        <EditAddressModel
            v-if="isEditAddress"
            :current-address="address"
            @on-cancel="toggleEditModal()" />
        
        <DeleteAddressConfirmation
            v-if="isDeleteAddress"
            :current-address="address"
            @on-cancel="toggleDeleteConfirmation()" />
    </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

import type { CustomerAddress } from '@/common/models/address.model'
import DeleteAddressConfirmation from '@/components/user-account/DeleteAddressConfirmation.vue'
import EditAddressModel from '@/components/user-account/EditAddressModel.vue'

import { onClickOutside } from '@vueuse/core'

/**
 * TODO:
 *      - Add function to make address as default
 */
export default defineComponent({
    name: 'CustomerAddressCard',
    setup() {
        // Component ref
        const optionMenu = ref(null)
        
        // Checker
        const isOptionOpen = ref<Boolean>(false)
        const isEditAddress = ref<Boolean>(false)
        const isDeleteAddress = ref <Boolean>(false)

        // Event
        onClickOutside(optionMenu, (event) => {
            if(isOptionOpen.value){ toggleOption() }
        })

        /**
         * Toggle option menu
         */
        const toggleOption = () => {
            return isOptionOpen.value = !isOptionOpen.value
        }

        /**
         * Make address as default
         */
        const makeDefault = (id: number) => {
            console.log(id)
            toggleOption()
        }

        /**
         * Toggle add address modal
         */
         const toggleEditModal = () => {
            return isEditAddress.value = !isEditAddress.value
        }

        /**
         * Toggle delete address confirmation
         */
        const toggleDeleteConfirmation = () => {
            return isDeleteAddress.value = !isDeleteAddress.value
        }

        return {
            isOptionOpen,
            isEditAddress,
            isDeleteAddress,
            optionMenu,
            toggleOption,
            makeDefault,
            toggleEditModal,
            toggleDeleteConfirmation
        }
    },
    components: {
        DeleteAddressConfirmation,
        EditAddressModel
    },
    props: {
        address: {
            type: Object as () => CustomerAddress,
            required: true
        }
    }
})
</script>