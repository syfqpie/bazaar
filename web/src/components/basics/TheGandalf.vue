<template>
	<ol class="wizard text-sm">
		<li
			v-for="step of steps"
			class="wizard-step cursor-pointer"
			:class="{
				'is-current': config.current === step.idx,
				'is-completed': step.isCompleted,
				'is-visited': step.isVisited,
				'is-skippable': step.isSkippable
			}"
			:key="step.idx">
			<span
				class="wizard-step-counter
				transition-colors duration-150
				after:transition-all after:duration-150">
			</span>

			<a
				class="wizard-step-link transition-colors duration-150"
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
		 * TODO:
		 * 	1. Add logic for 
		 * 	   - skippable
		 *     - completed
		 *  2. Complete step is in template
		 * 
		 * @param next next step index
		 */
		const isValidStep = (next: number,
							 initial: boolean =false) => {
			const validStep: boolean = next >= config.value.first! &&
									   next < config.value.total

			return validStep
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
			if (isValidStep(next, initial)) {
				// Update config
				config.value.previous = next !== config.value.first
											   ? next - 1
											   : null
				config.value.next = next !== config.value.last!
										   ? next + 1
										   : null
				config.value.current = next

				// Update current step as visited
				if (!steps.value[config.value.current].isVisited) {
					steps.value[config.value.current].isVisited = true
				}
			}

			// Post signal
			postGoStep()
		}

		/**
		 * Go to next step
		 */
		const nextStep = () => {
			if (config.value.next !== null &&
				config.value.total > 0 &&
				config.value.current! < config.value.total) {
				goStep(config.value.next)
			}
		}

		/**
		 * Back step 
		 */
		const backStep = () => {
			if (config.value.previous !== null &&
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
	--wizard-step-completed: #a5b4fc;
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
	background-color: var(--wizard-step-completed);
	color: var(--wizard-bg);
}

.wizard .wizard-step .wizard-step-counter:before {
	content: counter(stepper);
}

.wizard .wizard-step.is-visited .wizard-step-counter:after {
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

.wizard .wizard-step.is-visited:not(.is-current):not(.is-skippable) .wizard-step-counter:after {
	background-color: var(--wizard-step);
	background-size: 0.55rem;
	/* Refered to @fortawesome/fontawesome-free/svgs/solid/triangle-exclamation.svg */
	background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 512 512'%3e%3cpath fill='%236366f1' d='M256 32c14.2 0 27.3 7.5 34.5 19.8l216 368c7.3 12.4 7.3 27.7 .2 40.1S486.3 480 472 480H40c-14.3 0-27.6-7.7-34.7-20.1s-7-27.8 .2-40.1l216-368C228.7 39.5 241.8 32 256 32zm0 128c-13.3 0-24 10.7-24 24V296c0 13.3 10.7 24 24 24s24-10.7 24-24V184c0-13.3-10.7-24-24-24zm32 224c0-17.7-14.3-32-32-32s-32 14.3-32 32s14.3 32 32 32s32-14.3 32-32z'/%3e%3c/svg%3e");
}

.wizard .wizard-step.is-current .wizard-step-counter:after {
	background-color: var(--wizard-step);
	background-size: 0.55rem;
	/* Refered to @fortawesome/fontawesome-free/svgs/solid/wand-magic-sparkles.svg */
	background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 576 512'%3e%3cpath fill='%236366f1' d='M234.7 42.7L197 56.8c-3 1.1-5 4-5 7.2s2 6.1 5 7.2l37.7 14.1L248.8 123c1.1 3 4 5 7.2 5s6.1-2 7.2-5l14.1-37.7L315 71.2c3-1.1 5-4 5-7.2s-2-6.1-5-7.2L277.3 42.7 263.2 5c-1.1-3-4-5-7.2-5s-6.1 2-7.2 5L234.7 42.7zM46.1 395.4c-18.7 18.7-18.7 49.1 0 67.9l34.6 34.6c18.7 18.7 49.1 18.7 67.9 0L529.9 116.5c18.7-18.7 18.7-49.1 0-67.9L495.3 14.1c-18.7-18.7-49.1-18.7-67.9 0L46.1 395.4zM484.6 82.6l-105 105-23.3-23.3 105-105 23.3 23.3zM7.5 117.2C3 118.9 0 123.2 0 128s3 9.1 7.5 10.8L64 160l21.2 56.5c1.7 4.5 6 7.5 10.8 7.5s9.1-3 10.8-7.5L128 160l56.5-21.2c4.5-1.7 7.5-6 7.5-10.8s-3-9.1-7.5-10.8L128 96 106.8 39.5C105.1 35 100.8 32 96 32s-9.1 3-10.8 7.5L64 96 7.5 117.2zm352 256c-4.5 1.7-7.5 6-7.5 10.8s3 9.1 7.5 10.8L416 416l21.2 56.5c1.7 4.5 6 7.5 10.8 7.5s9.1-3 10.8-7.5L480 416l56.5-21.2c4.5-1.7 7.5-6 7.5-10.8s-3-9.1-7.5-10.8L480 352l-21.2-56.5c-1.7-4.5-6-7.5-10.8-7.5s-9.1 3-10.8 7.5L416 352l-56.5 21.2z'/%3e%3c/svg%3e");
}

.wizard .wizard-step:is(.is-completed, .is-skippable):not(.is-current) .wizard-step-counter:after {
	background-color: var(--wizard-step);
	background-size: 0.55rem;
	/* Refered to @fortawesome/fontawesome-free/svgs/solid/check.svg */
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 512 512'%3E%3Cpath fill='%236366f1' d='M470.6 105.4c12.5 12.5 12.5 32.8 0 45.3l-256 256c-12.5 12.5-32.8 12.5-45.3 0l-128-128c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0L192 338.7 425.4 105.4c12.5-12.5 32.8-12.5 45.3 0z'/%3E%3C/svg%3E");
}

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