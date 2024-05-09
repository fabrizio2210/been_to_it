<script setup>
import { useEventStore } from "../stores/event";
import { storeToRefs } from "pinia";
const { evento } = storeToRefs(useEventStore());
</script>

<template>
  <div class="timeline">
    <div v-if="evento.timeline !==''" v-html="evento.timeline"></div>
  </div>
</template>

<script>
export default {};
</script>
<style>
.poster {
  position: relative;
  width: 100%;
}
</style>
