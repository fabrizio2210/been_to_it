<script setup>
import { useIdStore } from "../stores/id";
import { storeToRefs } from "pinia";

const { id } = storeToRefs(useIdStore());

</script>

<template>
  <div class="photobook">
    <h2>Carica e vedi le foto durante il matrimonio su <a v-bind:href="url" >
    i.ve.been.to.it</a></h2>
  </div>
</template>

<script>
export default {
  computed: {
    url() {
      const {id} = storeToRefs(useIdStore());
      var url = "http://i.ve.been.to.it";
      if (typeof id !== 'undefined' && id.value !== null) {
        url = url + "?id=" + id.value;
      }
      return url;
    }
  }
}

</script>

<style>
.photobook {
  height: 500px;
}
</style>
