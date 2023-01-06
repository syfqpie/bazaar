<template>
    <div
        ref="variantDrawer"
        tabindex="-1"
        class="fixed z-40 h-screen overflow-y-hidden p-4 lg:p-6
        bg-white w-11/12 lg:w-[26rem] right-0 top-0">
        <h5 id="drawer-label" 
            class="inline-flex items-center mb-6 text-base font-semibold 
            text-gray-500 uppercase">
            {{  !isEdit ? 'New' : 'Edit' }} variant
        </h5>
        <button type="button"
            class="text-gray-400 bg-transparent hover:bg-gray-200 
            hover:text-gray-900 rounded-lg text-sm p-3 absolute
            top-2 right-2 lg:top-4 lg:right-4 inline-flex items-center"
            @click="emitToggle()">
            <i class="fa-solid fa-xmark"></i>
            <span class="sr-only">Close menu</span>
        </button>

        <form @submit.prevent>
            <div class="mb-3">
                <label class="text-sm text-gray-700">
                    Variant name
                </label>
                <TheInput
                    type="text"
                    placeholder="Enter variant name"
                    v-model="variantForm.name"
                    :class="{
                        'p-2': true,
                        'border-red-400 focus:!outline-red-200 \
                        focus:!border-red-500': v$.name.$dirty &&
                                                  v$.name.$invalid 
                        
                    }"
                    @blur="v$.name.$touch" />
                <p
                    v-for="error of v$.name.$errors"
                    :key="error.$uid"
                    class="mt-2 text-xs text-red-500">
                    {{ error.$message }}
                </p>
            </div>

            <div class="mb-3">
                <label class="text-sm text-gray-700">
                    SKU no.
                </label>
                <TheInput
                    type="text"
                    placeholder="Enter variant sku no."
                    v-model="variantForm.sku"
                    :class="{
                        'p-2': true,
                        'border-red-400 focus:!outline-red-200 \
                        focus:!border-red-500': v$.sku.$dirty &&
                                                  v$.sku.$invalid 
                        
                    }"
                    @blur="v$.sku.$touch" />
            </div>

            <div class="mb-3 grid grid-cols-2 gap-4">
                <div class="col-span-1">
                    <label class="text-sm text-gray-700">
                        Price
                    </label>
                    <TheInput
                        :type="'number'"
                        placeholder="0.00"
                        v-model="variantForm.price"
                        :class="{
                            'p-2': true,
                            'border-red-400 focus:!outline-red-200 \
                            focus:!border-red-500': v$.price.$dirty &&
                                                      v$.price.$invalid 
                            
                        }"
                        @blur="v$.price.$touch" />
                    <p
                        v-for="error of v$.price.$errors"
                        :key="error.$uid"
                        class="mt-2 text-xs text-red-500">
                        {{ error.$message }}
                    </p>
                </div>

                <div class="col-span-1">
                    <label class="text-sm text-gray-700">
                        Qty.
                    </label>
                    <TheInput
                        :type="'number'"
                        placeholder="0"
                        v-model="variantForm.quantity"
                        :class="{
                            'p-2': true,
                            'border-red-400 focus:!outline-red-200 \
                            focus:!border-red-500': v$.quantity.$dirty &&
                                                      v$.quantity.$invalid 
                            
                        }"
                        @blur="v$.quantity.$touch" />
                    <p
                        v-for="error of v$.quantity.$errors"
                        :key="error.$uid"
                        class="mt-2 text-xs text-red-500">
                        {{ error.$message }}
                    </p>
                </div>
            </div>

            <div class="mb-3 grid grid-cols-2 gap-4">
                <div class="col-span-1">
                    <label class="text-sm text-gray-700">
                        Limit per customer
                    </label>
                    <TheInput
                        :type="'number'"
                        :class="'p-2'"
                        placeholder="0" 
                        v-model="variantForm.customerQuantityLimit"
                        @blur="v$.customerQuantityLimit.$touch" />
                </div>

                <div class="col-span-1">
                    <label class="text-sm text-gray-700">
                        Weight
                    </label>
                    <TheInput
                        :type="'number'"
                        placeholder="0"
                        v-model="variantForm.weight"
                        :class="{
                            'p-2': true,
                            'border-red-400 focus:!outline-red-200 \
                            focus:!border-red-500': v$.weight.$dirty &&
                                                      v$.weight.$invalid 
                            
                        }"
                        @blur="v$.weight.$touch" />
                    <p
                        v-for="error of v$.weight.$errors"
                        :key="error.$uid"
                        class="mt-2 text-xs text-red-500">
                        {{ error.$message }}
                    </p>
                </div>
            </div>
        </form>

        <div class="absolute bottom-0 inset-x-6 py-4 lg:py-6">
            <TheButton 
                v-if="!isEdit"
                :size="'lg'"
                :is-full="true"
                @click="onSave()"> 
                Save
            </TheButton>

            <TheButton 
                v-else
                :size="'lg'"
                :is-full="true"
                @click="onSaveEdit()"> 
                Update
            </TheButton>
        </div>
    </div>
