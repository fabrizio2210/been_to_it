<script setup>
import { useEventStore } from "../stores/event";
import { storeToRefs } from "pinia";
const { evento } = storeToRefs(useEventStore());
</script>

<template>
  <div class="menu">
    <img
      v-if="
        typeof evento !== 'undefined' &&
        evento !== null &&
        typeof evento.allergie !== 'undefined' &&
        itToBool(evento.allergie)
      "
      id="menu-aperitivo"
      class="poster"
      src="@/assets/aperitivo_menu.png"
      alt="menu aperitivo"
    />
    <img
      v-if="
        typeof evento !== 'undefined' &&
        evento !== null &&
        typeof evento.allergie !== 'undefined' &&
        itToBool(evento.allergie)
      "
      id="menu-cena"
      class="poster"
      src="@/assets/cena_menu.png"
      alt="BARBEQUE ALLA PINZONERKELLER, Sparerips di maiale, Coscette di pollo marinate al curry e thimo, Salsicce fatte in casa, Roastbeef grigliato tutto d'un pezzo e poi tranciato davanti agli ospiti, Formaggio alla griglia (mini Tomini), Verdure mediterranee grigliate, patate al rosmarino, Polenta cremosa da paiuolo, salsettine fatte in casa (barbeque, salsa verde, maionaise al rafano,…), Bevande per la cena, Vino bianco Sauvignon, Vino rosso Ripasso Valpolicella, Birra alla spina, Acqua, Succhi e softdrinks, Un giro di caffè ed amari/grappe a fine pasto"
    />
    <img
      v-if="
        typeof evento !== 'undefined' &&
        evento !== null &&
        typeof evento.allergie !== 'undefined' &&
        itToBool(evento.allergie)
      "
      id="menu-notte"
      class="poster"
      src="@/assets/notte_menu.png"
      alt="menu notte"
    />
  </div>
</template>

<script>
export default {
  methods: {
    itToBool(str) {
      str = str.toLowerCase();
      if (str == "sì" || str == "si" || str == "true") {
        return true;
      } else {
        return false;
      }
    },
  },
};
</script>
<style>
.poster {
  position: relative;
  width: 100%;
}
</style>
