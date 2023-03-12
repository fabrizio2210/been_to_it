<script setup>
  import { watch } from 'vue'
  import { useRoute } from 'vue-router'
  import { useIdStore } from '../stores/id'

  const route = useRoute()
  const { setId } = useIdStore()
  const { id } = useIdStore()

  watch(
    () => route.query.id,
    async id => { await setId(id) }
  )
</script>

<template>
</template>
