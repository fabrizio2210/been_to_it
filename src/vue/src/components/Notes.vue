<script>
export default {
  props: {
    notesId: String,
    initialValue: String,
  },
  methods: {
    changeText() {
      this.$emit("changeText", this.text);
    },
  },
  data() {
    return { text: this.initialValue };
  },
};
</script>
<template>
  <div class="notes">
    <label :for="notesId">
      <div></div>
    </label>
    <textarea
      :id="notesId"
      @blur="changeText()"
      rows="4"
      cols="50"
      v-model="text"
    />
  </div>
</template>

<style scoped>
</style>
