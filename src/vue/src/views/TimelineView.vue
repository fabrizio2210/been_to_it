<script setup>
import { useEventStore } from "../stores/event";
import { storeToRefs } from "pinia";
const { evento } = storeToRefs(useEventStore());
</script>

<template>
  <div class="timeline">
    <h3>La timeline verrà mostrata qui.</h3>
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
