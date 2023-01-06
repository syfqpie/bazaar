<template>
    <section
        class="container mx-auto py-12 
        max-w-7xl px-2 sm:px-6 lg:px-8
        min-h-screen">
        <h5
            class="mb-0 text-base font-semibold 
            text-gray-900 md:text-xl">
            Add products
        </h5>

        <p
            class="text-sm font-normal text-gray-500
            dark:text-gray-400">
            Register new products to your shop
        </p>

        <div class="flex flex-row lg:space-x-6 mt-4">
            <div class="basis-3/12 border-r border-r-gray-200">
                <TheGandalf
                    ref="theWizard"
                    :items="wizardItems"
                    @on-post-step="onStep" />
            </div>

            <div class="basis-9/12 overflow-scroll max-h-[80vh]">
                <div class="mb-3" v-if="theWizard?.config.current === 0">
                    <h6
                        class="mb-2 text-base font-semibold 
                        text-gray-900 md:text-base">
                        Details
                    </h6>
                    <div class="mb-3">
                        <label class="text-sm text-gray-700">
                            Product name
                        </label>
                        <TheInput
                            type="text"
                            placeholder="Enter product name" />
                    </div>

                    <div class="mb-3">
                        <label class="text-sm text-gray-700">
                            Description
                        </label>
                        <TheTextArea
                            rows="6"
                            placeholder="Enter product description" />
                    </div>


                    <div class="inline-flex rounded-md shadow-sm">
                        <TheOutlineButton
                            disabled
                            size="sm"
                            class="rounded-r-none">
                            <i class="fa-solid fa-chevron-up"></i>
                        </TheOutlineButton>

                        <TheOutlineButton
                            size="sm"
                            class="rounded-l-none border-l-0"
                            @click="theWizard?.nextStep()">
                            <i class="fa-solid fa-chevron-down"></i>
                        </TheOutlineButton>
                    </div>
                </div>

                <div class="mb-3" v-else-if="theWizard?.config.current === 1">
                    <h6
                        class="mb-2 text-base font-semibold 
                        text-gray-900 md:text-base">
                        Variant(s)
                    </h6>

                    <AddVariantSection />

                    <div class="inline-flex rounded-md shadow-sm">
                        <TheOutlineButton
                            size="sm"
                            class="rounded-r-none"
                            @click="theWizard?.backStep()">
                            <i class="fa-solid fa-chevron-up"></i>
                        </TheOutlineButton>

                        <TheOutlineButton
                            size="sm"
                            class="rounded-l-none border-l-0"
                            @click="theWizard?.nextStep()">
                            <i class="fa-solid fa-chevron-down"></i>
                        </TheOutlineButton>
                    </div>
                </div>

                <div class="mb-3" v-else-if="theWizard?.config.current === 2">
                    <h6
                        class="mb-2 text-base font-semibold 
                        text-gray-900 md:text-base">
                        Shipping information
                    </h6>

                    <img
                        class="mx-auto opacity-40 h-80 mb-3"
                        src="@/assets/img/icons/work-in-progress.png" />

                    <div class="inline-flex rounded-md shadow-sm">
                        <TheOutlineButton
                            size="sm"
                            class="rounded-r-none"
                            @click="theWizard?.backStep()">
                            <i class="fa-solid fa-chevron-up"></i>
                        </TheOutlineButton>

                        <TheOutlineButton
                            size="sm"
                            class="rounded-l-none border-l-0"
                            @click="onSubmit">
                            Submit
                        </TheOutlineButton>
                    </div>
                </div>

                <div class="mb-3" v-if="false">
                    <TheButton>
                        Add product
                    </TheButton>
                </div>
            </div>
        </div>
    </section>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue'

import TheButton from '@/components/basics/TheButton.vue'
import TheGandalf from '@/components/basics/TheGandalf.vue'
import TheInput from '@/components/basics/TheInput.vue'
import TheTextArea from '@/components/basics/TheTextArea.vue'
import TheOutlineButton from '@/components/basics/TheOutlineButton.vue'
import AddVariantSection from '@/components/products/AddVariantSection.vue'
import type { GandalfConfig, GandalfItem, GandalfStep } from '@/common/utility/wizard.model'

import { useToast } from 'vue-toastification'

export default defineComponent({
    name: 'AddProduct',
    setup() {
        // Wizard
        const theWizard = ref<InstanceType<typeof TheGandalf> | null>(null)
        const wizardItems = ref<GandalfItem[]>([
			{ title: 'Product details', isSkippable: true  },
			{ title: 'Variants' },
			{ title: 'Shipping', isSkippable: true }
		])
        

        onMounted(() => {
            // console.log('Mounted AddProduct')
            console.log('hh', theWizard.value)
        })

        // 
        const toast = useToast()
        
        
        const onStep = (step: GandalfStep,
					    config: GandalfConfig) => { }
        
        const onSubmit = () => {
            toast.success('Added new product!')
        }

		return {
            theWizard,
			wizardItems,
			onStep,
            onSubmit
		}
    },
    components: { 
        AddVariantSection,
        TheButton,
        TheGandalf,
        TheInput,
        TheOutlineButton,
        TheTextArea
    }
})
</script>