<script setup>
import GuestItem from "./GuestItem.vue";
import { storeToRefs } from "pinia";
import { useGuestStore } from "../stores/guest";

const { guests, loading, error } = storeToRefs(useGuestStore());
const { fetchGuests } = useGuestStore();

fetchGuests();
</script>

<template>
  <template v-for="guest in guests">
    <GuestItem v-if="typeof guest.nome !== 'undefined' && guest.nome != ''">
      <template #heading>{{ guest.nome }}</template>
      {{ guest.viene }}
    </GuestItem>
  </template>
</template>
<script>
export default {
  computed: {},
  created() {},
  methods: {
    boolToIt(bool) {
      if (bool) {
        return "sì";
      } else {
        return "no";
      }
    },
    itToBool(str) {
      if (str == "sì" || str == "si" || str == "true") {
        return true;
      } else {
        return false;
      }
    },
  },
};
</script>
