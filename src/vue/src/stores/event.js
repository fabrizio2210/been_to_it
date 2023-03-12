import { defineStore } from 'pinia'
import { useIdStore } from './id'
const apiUrl = window.location.origin

export const useEventStore = defineStore({
  id: "event",
  state: () => ({
    evento: {},
    loading: false,
    error: false,
  }),
  actions: {
    async fetchEvent() {
      this.evento = null;
      this.loading = true;
      var url = new URL(`/api/event`, apiUrl);
      const id = useIdStore()
      const params = {
        uid: id.id
      };
      url.search = new URLSearchParams(params).toString();
      try {
        var payload = await fetch(url).then((response) =>
          response.json()
        );
        this.evento = payload["event"];
      } catch (error) {
        this.error = error;
      } finally {
        this.loading = false;
      }
    },
  },
});
