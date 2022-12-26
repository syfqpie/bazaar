<template>
	<ol class="wizard text-sm">
		<li
			v-for="step of steps"
			:key="step.idx"
			class="wizard-step cursor-pointer"
			:class="{
				'is-current': config.current === step.idx,
				'is-completed': step.isCompleted,
				'is-visited': step.isVisited
			}">
			<span class="wizard-step-counter"></span>

			<a
				class="wizard-step-link"
				@click="goStep(step.idx)">
				<span>{{ step.title }}</span>
			</a>

			<span class="wizard-step-line"></span>
		</li>
	</ol>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue'
import type { GandalfConfig, GandalfItem, GandalfStep } from '@/common/utility/wizard.model'

export default defineComponent({
	name: 'TheGandalf',
	setup(props, context) {
		
		const steps = ref<GandalfStep[]>([])
		const config = ref<GandalfConfig>({
			current: null,
			next: null,
			previous: null,
			first: null,
			last: null,
			total: 0
		})

		onMounted(() => {
			initSetup()
		})

		/**
		 * Init wizard setup. if items is
		 * empty list, then a console warn will
		 * be printed
		 */
		const initSetup = () => {
			if (props.items.length > 0) {
				// Map into wizard internal data
				steps.value = props.items.map(
					(item, index) => {
						let toSave = {
							idx: index,
							isVisited: false,
							isCompleted: false
						}
						return {
							...item,
							...toSave
						}
					}
				)

				// Go to root step
				goStep(0, true)
			} else {
				console.warn('0 or less')
			}
		}

		/**
		 * Validation for step.
		 * Should be call before using jumping
		 * step.
		 * 
		 * @param next next step index
		 */
		const isValidStep = (next: number) => {
			return (
				next >= config.value.first! &&
				next < config.value.total
			)
		}

		/**
		 * Go to the step index provided
		 * 
		 * @param next step to go index
		 * @param initial if this is initial?
		 */
		const goStep = (next: number,
						initial: boolean = false) => {
			if (initial) {
				// Set config initial values
				config.value.first = 0
				config.value.last = steps.value.length - 1
				config.value.total = steps.value.length
			}

			// Pre signal
			preGoStep()

			// Go step and update config
			if (isValidStep(next)) {
				// Update config
				config.value.previous = next !== config.value.first
											   ? next - 1
											   : null
				config.value.next = next !== config.value.last!
										   ? next + 1
										   : null
				config.value.current = next

				// Update current step as visited
				if (!steps.value[config.value.current].isCompleted) {
					steps.value[config.value.current].isCompleted = true
				}
			}

			// Post signal
			postGoStep()
		}

		/**
		 * Go to next step
		 */
		const nextStep = () => {
			if (config.value.next &&
				config.value.total > 0 &&
				config.value.current! < config.value.total) {
				goStep(config.value.next)
			}
		}

		/**
		 * Back step 
		 */
		const backStep = () => {
			if (config.value.previous &&
				config.value.total > 0 &&
				config.value.current! > 0) {
				goStep(config.value.previous)
			}
		}

		/**
		 * Pre go step signal.
		 */
		const preGoStep = () => {
			context.emit('onPreStep',
						  config.value,
						  steps.value)
		}

		/**
		 * Post go step singal.
		 */
		const postGoStep = () => {
			context.emit('onPostStep',
						  config.value,
						  steps.value)
		}

		return {
			config,
			steps,
			goStep,
			nextStep,
			backStep,
			preGoStep,
			postGoStep
		}
	},
	props: {
		items: {
			type: Array as () => GandalfItem[],
			default: []
		}
	},
	emits: [
		'onPreStep',
		'onPostStep'
	]
})
</script>

<style>
:root {
	--wizard-step-active: #6366f1;
	--wizard-step: #e0e7ff;
	--wizard-bg: #fff;
	--wizard-not-active-link: #818cf8;
}

.wizard {
	display: flex;
	flex-direction: column;
	counter-reset: stepper;
	gap: 8px;
	background-color: var(--wizard-bg);
}

.wizard .wizard-step {
	display: grid;
	grid-template-rows: [text-row] auto [line-row] 20px;
	grid-template-columns: [counter-column] 28px [text-column] auto;
	column-gap: 16px;
	row-gap: 8px;
	position: relative;
}

.wizard .wizard-step:last-child {
	grid-template-rows: [text-row] auto;
}

.wizard .wizard-step .wizard-step-counter {
	flex-shrink: 0;
	counter-increment: stepper;
	display: flex;
	align-items: center;
	justify-content: center;
	width: 28px;
	height: 28px;
	background-color: var(--wizard-step);
	color: var(--wizard-step-active);
	border-radius: 50%;
	line-height: 1;
	position: relative;
}

.wizard .wizard-step.is-current .wizard-step-counter {
	background-color: var(--wizard-step-active);
	color: var(--wizard-step);
}

.wizard .wizard-step.is-completed:not(.is-current) .wizard-step-counter {
	background-color: var(--wizard-step);
	color: var(--wizard-step-active);
}

.wizard .wizard-step .wizard-step-counter:before {
	content: counter(stepper);
}

.wizard .wizard-step.is-completed .wizard-step-counter:after {
	position: absolute;
	content: "";
	display: block;
	width: 16px;
	height: 16px;
	border-radius: 50%;
	right: -6px;
	bottom: -6px;
	background-size: 12px;
	background-repeat: no-repeat;
	background-position: center center;
}

.wizard .wizard-step.is-completed .wizard-step-counter:after {
	background-color: var(--wizard-step);
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' width='24' height='24'%3E%3Cpath fill='none' d='M0 0h24v24H0z'/%3E%3Cpath fill='%236366f1' d='M10 15.172l9.192-9.193 1.415 1.414L10 18l-6.364-6.364 1.414-1.414z'/%3E%3C/svg%3E");
}

/* .wizard .wizard-step.is-completed:not(.is-current) .wizard-step-counter:after {
  background-color: var(--wizard-step-active);
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' width='24' height='24'%3E%3Cpath fill='none' d='M0 0h24v24H0z'/%3E%3Cpath fill='%23e0e7ff' d='M10 15.172l9.192-9.193 1.415 1.414L10 18l-6.364-6.364 1.414-1.414z'/%3E%3C/svg%3E");
} */

.wizard .wizard-step:not(:first-child) .wizard-step-line {
	display: block;
	width: 2px;
	background-color: var(--wizard-step);
	height: 1.25rem;
	justify-self: center;
	margin-top: -4rem;
}

.wizard .wizard-step:not(:first-child).is-completed .wizard-step-line {
	background-color: var(--wizard-step-active);
}

.wizard .wizard-step .wizard-step-link {
	display: flex;
	gap: 12px;
	text-decoration: none;
	color: var(--wizard-not-active-link);
}

.wizard .wizard-step.is-current .wizard-step-link {
	color: var(--wizard-step-active);
}

.wizard .wizard-step .wizard-step-link span {
	padding-top: calc((28px - 1.5em) / 2);
	font-weight: 600;
	border-bottom: 2px solid transparent;
}

.wizard .wizard-step .wizard-step-link:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
}

.wizard .wizard-step .wizard-step-link:hover span {
	border-color: currentcolor;
}

.wizard .wizard-step .wizard-step-link:focus {
	outline-offset: 4px;
	outline-color: var(--wizard-step-active);
	outline-width: 2px;
	border-radius: 4px;
}
</style>