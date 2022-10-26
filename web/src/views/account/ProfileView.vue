<template>
    <div class="w-full">
        <div class="p-4 sm:p-6 md:p-8 w-full bg-white
            rounded-lg border border-gray-200 shadow-sm">
            <h5 class="mb-0 text-base font-semibold text-gray-900 md:text-xl">
                Profile
            </h5>
            <p class="text-sm font-normal text-gray-500 dark:text-gray-400 mb-3">
                Manage and protect your account
            </p>

            <div class="grid grid-cols-2">
                <form @submit.prevent>
                    <div class="mb-3">
                        <label class="text-sm text-gray-700">
                            Email
                        </label>
                        <input type="email"
                            class="mt-1 block w-full rounded-lg bg-gray-50
                            border border-gray-300 text-gray-900
                            text-sm p-2.5 focus:outline-none
                            focus:shadow-outline focus:ring-gray-500
                            focus:ring-1" />
                    </div>

                    <div class="mb-3">
                        <label class="text-sm text-gray-700">
                            Name
                        </label>
                        <input type="text"
                            class="mt-1 block w-full rounded-lg bg-gray-50
                            border border-gray-300 text-gray-900
                            text-sm p-2.5 focus:outline-none
                            focus:shadow-outline focus:ring-gray-500
                            focus:ring-1" />
                    </div>

                    <div class="mb-3">
                        <label class="text-sm text-gray-700">
                            Phone no.
                        </label>
                        <input type="text"
                            class="mt-1 block w-full rounded-lg bg-gray-50
                            border border-gray-300 text-gray-900
                            text-sm p-2.5 focus:outline-none
                            focus:shadow-outline focus:ring-gray-500
                            focus:ring-1" />
                    </div>

                    <div class="mb-3">
                        <label class="text-sm text-gray-700">
                            Gender
                        </label>
                        <input type="text"
                            class="mt-1 block w-full rounded-lg bg-gray-50
                            border border-gray-300 text-gray-900
                            text-sm p-2.5 focus:outline-none
                            focus:shadow-outline focus:ring-gray-500
                            focus:ring-1" />
                    </div>

                    <div class="mb-3">
                        <label class="text-sm text-gray-700">
                            Date of birth
                        </label>
                        <input type="date"
                            class="mt-1 block w-full rounded-lg bg-gray-50
                            border border-gray-300 text-gray-900
                            text-sm p-2.5 focus:outline-none
                            focus:shadow-outline focus:ring-gray-500
                            focus:ring-1" />
                    </div>

                    <button class="block rounded-lg border border-transparent 
                        bg-green-300 focus:hover:enabled:bg-green-500
                        px-3 py-2 text-white enabled:bg-green-400
                        focus:outline-none focus:ring-2 focus:ring-green-200
                        font-medium text-sm">
                        Save
                    </button>
                </form>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { onMounted, defineComponent } from 'vue'

export default defineComponent({
    name: 'Profile',
    setup() {
        onMounted(() => {
            // console.log('Mounted Profile')
        })

        return {}
    }
})
</script>