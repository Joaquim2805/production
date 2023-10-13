<template>
  <div class="registration-page">
    <div class="registration-container">
      <h2>Inscription</h2>
      <form @submit.prevent="register" class="registration-form">
        <div class="form-group">
          <input
            type="text"
            v-model="id"
            placeholder="ID de l'utilisateur"
            required
          />
        </div>
        <div class="form-group">
          <input
            type="password"
            v-model="password"
            placeholder="Mot de passe"
            required
          />
        </div>
        <div class="form-group">
          <input
            type="password"
            v-model="confirmPassword"
            placeholder="Confirmer le mot de passe"
            required
          />
        </div>
        <button type="submit" class="submit-button">S'inscrire</button>
      </form>
      <div v-if="error" class="error-message">{{ error }}</div>
      <p>
        Vous avez déjà un compte ?
        <router-link to="/login">Connectez-vous ici</router-link>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      id: "",
      password: "",
      confirmPassword: "",
      error: null,
    };
  },
  methods: {
    register() {
      if (this.password !== this.confirmPassword) {
        this.error = "Les mots de passe ne correspondent pas.";
      } else {
        // Ajoutez ici la logique d'enregistrement (simulée ici par une animation)
        this.animateRegistration();
        this.error = null;
        this.$router.push("/login");
      }
    },
    animateRegistration() {
      // Ajoutez ici des animations de chargement ou de succès
    },
  },
};
</script>

<style scoped>
.registration-page {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: linear-gradient(135deg, #b4afdb, #6e66da);
}

.registration-container {
  background: rgba(255, 255, 255, 0.8);
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  width: 400px; /* Augmentation de la taille du cadre */
}

h2 {
  text-align: center;
  color: #333;
}

.registration-form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.form-group {
  margin: 10px 0;
}

input {
  padding: 10px;
  width: 100%;
  border: 1px solid #030a49;
  border-radius: 5px;
  font-size: 16px;
}

.submit-button {
  padding: 10px 20px;
  background-color: #0e84d3;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease; /* Ajout d'une transition pour l'animation CSS */
}

.submit-button:hover {
  background-color: #2071a7;
}

.error-message {
  color: #ff5733;
  text-align: center;
}
</style>
