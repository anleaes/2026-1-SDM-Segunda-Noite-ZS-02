<template>
  <div id="app-layout" style="display: flex; font-family: sans-serif; min-height: 100vh; margin: 0;">
    <!-- Barra Lateral de Navegação -->
    <nav style="width: 260px; background-color: #2c3e50; color: white; padding: 20px; box-sizing: border-box; display: flex; flex-direction: column; gap: 5px;">
      <h2 style="color: #42b983; margin-bottom: 20px; font-size: 22px; text-align: center;">🏥 Prontuário App</h2>
      
      <div style="display: flex; flex-direction: column; gap: 10px; overflow-y: auto; flex: 1;">
        <RouterLink to="/pacientes" class="nav-link">👥 Pacientes</RouterLink>
        <RouterLink to="/medicos" class="nav-link">🩺 Médicos</RouterLink>
        <RouterLink to="/anamneses" class="nav-link">📝 Anamneses</RouterLink>
        <RouterLink to="/consultas" class="nav-link">📅 Consultas</RouterLink>
        <RouterLink to="/cids" class="nav-link">📋 Tabela CIDs</RouterLink>
        <RouterLink to="/atestados" class="nav-link">📄 Atestados Médicos</RouterLink>
        <RouterLink to="/medicamentos" class="nav-link">📦 Medicamentos</RouterLink>
        <RouterLink to="/receitas" class="nav-link">💊 Receitas</RouterLink>
        <RouterLink to="/exames-solicitados" class="nav-link">🧪 Exames Solicitados</RouterLink>
        <RouterLink to="/resultados-exames" class="nav-link">📊 Resultados de Exames</RouterLink>
      </div>
    </nav>

    <!-- Conteúdo Principal Dinâmico -->
    <main style="flex: 1; padding: 40px; background-color: #f8f9fa; box-sizing: border-box; overflow-y: auto;">
      <RouterView />
    </main>
  </div>
</template>

<style scoped>
.nav-link {
  color: #ecf0f1;
  text-decoration: none;
  padding: 8px 12px;
  border-radius: 4px;
  transition: 0.2s;
  font-weight: 500;
  font-size: 14px;
}
.nav-link:hover {
  background-color: #34495e;
  color: #42b983;
}
.router-link-active {
  background-color: #42b983 !important;
  color: white !important;
}
</style>