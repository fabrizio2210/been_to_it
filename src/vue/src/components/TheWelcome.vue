<script setup>
import WelcomeItem from "./WelcomeItem.vue";
import Switch from "./Switch.vue";
import DocumentationIcon from "./icons/IconDocumentation.vue";
import ToolingIcon from "./icons/IconTooling.vue";
import EcosystemIcon from "./icons/IconEcosystem.vue";
import CommunityIcon from "./icons/IconCommunity.vue";
import SupportIcon from "./icons/IconSupport.vue";
import { storeToRefs } from "pinia";
import { useGuestStore } from "../stores/guest";

const { guest, loading, error } = storeToRefs(useGuestStore());
const { fetchGuest } = useGuestStore();

fetchGuest();
</script>

<template>
  <WelcomeItem>
    <template #icon>
      <DocumentationIcon />
    </template>
    <template #heading>Confermi la tua presenza?</template>
    <Switch
      checkboxId="a"
      v-if="typeof guest.viene !== 'undefined'"
      :initialValue="guest.viene"
      @changeCheck="changePresence($event)"
    />
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <CommunityIcon />
    </template>
    <template #heading>Hai bisogno di una stanza?</template>
    <Switch
      checkboxId="b"
      v-if="typeof guest.stanza !== 'undefined'"
      :initialValue="guest.stanza"
      @changeCheck="changeRoom($event)"
    />
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <SupportIcon />
    </template>
    <template #heading>Vuoi partecipare all'addio nubilato/celibato?</template>
    {{ party_text }}
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <CommunityIcon />
    </template>
    <template #heading>Note</template>
    {{ note_text }}
  </WelcomeItem>
</template>
<script>
export default {
  data() {
    return {
      note_text: "Vuoi farci sapere qualcosa?",
      party_text: "Contatta il testimone",
    };
  },
  computed: {},
  created() {
    const guest_id = this.$route.query.id;
  },
  methods: {
    boolToIt(bool) {
      if (bool) {
        return "sì";
      } else {
        return "no";
      }
    },
    changePresence(presence) {
      const { updateGuest } = useGuestStore();
      console.log("Presente:" + presence);
      updateGuest({ viene: this.boolToIt(presence) });
    },
    changeRoom(room) {
      const { updateGuest } = useGuestStore();
      console.log("Room:" + room);
      updateGuest({ stanza: this.boolToIt(room) });
    },
  },
};
</script>
