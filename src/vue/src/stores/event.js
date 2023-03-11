import { defineStore } from "pinia";

export const eventStore = defineStore("event", () => {
  const event = {};

  return { event };
});
