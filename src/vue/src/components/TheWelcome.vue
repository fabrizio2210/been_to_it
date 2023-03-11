<script setup>
import WelcomeItem from "./WelcomeItem.vue";
import DocumentationIcon from "./icons/IconDocumentation.vue";
import ToolingIcon from "./icons/IconTooling.vue";
import EcosystemIcon from "./icons/IconEcosystem.vue";
import CommunityIcon from "./icons/IconCommunity.vue";
import SupportIcon from "./icons/IconSupport.vue";
</script>

<template>
  <WelcomeItem>
    <template #icon>
      <DocumentationIcon />
    </template>
    <template #heading>Dove</template>
    {{ where_text }}
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <ToolingIcon />
    </template>
    <template #heading>Quando</template>
    {{ date_text }}
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <EcosystemIcon />
    </template>
    <template #heading>Confermi la tua presenza?</template>
    Sì, No
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <CommunityIcon />
    </template>
    <template #heading>Hai bisogno di una stanza?</template>
    Sì, No
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <SupportIcon />
    </template>
    <template #heading>Vuoi partecipare all'addio nubilato/celibato?</template>
    {{ party_text }}
  </WelcomeItem>
</template>
<script>
export default {
  data() {
    return {
      date_text: "venerdì 22 settembre",
      where_text: "Pinzoner Keller",
      party_text: "Contatta il testimone",
    };
  },
  created() {
    const guest_id = this.$route.query.id;
  },
};
</script>
