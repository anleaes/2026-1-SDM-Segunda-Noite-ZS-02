<template>
  <div style="padding: 20px; font-family: sans-serif;">
    <h2>🧪 Exames Solicitados</h2>
    <p>Pedidos de exames laboratoriais e de imagem gerados durante as consultas médicas.</p>

    <!-- Mensagem de Carregamento -->
    <div v-if="loading" style="color: #3498db; font-weight: bold; margin: 20px 0;">
      🔄 Carregando pedidos de exames do servidor...
    </div>

    <!-- Mensagem de Erro -->
    <div v-else-if="error" style="color: #e74c3c; background-color: #fce4e4; padding: 15px; border-radius: 4px; margin: 20px 0;">
      ⚠️ {{ error }}
    </div>

    <!-- Tabela de Dados Reais -->
    <table v-else border="1" cellpadding="10" style="width: 100%; border-collapse: collapse; background-color: white; margin-top: 20px; text-align: left;">
      <thead style="background-color: #f2f2f2;">
        <tr>
          <th>ID</th>
          <th>Nome do Exame</th>
          <th>ID da Consulta</th>
          <th>Exige Jejum?</th>
          <th>Instruções de Preparo</th>
          <th>Descrição / Objetivo</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="exame in exames" :key="exame.id">
          <td>{{ exame.id }}</td>
          <td style="font-weight: bold; color: #2c3e50;">{{ exame.nome_exame }}</td>
          <td>#{{ exame.consulta }}</td>
          <!-- Validação visual do campo booleano de Jejum -->
          <td>
            <span :style="exame.exige_jejum ? 'color: #c0392b; font-weight: bold;' : 'color: #27ae60;'">
              {{ exame.exige_jejum ? '🔴 Sim' : '🟢 Não' }}
            </span>
          </td>
          <td>{{ exame.preparo || 'Nenhum preparo especial necessário.' }}</td>
          <td>{{ exame.descricao }}</td>
        </tr>
        <tr v-if="exames.length === 0">
          <td colspan="6" style="text-align: center; color: gray;">Nenhum exame solicitado no banco de dados.</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      exames: [],
      loading: true,
      error: null
    };
  },
  mounted() {
    this.buscarExames();
  },
  methods: {
    async buscarExames() {
      try {
        this.loading = true;
        // URL ajustada de acordo com a arquitetura do grupo
        const response = await axios.get('http://localhost:8000/examesolicitado/api/');
        this.exames = response.data;
        this.error = null;
      } catch (err) {
        console.error("Erro ao buscar exames solicitados:", err);
        this.error = "Não foi possível carregar os exames solicitados. Verifique se a rota http://localhost:8000/examesolicitado/api/ está correta.";
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>