<script setup>
import { onMounted } from "vue";
import WelcomeItem from "./WelcomeItem.vue";
import Switch from "./Switch.vue";
import Notes from "./Notes.vue";
import DocumentationIcon from "./icons/IconDocumentation.vue";
import ToolingIcon from "./icons/IconTooling.vue";
import EcosystemIcon from "./icons/IconEcosystem.vue";
import CommunityIcon from "./icons/IconCommunity.vue";
import SupportIcon from "./icons/IconSupport.vue";
import GiftIcon from "./icons/IconGift.vue";
import EmailIcon from "./icons/IconEmail.vue";
import TransportIcon from "./icons/IconTransport.vue";
import FoodIcon from "./icons/IconFood.vue";
import PartyIcon from "./icons/IconParty.vue";
import DressIcon from "./icons/IconDress.vue";
import { storeToRefs } from "pinia";
import { useGuestStore } from "../stores/guest";
import { useEventStore } from "../stores/event";
import { useRoute, useRouter } from "vue-router";

const { guest, loading, error } = storeToRefs(useGuestStore());
const { evento } = storeToRefs(useEventStore());
const { fetchGuest } = useGuestStore();

onMounted(async () => {
  const route = useRoute();
  const router = useRouter();
  await router.isReady();
  fetchGuest();
});
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
        @changeCheck="changeBool('viene', $event)"
      />
    </WelcomeItem>

    <div
      class="optional-section"
      v-if="typeof guest.viene !== 'undefined' && itToBool(guest.viene)"
    >
      <WelcomeItem>
        <template #icon>
          <FoodIcon />
        </template>
        <template #heading
          >Hai delle alergie od intolleranze alimentari?</template
        >
        <Switch
          checkboxId="b"
          v-if="typeof guest.alergie !== 'undefined'"
          :initialValue="guest.alergie"
          @changeCheck="changeBool('alergie', $event)"
        />
      </WelcomeItem>

      <WelcomeItem>
        <template #icon>
          <TransportIcon />
        </template>
        <template #heading
          >Sarebbe comodo un pulmino da Trento o Mezzocorona?</template
        >
        <Switch
          checkboxId="c"
          v-if="typeof guest.pulmino !== 'undefined'"
          :initialValue="guest.pulmino"
          @changeCheck="changeBool('pulmino', $event)"
        />
      </WelcomeItem>

      <WelcomeItem
        v-if="evento !== null && typeof evento.addio !== 'undefined'"
      >
        <template #icon>
          <PartyIcon />
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
        <div v-html="evento.dresscode"></div>
      </WelcomeItem>

      <WelcomeItem
        v-if="evento !== null && typeof evento.regalo !== 'undefined'"
      >
        <template #icon>
          <GiftIcon />
        </template>
        <template #heading>Regalo</template>
        {{ evento.regalo }}
      </WelcomeItem>

      <WelcomeItem>
        <template #icon>
          <EmailIcon />
        </template>
        <template #heading>Email</template>
        {{ email_text }}
        <Notes
          notesId="email"
          :multiline="false"
          v-if="typeof guest.email !== 'undefined'"
          :initialValue="guest.email"
          @changeText="changeText('email', $event)"
        />
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
        :multiline="true"
        v-if="typeof guest.note !== 'undefined'"
        :initialValue="guest.note"
        @changeText="changeText('note', $event)"
      />
    </WelcomeItem>
  </template>
</template>
<script>
export default {
  data() {
    return {
      note_text: "Vuoi farci sapere qualcosa? Il testo si salva appena finisci di scrivere.",
      email_text:
        "Inserisci la tua email, ti invieremo un invito in calendario più avanti. Il testo si salva appena finisci di scrivere.",
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
    changeBool(field, value) {
      const { updateGuest } = useGuestStore();
      console.log("field:" + field);
      updateGuest({ [field]: this.boolToIt(value) });
    },
    changeText(field, text) {
      const { updateGuest } = useGuestStore();
      console.log("field:" + field);
      updateGuest({ [field]: text });
    },
  },
};
</script>
<style scoped>
@media (min-width: 1024px) {
  .optional-section {
    border-left: 1px solid var(--color-border);
  }
}
</style>
