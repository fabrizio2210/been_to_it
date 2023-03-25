<script setup>
import WelcomeItem from "./WelcomeItem.vue";
import Switch from "./Switch.vue";
import Notes from "./Notes.vue";
import DocumentationIcon from "./icons/IconDocumentation.vue";
import ToolingIcon from "./icons/IconTooling.vue";
import EcosystemIcon from "./icons/IconEcosystem.vue";
import CommunityIcon from "./icons/IconCommunity.vue";
import SupportIcon from "./icons/IconSupport.vue";
import GiftIcon from "./icons/IconGift.vue";
import DressIcon from "./icons/IconDress.vue";
import { storeToRefs } from "pinia";
import { useGuestStore } from "../stores/guest";
import { useEventStore } from "../stores/event";

const { guest, loading, error } = storeToRefs(useGuestStore());
const { evento } = storeToRefs(useEventStore());
const { fetchGuest } = useGuestStore();

fetchGuest();
</script>

<template>
  <template v-if="typeof guest !== 'undefined' && Object.keys(guest) != 0">
    <div>
      <h2>Ciao {{ guest.nome }}</h2>
    </div>
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

    <div
      class="optional-section"
      v-if="typeof guest.viene !== 'undefined' && itToBool(guest.viene)"
    >
      <WelcomeItem>
        <template #icon>
          <CommunityIcon />
        </template>
        <template #heading
          >In caso fosse disponibile, avresti bisogno di una stanza?</template
        >
        <Switch
          checkboxId="b"
          v-if="typeof guest.stanza !== 'undefined'"
          :initialValue="guest.stanza"
          @changeCheck="changeRoom($event)"
        />
      </WelcomeItem>

      <WelcomeItem v-if="evento !== null && typeof evento.addio !== 'undefined'">
        <template #icon>
          <SupportIcon />
        </template>
        <template #heading
          >Vuoi partecipare all'addio nubilato/celibato?</template
        >
        {{ evento.addio }}
      </WelcomeItem>

      <WelcomeItem>
        <template #icon>
          <DressIcon />
        </template>
        <template #heading>Dress code</template>
        Chiedi ad Ervisa.
      </WelcomeItem>

      <WelcomeItem v-if="evento !== null && typeof evento.regalo !== 'undefined'">
        <template #icon>
          <GiftIcon />
        </template>
        <template #heading>Regalo</template>
        {{ evento.regalo }}
      </WelcomeItem>
    </div>

    <WelcomeItem>
      <template #icon>
        <CommunityIcon />
      </template>
      <template #heading>Note</template>
      {{ note_text }}
      <Notes
        notesId="notes"
        v-if="typeof guest.note !== 'undefined'"
        :initialValue="guest.note"
        @changeText="changeNote($event)"
      />
    </WelcomeItem>
  </template>
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
    itToBool(str) {
      if (str == "sì" || str == "si" || str == "true") {
        return true;
      } else {
        return false;
      }
    },
    changePresence(presence) {
      const { updateGuest } = useGuestStore();
      updateGuest({ viene: this.boolToIt(presence) });
    },
    changeRoom(room) {
      const { updateGuest } = useGuestStore();
      updateGuest({ stanza: this.boolToIt(room) });
    },
    changeNote(note) {
      const { updateGuest } = useGuestStore();
      console.log(note);
      updateGuest({ note: note });
    },
  },
};
</script>
<style scoped>
.optional-section {
  border-left: 1px solid var(--color-border);
}
</style>
