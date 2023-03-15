<script setup>
import { watch } from "vue";
import { useRoute } from "vue-router";
import { useIdStore } from "../stores/id";
import { useEventStore } from "../stores/event";

const route = useRoute();
const { setId } = useIdStore();
const { id } = useIdStore();
const { fetchEvent } = useEventStore();

watch(
  () => route.query.id,
  async (newId) => {
    if (id != newId) {
      await setId(newId);
      fetchEvent();
    }
  }
);
</script>

<template></template>
