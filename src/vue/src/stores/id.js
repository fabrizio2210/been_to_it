import { defineStore } from "pinia";

export const useIdStore = defineStore({
  id: "id",
  state: () => ({
    id: localStorage.getItem("id"),
  }),
  actions: {
    setId(id) {
      this.id = id;
      localStorage.setItem("id", id);
    },
  },
});
