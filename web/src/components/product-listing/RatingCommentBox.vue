<template>
    <article 
        class="md:gap-8 md:grid md:grid-cols-3">
        <div>
            <div class="flex items-center mb-6 space-x-4">
                <img
                    class="w-10 h-10 rounded-full" 
                    :src="userImage">
                <div class="space-y-1 font-medium">
                    <p>{{ userName }}</p>
                    <!-- <div class="flex items-center text-sm text-gray-500 dark:text-gray-400">
                        <i class="fa-brands fa-canadian-maple-leaf w-5 mr-1.5"></i>
                        {{ userCountry }}
                    </div> -->
                </div>
            </div>
            <ul class="space-y-4 text-sm text-gray-500 dark:text-gray-400">
                <li class="flex items-center">
                    <i class="w-5 mr-1.2 fas fa-calendar-check"></i>
                    {{ userJoinDate }}
                </li>
            </ul>
        </div>
        <div class="col-span-2 mt-6 md:mt-0">
            <div class="flex items-start mb-5">
                <div class="pr-4">
                    <footer>
                        <p class="mb-2 text-sm text-gray-500 dark:text-gray-400">
                            Reviewed:
                            <time>
                            {{ userProductReviewDate }}
                            </time>
                        </p>
                    </footer>
                    <h4 class="text-xl font-bold text-gray-900">
                        {{ userProductReviewTitle }}
                    </h4>
                </div>
                <p 
                    class="bg-slate-700 lg:outline outline-7  
                    outline-indigo-500 font-medium text-sm 
                    text-slate-100 text-center mb-3 inline-flex 
                    items-center p-1.5 rounded-md shadow-sm">
                    {{ userProductReviewRating }}
                </p>
            </div>
            <p class="mb-2 font-light text-gray-500 dark:text-gray-400">
                {{ userProductReviewComment }}
            </p>
            <aside class="flex items-center mt-3 space-x-5">
                <a 
                    @click="onHelpful()"
                    class="cursor-pointer inline-flex items-center text-sm font-medium
                    text-blue-600 hover:underline dark:text-blue-500"
                    >
                <i class="fas fa-thumbs-up w-4 h-4 mr-1.5"></i>
                Helpful
                </a>
                <a  
                    @click="onNotHelpful()"
                    class="cursor-pointer inline-flex items-center text-sm font-medium
                    text-blue-600 hover:underline dark:text-blue-500 group"
                    >
                <i class="fas fa-thumbs-down w-4 h-4 mr-1.5"></i>
                Not helpful
                </a>
            </aside>
        </div>
    </article>
</template>


<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
    name: 'RatingCommentBox',
    setup(props, context) {
        /**
         * Emit Helpful signal to listener
         */
        const onHelpful = ()  => {
            context.emit('onHelpful')
        }

        /**
         * Emit Not helpful signal to litener
         */
         const onNotHelpful = ()  => {
            context.emit('onNotHelpful')
        }

        return {
            onNotHelpful,
            onHelpful
        }
    },
    props: {
        userName: {
            type: String,
            required: true
        },
        // userCountry: {
        //     type: String,
        //     required: true
        // },
        userImage: {
            type: String,
            required: true,
            // default: '@/assets/img/default/user-icon.png'
        },
        userJoinDate: {
            type: String,
            required: true
        },
        userProductReviewDate: {
            type: String,
            required: true
        },
        userProductReviewTitle:{
            type: String,
            required: true
        },
        userProductReviewRating:{
            type: String,
            required: true
        },
        userProductReviewComment: {
            type: String,
            required: true
        }
    },
    emits: [
        'onHelpful',
        'onNotHelpful'
    ]
})
</script>