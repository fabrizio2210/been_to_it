<script setup>
import { useEventStore } from "../stores/event";
import { storeToRefs } from "pinia";
const { evento } = storeToRefs(useEventStore());
</script>

<template>
  <div class="timeline">
    <img 
      id=timeline
      class="poster"
      src="@/assets/timeline.png"
      alt="15.30 cerimonia, 17:00 aperitvo & fingerfood, 19:00 cena grigliata, 22:00 taglio torta, 22:30 brindisi, 22:45 first dance, 24:00 spaghettata, 24:30 party"
    />
    <img 
      v-if="typeof evento !== 'undefined' && evento !== null && typeof evento.allergie !== 'undefined' && itToBool(evento.allergie)"
      id=menu-cena
      class="poster"
      src="@/assets/cena_menu.png"
      alt="BARBEQUE ALLA PINZONERKELLER, Sparerips di maiale, Coscette di pollo marinate al curry e thimo, Salsicce fatte in casa, Roastbeef grigliato tutto d'un pezzo e poi tranciato davanti agli ospiti, Formaggio alla griglia (mini Tomini), Verdure mediterranee grigliate, patate al rosmarino, Polenta cremosa da paiuolo, salsettine fatte in casa (barbeque, salsa verde, maionaise al rafano,…), Bevande per la cena, Vino bianco Sauvignon Fallwind cantina Appiano, Vino rosso Ripasso Valpolicella, Birra alla spina, Acqua, Succhi e softdrinks, Un giro di caffè ed amari/grappe a fine pasto"
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
    }
  }
}
</script>
<style>
.poster {
  position: relative;
  width: 100%;
}
</style>
