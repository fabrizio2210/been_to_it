<script setup>
import Guests from "../components/Guests.vue"
</script>

<template>
  <div class="guests">
    <Guests />
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .guests {
    min-height: 100vh;
    display: flex;
    flex-flow: column;
  }
}
</style>
