<template>
  <header>
    <div class="header-content">
      <h2 class="app-title">Percevoir</h2>
      <nav>
        <ul class="nav-list">
          <li>
            <span class="welcome-message">
              Bienvenue, {{ $route.params.id }}
            </span>
          </li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<script>
export default {
  name: "Header",
};
</script>

<style scoped>
.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background: linear-gradient(to right, #1e88e5, #1565c0);
  color: #fff;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);
}

.app-title {
  font-size: 24px;
  font-weight: bold;
  margin: 0;
}

.welcome-message {
  font-size: 20px;
  font-weight: bold;
  color: #020e1d;
  text-transform: capitalize;
}

nav ul {
  list-style: none;
  padding: 0;
  display: flex;
}

nav li {
  margin-right: 20px;
}

a {
  color: #fff;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
</style>