</template>

<script lang="ts">
import { computed, onMounted, defineComponent, ref } from 'vue'

import TheButton from '@/components/basics/TheButton.vue'
import TheInput from '@/components/basics/TheInput.vue'
import type { AddVariantList, VariantBaseInput } from '@/common/models/product.model'

import useVuelidate from '@vuelidate/core'
import { helpers, required, maxLength, minValue } from '@vuelidate/validators'
import { onClickOutside } from '@vueuse/core'

export default defineComponent({
    name: 'VariantDrawer',
    setup(props, context) {
        // Component ref
        const variantDrawer = ref(null)

        // Form
        const variantForm = ref<VariantBaseInput>({
            name: (
                props.variantItem ? props.variantItem.name : null
            ),
            price: (
                props.variantItem ? props.variantItem.price : null
            ), 
            quantity: (
                props.variantItem ? props.variantItem.quantity : null
            ),
            sku: (
                props.variantItem ? props.variantItem.sku : null
            ),
            weight: (
                props.variantItem ? props.variantItem.weight : null
            ),
            customerQuantityLimit: (
                props.variantItem ? props.variantItem.customerQuantityLimit : null
            )
        })
        const validation = computed(() => ({
            name: {
                required: helpers.withMessage(
                    'Name is required',
                    required
                ),
                maxLength: helpers.withMessage(
                    'Max length is 128 words',
                    maxLength(128)
                )
            },
            price: {
                required: helpers.withMessage(
                    'Price is required',
                    required
                ),
                minValue: helpers.withMessage(
                    'Min price is 0.00',
                    minValue(0.00)
                )
            },
            quantity: {
                required: helpers.withMessage(
                    'Quantity is required',
                    required
                ),
                minValue: helpers.withMessage(
                    'Min quantity is 0',
                    minValue(0)
                )
            },
            sku: { },
            weight: {
                minValue: helpers.withMessage(
                    'Min weight is 0',
                    minValue(0)
                )
            },
            customerQuantityLimit: {
                minValue: helpers.withMessage(
                    'Min limit is 0',
                    minValue(0)
                )
            }
        }))
        const v$ = useVuelidate(validation, variantForm.value)

        onMounted(() => {
            // console.log('Mounted VariantDrawer')
        })

        const onSave = () => {
            // Validate
            v$.value.$touch()

            if (v$.value.$invalid) {
                // noop
            } else {
                emitSave()
            }
        }

        const onSaveEdit = () => {
            // Validate
            v$.value.$touch()

            if (v$.value.$invalid) {
                // noop
            } else {
                emitUpdate()
            }
        }

        const emitUpdate = () => {
            if (props.variantItem) {
                context.emit('onUpdate',
                             variantForm.value,
                             props.variantItem.idx)
            }
        }

        const emitSave = () => {
            context.emit('onSave', variantForm.value)
        }

        const emitToggle = () => {
            context.emit('onToggle')
        }

        // Event
        onClickOutside(variantDrawer, (event) => {
            emitToggle()
        })

        return {
            variantForm,
            v$,
            validation,
            onSave,
            onSaveEdit,
            variantDrawer,
            emitToggle
        }
    },
    components: { TheButton, TheInput },
    props: {
        isEdit: {
            type: Boolean,
            default: false
        },
        variantItem: {
            type: Object as () => AddVariantList | null,
            default: null
        }
    },
    emits: ['onToggle', 'onSave', 'onUpdate']
})
</script>