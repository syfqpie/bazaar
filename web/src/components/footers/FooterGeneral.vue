<template>
    <footer
        class="bg-neutral-100 rounded-lg shadow
        px-4 py-4 md:py-8 lg:px-32 sticky top-[100vh]">
        <div class="flex flex-col sm:flex-row items-center sm:justify-between">
            <a
                href="https://github.com/syfqpie/bazaar"
                class="flex items-center mb-4 sm:mb-0">
                <img
                    src="@/assets/img/default/trolley.png"
                    class="mr-3 h-8" alt="Bazaar Logo" />
                <span class="self-center text-2xl font-semibold whitespace-nowrap">
                    Bazaar
                </span>
            </a>

            <ul class="flex flex-wrap items-center mb-2 text-sm text-gray-500 sm:mb-0">
                <li>
                    <a
                        href="https://github.com/syfqpie/bazaar"
                        class="mr-4 hover:underline md:mr-6">
                        Github
                    </a>
                </li>
                <li>
                    <a
                        href="https://github.com/syfqpie/bazaar"
                        class="mr-4 hover:underline md:mr-6">
                        Privacy Policy
                    </a>
                </li>
                <li>
                    <a
                        href="https://github.com/syfqpie/bazaar"
                        class="hover:underline">
                        Contact
                    </a>
                </li>
            </ul>
        </div>

        <hr class="my-4 border-gray-200 sm:mx-auto lg:my-8" />
        <span class="block text-sm text-gray-500 text-center">
            © 2022 
            <a
                href="https://github.com/syfqpie/bazaar"
                class="hover:underline">
                Bazaar.
            </a>
            All rights reserved.
        </span>
    </footer>
</template>

<script lang="ts">
import { onMounted, defineComponent } from 'vue'

export default defineComponent({
    name: 'FooterGeneral',
    setup() {
        onMounted(() => {
            // console.log('Mounted FooterGeneral')
        })

        return {}
    }
})
</script>