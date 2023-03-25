import { defineStore } from "pinia";
import { useIdStore } from "./id";
const apiUrl = window.location.origin;

export const useGuestStore = defineStore({
  id: "guest",
  state: () => ({
    guest: {},
    guests: [],
    loading: false,
    error: false,
  }),
  actions: {
    async fetchGuest() {
      this.guest = {};
      this.loading = true;
      const id = useIdStore();
      var url = new URL(`/api/guest/${id.id}`, apiUrl);
      try {
        var payload = await fetch(url).then((response) => response.json());
        this.guest = payload["guest"];
      } catch (error) {
        this.error = error;
      } finally {
        this.loading = false;
      }
    },
    async fetchGuests() {
      this.guests = [];
      this.loading = true;
      var url = new URL(`/api/guests`, apiUrl);
      try {
        var payload = await fetch(url).then((response) => response.json());
        this.guests = payload["guests"];
      } catch (error) {
        this.error = error;
      } finally {
        this.loading = false;
      }
    },
    async updateGuest(attr) {
      this.loading = true;
      const id = useIdStore();
      var url = new URL(`/api/guest/${id.id}`, apiUrl);
      const requestOptions = {
        headers: {
          "Content-Type": "application/json",
        },
        method: "PUT",
        body: JSON.stringify(attr),
      };
      try {
        var payload = await fetch(url, requestOptions).then((response) =>
          response.json()
        );
        this.guest = payload["guest"];
      } catch (error) {
        this.error = error;
      } finally {
        this.loading = false;
      }
    },
  },
});
