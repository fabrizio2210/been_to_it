<script setup>
import { useEventStore } from "../stores/event";
import { storeToRefs } from "pinia";
const { evento } = storeToRefs(useEventStore());
</script>

<template>
  <div class="menu">
    <h3>Il menù verrà mostrato qui</h3>
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
