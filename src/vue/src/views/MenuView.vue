<script setup>
import { useEventStore } from "../stores/event";
import { storeToRefs } from "pinia";
const { evento } = storeToRefs(useEventStore());
</script>

<template>
  <div class="menu">
    <div v-if="evento.menu !== ''" v-html="evento.menu"></div>
  </div>
</template>

<script>
export default {
  methods: {
    itToBool(str) {
      str = str.toLowerCase();
      if (str == "sì" || str == "si" || str == "true") {
        return true;
      } else {
        return false;
      }
    },
  },
};
</script>
<style>
.poster {
  position: relative;
  width: 100%;
}
</style>
