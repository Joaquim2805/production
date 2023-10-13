<template>
  <div class="login-page">
    <div class="login-container">
      <h2 class="animate__animated animate__bounce">Connexion</h2>
      <form
        @submit.prevent="login"
        class="login-form animate__animated animate__fadeIn"
      >
        <div class="form-group animate__animated animate__slideInLeft">
          <input
            type="text"
            v-model="id"
            placeholder="ID de l'utilisateur"
            required
          />
        </div>
        <div class="form-group animate__animated animate__slideInRight">
          <input
            type="password"
            v-model="password"
            placeholder="Mot de passe"
            required
          />
        </div>
        <button type="submit" class="animate__animated animate__pulse">
          Se connecter
        </button>
      </form>
      <p>
        Pas encore de compte ?
        <router-link to="/register">Inscrivez-vous ici</router-link>
      </p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      id: "",
      password: "",
      data: "",
    };
  },
  methods: {
    login() {
      // Récupérer l'ID et le mot de passe depuis les données du composant
      const id = this.id;
      const password = this.password;

      // Faire une requête Axios GET pour envoyer les données au serveur
      axios
        .get(`http://127.0.0.1:8001/login?id=${id}&password=${password}`)
        .then((response) => {
          if (response.data && response.data.access_token) {
            this.data = response.data;

            // Gérer la réponse du serveur ici
            this.message = response.data; // Par exemple, stocker le message de réponse dans la variable 'message'
            console.log(this.message.access_token);
            this.$router.push({ name: "header_user", params: { id: id } });
          }
        })
        .catch((error) => {
          // Gérer les erreurs ici
          console.error("Erreur lors de la requête :", error);
        });
    },
  },
};
</script>

<style scoped>
.login-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(to right, #3494e6, #ec6ead);
}
.login-container {
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  padding: 20px;
  text-align: center;
  animation: fadeIn 0.5s;
}

h2 {
  color: #333;
  margin: 0 0 20px;
}

.login-form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.form-group {
  margin: 10px 0;
  width: 100%;
}

input {
  padding: 10px;
  border: none;
  border-bottom: 2px solid #007bff;
  outline: none;
  border-radius: 5px;
  width: 100%;
}

button {
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px 0;
  cursor: pointer;
  width: 100%;
  margin-top: 20px;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
</style>
