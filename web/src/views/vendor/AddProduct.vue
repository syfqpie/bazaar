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

        <div class="flex flex-row mt-4">
            <div class="basis-3/12 border-r border-r-gray-200">
                <TheGandalf
                    ref="theWizard"
                    :items="wizardItems"
                    @on-post-step="onStep" />
            </div>

            <div class="basis-9/12 overflow-scroll max-h-[80vh] lg:pl-6">
                <form @submit.prevent>
                    <div class="mb-3" v-if="theWizard?.config.current === 0">
                        <h6
                            class="mb-2 text-base font-semibold 
                            text-gray-900 md:text-base">
                            Details
                        </h6>
                        
                        <div class="mb-3">
                            <label class="text-sm text-gray-700">
                                Name
                            </label>
                            <TheInput
                                type="text"
                                placeholder="Enter product name"
                                v-model="productForm.name"
                                :class="{
                                    'border-red-400': v$.name.$dirty &&
                                                        v$.name.$invalid 
                                }"
                                :disabled="isWizardCompleted"
                                @blur="v$.name.$touch" />
                            <p
                                v-for="error of v$.name.$errors"
                                :key="error.$uid"
                                class="mt-2 text-xs text-red-600 dark:text-red-500">
                                {{ error.$message }}
                            </p>
                        </div>

                        <div class="mb-3">
                            <label class="text-sm text-gray-700">
                                Description
                            </label>
                            <TheTextArea
                                rows="6"
                                placeholder="Enter product description"
                                v-model="productForm.description"
                                :class="{
                                    'border-red-400': v$.description.$dirty &&
                                                        v$.description.$invalid 
                                }"
                                :disabled="isWizardCompleted"
                                @blur="v$.description.$touch" />
                            <p
                                v-for="error of v$.description.$errors"
                                :key="error.$uid"
                                class="mt-2 text-xs text-red-600 dark:text-red-500">
                                {{ error.$message }}
                            </p>
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

                        <AddVariantSection
                            :is-wizard-completed="isWizardCompleted"
                            :form-variants="productForm.variants"
                            @on-update="onVariantsUpdate" />

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
                                :disabled="isWizardCompleted"
                                @click="onSubmit">
                                Submit
                            </TheOutlineButton>
                        </div>
                    </div>
                </form>

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
import { computed, defineComponent, onMounted, ref, watch } from 'vue'

import TheButton from '@/components/basics/TheButton.vue'
import TheGandalf from '@/components/basics/TheGandalf.vue'
import TheInput from '@/components/basics/TheInput.vue'
import TheTextArea from '@/components/basics/TheTextArea.vue'
import TheOutlineButton from '@/components/basics/TheOutlineButton.vue'
import AddVariantSection from '@/components/products/AddVariantSection.vue'
import type { GandalfConfig, GandalfItem, GandalfStep } from '@/common/utility/wizard.model'

import { useToast } from 'vue-toastification'
import useVuelidate from '@vuelidate/core'
import { helpers, minLength, required } from '@vuelidate/validators'
import type { ProductInput, VariantInput } from '@/common/models/product.model'

export default defineComponent({
    name: 'AddProduct',
    setup() {
        // Wizard
        const theWizard = ref<InstanceType<typeof TheGandalf> | null>(null)
        const wizardItems = ref<GandalfItem[]>([
			{ title: 'Product details', isSkippable: true  },
			{ title: 'Variants' }
		])
        const isWizardCompleted = ref(false)

        // Form
        const productForm = ref<ProductInput>({
            name: null,
            description: null,
            category: [],
            is_publish: false,
            variants: []
        })
        const validation = computed(() => ({
            name: { 
                required: helpers.withMessage(
                    'Name is required',
                    required
                )
            },
            description: { 
                required: helpers.withMessage(
                    'Description is required',
                    required
                )
            },
            variants: { 
                required: helpers.withMessage(
                    'At least 1 variant is required',
                    required
                ),
                minLength: helpers.withMessage(
                    'At least 1 variant is required',
                    minLength(1)
                )
            }
        }))
        const v$ = useVuelidate(validation, productForm.value)
        

        onMounted(() => {
            // console.log('Mounted AddProduct')
        })

        // Services
        const toast = useToast()
        
        const onStep = (step: GandalfStep,
					    config: GandalfConfig) => { }
        
        const onSubmit = () => {
            v$.value.$validate()
            if (v$.value.$error) {
                for (let item of v$.value.$errors) {
                    toast.error(item.$message)
                }
            } else {
                isWizardCompleted.value = true
                toast.success('Added new product!')
            }
            // toast.success('Added new product!')
        }

        /**
         * AddVariantSection onUpdate's emitter receiver
         * @param variants new updated variants
         */
        const onVariantsUpdate = (variants: VariantInput[]) => {
            productForm.value.variants = variants
        }

        /**
         * Update steps isCompleted flag
         */
         watch(v$, (newValue, oldValue) => {
            const step1Completed = (
                !newValue.name.$error && newValue.name.$dirty &&
                !newValue.description.$error && newValue.description.$dirty
            )
            const step2Completed = productForm.value.variants.length > 0

            if (theWizard.value && theWizard.value.steps.length > 0) {
                theWizard.value.steps[0].isCompleted = step1Completed
                theWizard.value.steps[1].isCompleted = step2Completed
            }
        })

		return {
            productForm,
            v$,
            theWizard,
			wizardItems,
            isWizardCompleted,
			onStep,
            onSubmit,
            onVariantsUpdate
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