import { defineStore } from "pinia";
import { useIdStore } from "./id";
const apiUrl = window.location.origin;

export const useEventStore = defineStore({
  id: "event",
  state: () => ({
    evento: {
      descrizione_par1: `22 settembre dalle 15.00<br />
      Pinzonerkeller<br />P.za S. Stefano Montagna (BZ)`,
      descrizione_par2: `Seguirà cena in loco <br />
      fino a tarda sera`,
      descrizione_par3: `Per favore, conferma<br />
      la tua presenza cliccando<br />
      sull'interruttore qua sotto<br />`,
    },
    loading: true,
    error: false,
  }),
  actions: {
    async fetchEvent() {
      //this.evento = null;
      this.loading = true;
      var url = new URL(`/api/event`, apiUrl);
      const id = useIdStore();
      const params = {
        uid: id.id,
      };
      url.search = new URLSearchParams(params).toString();
      try {
        var payload = await fetch(url).then((response) => response.json());
        this.evento = payload["event"];
      } catch (error) {
        this.error = error;
      } finally {
        this.loading = false;
      }
    },
  },
});
