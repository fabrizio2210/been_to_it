import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/id/:id",
      component: HomeView,
    },
    {
      path: "/guests",
      name: "guests",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/GuestsView.vue"),
    },
    {
      path: "/menu",
      name: "menu",
      component: () => import("../views/MenuView.vue"),
    },
    {
      path: "/timeline",
      name: "timeline",
      component: () => import("../views/TimelineView.vue"),
    },
    {
      path: "/photobook",
      name: "photobook",
      component: () => import("../views/PhotobookView.vue"),
    },
  ],
});

export default router;
