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
  fetchEvent();
});
</script>

<template>
  <div id="invito">
    <img
      id="bg_img"
      src="@/assets/invito_settembre_bg.jpg"
      alt="background image"
    />
    <p
      v-if="evento"
      id="par1"
      style="top: 52%; left: 50%"
      class="ft16"
      :class="[loading ? 'blur' : 'noblur']"
      v-html="evento.descrizione_par1"
    />
    <p
      v-if="evento"
      d="par2"
      style="top: 66%; left: 64%"
      class="ft11"
      :class="[loading ? 'blur' : 'noblur']"
      v-html="evento.descrizione_par2"
    />
    <p
      v-if="evento"
      d="par3"
      style="top: 79.5%; left: 58.5%"
      class="ft11"
      :class="[loading ? 'blur' : 'noblur']"
      v-html="evento.descrizione_par3"
    />
  </div>
</template>

<style scoped>
@font-face {
  font-family: "glacial-indifference-regular";
  src: local("glacial-indifference-regular"),
    url(@/assets/GlacialIndifference-Regular.ttf) format("truetype");
}
@font-face {
  font-family: "glacial-indifference-bold";
  src: local("glacial-indifference-regular"),
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
  font-size: 9px;
  font-family: glacial-indifference-regular;
  color: #000000;
  transition: filter 0.2s;
}
.ft16 {
  font-size: 10px;
  font-family: glacial-indifference-bold;
  color: #000000;
  transition: filter 0.2s;
}

@media (min-width: 380px) {
  .ft11 {
    font-size: 9.5px;
  }
  .ft16 {
    font-size: 11px;
  }
}
@media (min-width: 400px) {
  .ft11 {
    font-size: 10px;
  }
  .ft16 {
    font-size: 12px;
  }
}
@media (min-width: 500px) {
  .ft11 {
    font-size: 12px;
  }
  .ft16 {
    font-size: 14px;
  }
}
@media (min-width: 595px) {
  .ft11 {
    font-size: 15px;
  }
  .ft16 {
    font-size: 20px;
  }
}
@media (min-width: 760px) {
  .ft11 {
    font-size: 20px;
  }
  .ft16 {
    font-size: 25px;
  }
}
@media (min-width: 830px) {
  .ft11 {
    font-size: 22px;
  }
  .ft16 {
    font-size: 27px;
  }
}
@media (min-width: 915px) {
  .ft11 {
    font-size: 25px;
  }
  .ft16 {
    font-size: 30px;
  }
}
@media (min-width: 1024px) {
  #invito {
    width: 1024px;
  }
  .ft11 {
    font-size: 30px;
  }
  .ft16 {
    font-size: 34px;
  }
}
</style>
