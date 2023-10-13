import { createRouter, createWebHistory } from "vue-router";
import drag_drop from "../components/drag_drop.vue";
import Header from "../components/Header.vue";
import login from "../Views/Login/login.vue";
import Header_user from "../Views/Header_user/Header_user.vue";
import register from "../Views/Register/Register.vue";

const routes = [
  {
    path: "/",
    component: Header, // Définissez le composant Header comme route par défaut
  },

  {
    path: "/header_user/:id",
    name: "header_user",
    component: Header_user,
    // Définissez le composant Header comme route par défaut
  },
  {
    path: "/file",
    name: "file",
    component: drag_drop,
  },
  {
    path: "/login",
    name: "login",
    component: login,
  },
  {
    path: "/register",
    name: "register",
    component: register,
  },
  // Autres routes...
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
