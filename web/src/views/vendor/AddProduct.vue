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

        <div class="grid grid-cols-12 divide-x mt-4">
            <div class="col-span-3 lg:pr-6">
                <TheGandalf
                    ref="theWizard"
                    :items="wizardItems"
                    :isCompleted="isWizardCompleted"
                    @on-post-step="onStep" />
            </div>

            <div class="col-span-9 overflow-scroll max-h-[80vh] lg:pl-6">
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
                            <label class="text-sm">
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
                            :is-wizard-on-submit="isWizardOnSubmit"
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
                                v-if="!isWizardCompleted"
                                size="sm"
                                class="rounded-l-none border-l-0"
                                :disabled="isWizardCompleted"
                                @click="onSubmit">
                                Submit
                            </TheOutlineButton>

                            <TheOutlineButton
                                v-else
                                size="sm"
                                class="rounded-l-none border-l-0"
                                @click="theWizard?.nextStep()">
                                <i class="fa-solid fa-chevron-down"></i>
                            </TheOutlineButton>
                        </div>
                    </div>

                    <div class="mb-3" v-else-if="theWizard?.config.current === 2">
                        <div
                            class="flex flex-row align-middle items-center">
                            <div class="basis-3/12">
                                <img
                                    v-if="isWizardOnSubmit && !isWizardCompleted"
                                    src="@/assets/img/icons/package-on-conveyor.png"
                                    class="h-auto w-9/12"
                                    alt="Empty" />
                                
                                <img
                                    v-else-if="!isWizardOnSubmit && isWizardCompleted"
                                    src="@/assets/img/icons/package-checked.png"
                                    class="h-auto w-9/12"
                                    alt="Empty" />
                            </div>

                            <div class="basis-9/12">
                                <div v-if="isWizardOnSubmit && !isWizardCompleted">
                                    <p class="text-sm text-gray-900">
                                        <span class="font-semibold text-indigo-700">Processing.</span>
                                        You product with the variants are being processed.
                                    </p>
                                    <p class="text-sm mb-2">
                                        Please wait...
                                    </p>
                                </div>

                                <div v-else-if="!isWizardOnSubmit && isWizardCompleted">
                                    <p class="text-sm text-gray-900">
                                        <span class="font-semibold text-indigo-700">Success!</span>
                                        You product with the variants has been saved!
                                    </p>
                                    <p class="text-sm mb-2">
                                        Please wait, you will be redirected to
                                        the product main page in 5 seconds..
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </form>
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
import type { ProductInput } from '@/common/models/product.model'
import type { VariantInput } from '@/common/models/variant.model'
import { useProductStore } from '@/stores'

import { useToast } from 'vue-toastification'
import useVuelidate from '@vuelidate/core'
import { helpers, minLength, required } from '@vuelidate/validators'
import { useRouter } from 'vue-router'

export default defineComponent({
    name: 'AddProduct',
    setup() {
        // Wizard
        const theWizard = ref<InstanceType<typeof TheGandalf> | null>(null)
        const wizardItems = ref<GandalfItem[]>([
			{ title: 'Product details', isSkippable: true  },
			{ title: 'Variants' },
            { title: 'Completed', isSkippable: true, isNoIcon: true }
		])
        const isWizardCompleted = ref(false)
        const isWizardOnSubmit = ref(false)

        // Form
        const productForm = ref<ProductInput>({
            name: null,
            description: null,
            category: [],
            isPublish: false,
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

        // Services
        const router = useRouter()
        const toast = useToast()
        const productStore = useProductStore()
        
        onMounted(() => {
            // console.log('Mounted AddProduct')
        })
        
        /**
         * On step callback function
         * 
         * @param step current step
         * @param config current config
         */
        const onStep = (step: GandalfStep,
					    config: GandalfConfig) => { }
        
        /**
         * Submit form to create new product.
         * Would call validate first and only
         * proceed to request if no error found.
         * 
         */
        const onSubmit = () => {
            v$.value.$validate()
            if (v$.value.$error) {
                toast.error('Form not valid. Please check')
            } else {
                theWizard.value!.steps[2].isCompleted = true
                isWizardOnSubmit.value = true
                createProduct()
            }
        }

        /**
         * TODO:
         *      Redirect to product page after success
         */
        const createProduct = () => {
            return productStore.create(productForm.value)
                .then(data => {
                    toast.success('Added new product!')
                    isWizardOnSubmit.value = false
                    isWizardCompleted.value = true

                    // hack
                    setTimeout(() => {
                        return theWizard.value!.nextStep()
                    }, 200)

                    setTimeout(() => {
                        const nextPath = `${ data.id }/details`
                        return router.push({ path: nextPath })
                    }, 5200)
                    
                })
                .catch(err => {
                    toast.error('Error')
                    isWizardOnSubmit.value = false
                })
        }

        /**
         * AddVariantSection onUpdate's emitter receiver
         * 
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

        /**
         * Update complete step title
         * when on submit (loading state)
         */
        watch(isWizardOnSubmit, (newValue, oldValue) => {
            if (theWizard.value && newValue) {
                theWizard.value.steps[wizardItems.value.length - 1].title = 'Submitting...'
            } else if (theWizard.value && !newValue) {
                theWizard.value.steps[wizardItems.value.length - 1].title =
                    wizardItems.value[wizardItems.value.length - 1].title
            }
        })

		return {
            productForm,
            v$,
            theWizard,
			wizardItems,
            isWizardCompleted,
            isWizardOnSubmit,
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