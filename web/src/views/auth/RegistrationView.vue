<template>
    <div class="w-full py-8 px-12">
        <div>
            <img alt="Bazaar"
                class="mx-auto h-12 w-auto"
                src="@/assets/img/default/trolley.png" />

            <h2 class="mt-6 text-center text-3xl
                font-bold tracking-tight text-gray-900">
                Create your account
            </h2>
        </div>

        <form>
            <div class="mt-8 max-w-md">
                <div class="grid grid-cols-1 gap-3">
                    <div>
                        <label class="text-gray-700">Email</label>
                        <input type="email"
                            class="mt-1 block w-full rounded-md bg-gray-100
                            border-transparent px-3 py-2 focus:outline-none
                            focus:shadow-outline focus:ring-gray-500
                            focus:ring-1 focus:bg-white"
                            placeholder="Enter your email" />
                    </div>

                    <div>
                        <label class="text-gray-700">First name</label>
                        <input type="text"
                            class="mt-1 block w-full rounded-md bg-gray-100
                            border-transparent px-3 py-2 focus:outline-none
                            focus:shadow-outline focus:ring-gray-500
                            focus:ring-1 focus:bg-white"
                            placeholder="Enter your first name" />
                    </div>

                    <div>
                        <label class="text-gray-700">Last name</label>
                        <input type="text"
                            class="mt-1 block w-full rounded-md bg-gray-100
                            border-transparent px-3 py-2 focus:outline-none
                            focus:shadow-outline focus:ring-gray-500
                            focus:ring-1 focus:bg-white"
                            placeholder="Enter your last name" />
                    </div>

                    <div class="mt-1 flex items-center justify-between">
                        <div class="flex items-center">
                            
                        </div>

                        <div class="text-sm">
                            <a href="#" 
                                class="font-medium text-green-400
                                hover:text-green-300">
                                Forgot your password?
                            </a>
                        </div>
                    </div>

                    <div>
                        <button type="submit"
                            class="mt-1 group relative flex w-full justify-center
                            rounded-md border border-transparent bg-green-300
                            px-3 py-2 text-white hover:bg-green-400
                            focus:outline-none focus:ring-2 focus:ring-green-200">
                            Sign up
                        </button>
                    </div>

                    <div class="mt-2 mb-1 justify-self-center text-sm">
                        <p>or</p>
                    </div>

                    <div class="flex flex-col">
                        <div class="text-sm text-center">
                            <p class="text-gray-500">
                                Forgot your password?
                                <router-link :to="{ name: 'reset' }"
                                    class="font-medium 
                                    text-green-400 hover:text-green-300">
                                    Reset
                                </router-link>
                            </p>
                        </div>
                        
                        <div class="text-sm text-center">
                            <p class="text-gray-500">
                                Already have an account?
                                <router-link :to="{ name: 'login' }"
                                    class="font-medium 
                                    text-green-400 hover:text-green-300">
                                    Sign in
                                </router-link>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </form>
    </div>
</template>

<script lang="ts">
import { onMounted, defineComponent } from 'vue'

export default defineComponent({
  name: 'Registration',
  setup() {
    onMounted(() => {
      // console.log('Mounted Registration')
    })

    return {}
  }
})
</script>
