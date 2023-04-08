<script>
export default {
  props: {
    notesId: String,
    initialValue: String,
    multiline: Boolean,
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
      :class="[multiline ? 'textbox' : 'input']"
      :id="notesId"
      @blur="changeText()"
      v-model="text"
    />
  </div>
</template>

<style scoped>
textarea {
  left: 10px;
  top: 10px;
  resize: none;
}

.input {
  height: 25px;
  width: 250px;
}

.textbox {
  width: calc(50vw); /* calc and viewport to the rescue */
  height: calc(50vh - 20px);
}
</style>
