<template>
    <div class="w-full">
        <div
            class="p-4 sm:p-6 md:p-8 w-full bg-white
            rounded-lg border border-gray-200 shadow-sm">
            <h5 class="mb-0 text-base font-semibold text-gray-900 md:text-xl">
                Profile
            </h5>
            <p class="text-sm font-normal text-gray-500 dark:text-gray-400 mb-3">
                Manage and protect your account
            </p>

            <div class="grid grid-cols-2">
                <div>
                    <div class="mb-3">
                        <label class="text-sm text-gray-700">
                            Email
                        </label>
                        <input
                            type="email"
                            class="mt-1 block w-full rounded-lg disabled:bg-gray-50
                            border disabled:border-gray-200 disabled:text-gray-400
                            disabled:cursor-not-allowed text-sm p-2.5"
                            :value="authStore.email"
                            disabled />
                    </div>

                    <div class="mb-3">
                        <label class="text-sm text-gray-700">
                            Role
                        </label>
                        
                        <h5 class="mt-1 flex items-center text-sm font-extrabold">
                            <span 
                                class="text-medium font-semibold px-2.5 py-0.5 rounded"
                                :class="{
                                    'bg-gray-200 text-gray-900': authStore.userType === UserType.Admin,
                                    'bg-pink-100 text-pink-800': authStore.userType === UserType.Vendor,
                                    'bg-indigo-100 text-indigo-800': authStore.userType === UserType.Customer
                                }">
                                {{ authStore.getUserTypeNormal }}
                            </span>
                        </h5>
                    </div>

                    <div v-if="authStore.userType !== UserType.Admin">
                        <hr class="mt-4 mb-3 h-px bg-gray-200 border-0" />
                        <ProfileVendor v-if="authStore.userType === UserType.Vendor" />

                        <ProfileCustomer v-else-if="authStore.userType === UserType.Customer" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent, onMounted } from 'vue'

import { UserType } from '@/common/models/user.model'
import ProfileVendor from '@/components/user-account/ProfileVendor.vue'
import ProfileCustomer from '@/components/user-account/ProfileCustomer.vue'
import { useAuthStore, useVendorStore } from '@/stores'

export default defineComponent({
    name: 'AccountProfile',
    setup() {
        // Services
        const authStore = useAuthStore()
        const vendorStore = useVendorStore()

        onMounted(() => {
            // console.log('Mounted AccountProfile')
        })

        return {
            authStore,
            vendorStore,
            UserType
        }
    },
    components: {
        ProfileVendor,
        ProfileCustomer
    }
})
</script>