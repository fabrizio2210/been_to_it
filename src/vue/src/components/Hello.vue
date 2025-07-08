<script setup>
import { onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useEventStore } from "../stores/event";
import { useIdStore } from "../stores/id";
import { useRoute, useRouter } from "vue-router";

const { evento, loading, error } = storeToRefs(useEventStore());
const { setId } = useIdStore();
const { fetchEvent } = useEventStore();

onMounted(async () => {
  const route = useRoute();
  const router = useRouter();
  const { setId } = useIdStore();
  await router.isReady();
  if (typeof route.query.id !== "undefined") {
    setId(route.query.id);
  }
  if (typeof route.params.id !== "undefined") {
    setId(route.params.id);
  }
  fetchEvent();
});
</script>

<template>
  <div id="invito">
    <img id="bg_img" src="/resources/invito_bg.jpg" alt="background image" />
    <p
      v-if="evento"
      id="par1"
      style="top: 65%; left: 50%; transform: translateX(-50%, 0%)"
      class="ft16"
      :class="[loading ? 'blur' : 'noblur']"
      v-html="evento.descrizione_par1"
    />
    <p
      v-if="evento"
      d="par2"
      style="top: 73%; left: 50%; transform: translate(-50%, 0%)"
      class="ft11"
      :class="[loading ? 'blur' : 'noblur']"
      v-html="evento.descrizione_par2"
    />
    <p
      v-if="evento"
      d="par3"
      style="top: 56%; left: 50%; transform: translateX(-50%, 0%)"
      class="ft13"
      :class="[loading ? 'blur' : 'noblur']"
      v-html="evento.descrizione_par3"
    />
  </div>
</template>

<style scoped>
@font-face {
  font-family: "eyesome-script";
  src: local("eyesome-script"),
    url(@/assets/eyesome-script.otf) format("opentype");
}
@font-face {
  font-family: "glacial-indifference-regular";
  src: local("glacial-indifference-regular"),
    url(@/assets/GlacialIndifference-Regular.ttf) format("truetype");
}
@font-face {
  font-family: "glacial-indifference-bold";
  src: local("glacial-indifference-bold"),
    url(@/assets/GlacialIndifference-Bold.ttf) format("truetype");
}

.blur {
  filter: blur(9px);
}

.noblur {
  filter: blur(0px);
}

#bg_img {
  width: 100%;
}
#invito {
  position: relative;
  width: 100%;
}
p {
  margin: 0;
  padding: 0;
  text-align: center;
  white-space: nowrap;
  position: absolute;
  line-height: 1.15;
}
.ft11 {
  font-size: 3.2vw;
  font-family: glacial-indifference-regular;
  color: #535959;
  letter-spacing: 0.05em;
  transition: filter 0.2s;
}
.ft13 {
  font-size: 3.4vw;
  font-family: eyesome-script;
  color: #535959;
  letter-spacing: 0.06em;
  transition: filter 0.2s;
}
.ft16 {
  font-size: 3.3vw;
  font-family: glacial-indifference-regular;
  color: #535959;
  letter-spacing: 0.05em;
  transition: filter 0.2s;
}
@media (min-width: 1024px) {
  #invito {
    width: 1024px;
  }
  .ft11 {
    font-size: 33px;
  }
  .ft13 {
    font-size: 36px;
  }
  .ft16 {
    font-size: 34px;
  }
}
</style>
