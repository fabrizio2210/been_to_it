import { defineStore } from "pinia";
const apiUrl = window.location.origin;

export const useEventStore = defineStore({
  id: 'event',
  state: () => ({
    evento: {},
    loading: false,
    error: false
  }),
  actions: {
    async fetchEvent() {
      this.evento = null;
      this.loading = true;
      try {
        var payload = await fetch(`${apiUrl}/api/event`).then((response) =>
          response.json()
        );
        this.evento = payload['event']
      } catch (error) {
        this.error = error;
      } finally {
        this.loading = false;
      }
    }
  }
});
