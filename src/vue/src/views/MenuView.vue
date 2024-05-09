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
.title {
  color: #535959;
  text-align: center;
  padding-top: 20px;
  font-family: glacial-indifference-bold;
}
.item {
  color: #535959;
  text-align: center;
  font-family: glacial-indifference-regular;
}
ul {
  padding-inline-start: 0; 
  list-style-type: none;
}
.poster {
  position: relative;
  width: 100%;
}
</style>
