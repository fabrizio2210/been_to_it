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
      v-model="text"
    />
  </div>
</template>

<style scoped>
textarea {
  left:10px; top:10px;
  width:  calc(50vw - 20px);      /* calc and viewport to the rescue */
  height: calc(50vh - 20px);
  resize: none;
}
</style>
