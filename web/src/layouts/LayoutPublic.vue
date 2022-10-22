<template>
    <NavbarPublic />
    <router-view />
</template>

<script lang="ts">
import { onMounted, defineComponent } from 'vue';
import NavbarPublic from '@/components/navbars/NavbarPublic.vue';

export default defineComponent({
    name: 'LayoutPublic',
    setup() {
        onMounted(() => {
            // console.log('Mounted LayoutPublic');
        });

        return {};
    },
    components: {
        NavbarPublic
    }
});
</script>