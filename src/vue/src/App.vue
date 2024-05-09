<script setup>
import { RouterLink, RouterView } from "vue-router";
import Hello from "./components/Hello.vue";

import { useEventStore } from "./stores/event";
import { storeToRefs } from "pinia";
const { evento } = storeToRefs(useEventStore());
</script>

<template>
  <div>
    <Hello />
    <nav>
      <RouterLink to="/">Tu</RouterLink>
      <RouterLink to="/guests">Altri invitati</RouterLink>
      <RouterLink
        v-if="
          typeof evento !== 'undefined' && evento !== null && evento.menu !== ''
        "
        to="/menu"
        >Menù</RouterLink
      >
      <RouterLink
        v-if="
          typeof evento !== 'undefined' &&
          evento !== null &&
          evento.timeline !== ''
        "
        to="/timeline"
        >Timeline</RouterLink
      >
      <RouterLink to="/photobook">Foto</RouterLink>
    </nav>
    <RouterView />
  </div>
</template>
<script>
export default {
  computed: {
    message() {
      return (
        "Ciao " + this.$route.query.id + " sei invitato al nostro matrimonio"
      );
    },
  },
};
</script>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 1rem;
  /* margin-bottom: 2rem; */
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
