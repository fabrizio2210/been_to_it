<script setup>
import GuestItem from "./GuestItem.vue";
import { storeToRefs } from "pinia";
import { useGuestStore } from "../stores/guest";

const { guests, loading, error, firstGuestsLoading } = storeToRefs(
  useGuestStore()
);
const { fetchGuests } = useGuestStore();

fetchGuests();
</script>

<template>
  <template v-for="guest in guests">
    <GuestItem v-if="typeof guest.nome !== 'undefined' && guest.nome != ''">
      <template #heading>
        <span
          class="guest-list-item"
          :class="[firstGuestsLoading ? 'blur' : 'noblur']"
        >
          {{ guest.nome }}:
        </span>
      </template>
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
<style scoped>
.guest-list-item {
  transition: filter 0.2s;
}

.blur {
  filter: blur(9px);
}

.noblur {
  filter: blur(0px);
}
</style>
