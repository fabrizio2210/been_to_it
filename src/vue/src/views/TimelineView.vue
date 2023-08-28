<script setup>
import { useEventStore } from "../stores/event";
import { storeToRefs } from "pinia";
const { evento } = storeToRefs(useEventStore());
</script>

<template>
  <div class="timeline">
    <img
      id="timeline"
      v-if="typeof evento !== 'undefined' && evento !== null && evento.id == 0"
      class="poster"
      src="@/assets/timeline.png"
      alt="15.30 cerimonia, 17:00 aperitvo & fingerfood, 19:00 cena grigliata, 22:00 taglio torta, 22:30 brindisi, 22:45 first dance, 24:00 spaghettata, 24:30 party"
    />
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
