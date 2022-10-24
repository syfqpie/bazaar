<template>
    <div class="w-full py-8 px-12">
        <div>
            <img alt="Bazaar"
                class="mx-auto h-12 w-auto"
                src="@/assets/img/default/trolley.png" />

            <h2 class="mt-6 text-center text-3xl
                font-bold tracking-tight text-gray-900">
                Reset your password with Bazaar
            </h2>
        </div>

        <form>
            <div class="mt-8 max-w-md">
                <div class="grid grid-cols-1 gap-3">
                    <div>
                        <label class="text-gray-700">New password</label>
                        <input type="password"
                            class="mt-1 block w-full rounded-md bg-gray-100
                            border-transparent px-3 py-2 focus:outline-none
                            focus:shadow-outline focus:ring-gray-500
                            focus:ring-1 focus:bg-white"
                            placeholder="Enter your new password" />
                    </div>

                    <div>
                        <label class="text-gray-700">Confirm new password</label>
                        <input type="email"
                            class="mt-1 block w-full rounded-md bg-gray-100
                            border-transparent px-3 py-2 focus:outline-none
                            focus:shadow-outline focus:ring-gray-500
                            focus:ring-1 focus:bg-white"
                            placeholder="Enter your confirm new password" />
                    </div>

                    <div>
                        <button type="submit"
                            class="mt-1 group relative flex w-full justify-center
                            rounded-md border border-transparent bg-green-300
                            px-3 py-2 text-white hover:bg-green-400
                            focus:outline-none focus:ring-2 focus:ring-green-200">
                            Reset password
                        </button>
                    </div>
                </div>
            </div>
        </form>
    </div>
</template>

<script lang="ts">
import { onMounted, defineComponent } from 'vue'

export default defineComponent({
  name: 'ConfirmReset',
  setup() {
    onMounted(() => {
      // console.log('Mounted ConfirmReset')
    })

    return {}
  }
})
</script>
