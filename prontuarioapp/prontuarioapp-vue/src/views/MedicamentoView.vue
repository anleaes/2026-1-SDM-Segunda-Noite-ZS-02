<template>
  <div style="padding: 20px; font-family: sans-serif;">
    <h2>📦 Catálogo de Medicamentos</h2>
    <p>Consulta de fármacos registrados, princípios ativos e restrições de controle.</p>

    <!-- Mensagem de Carregamento -->
    <div v-if="loading" style="color: #3498db; font-weight: bold; margin: 20px 0;">
      🔄 Carregando catálogo de medicamentos...
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
          <th>Nome de Referência</th>
          <th>Princípio Ativo</th>
          <th>Categoria</th>
          <th>É Controlado?</th>
          <th>Tem Genérico?</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="medicamento in medicamentos" :key="medicamento.id">
          <td>{{ medicamento.id }}</td>
          <td style="font-weight: bold; color: #2c3e50;">{{ medicamento.nome_referencia }}</td>
          <td>{{ medicamento.principio_ativo }}</td>
          <td>{{ medicamento.categoria }}</td>
          <!-- Validação visual se é tarja preta / controlado -->
          <td>
            <span :style="medicamento.e_controlado ? 'color: #c0392b; font-weight: bold; background-color: #fadbd8; padding: 2px 6px; border-radius: 4px;' : 'color: #27ae60;'">
              {{ medicamento.e_controlado ? '⚠️ Sim (Controlado)' : 'Não' }}
            </span>
          </td>
          <!-- Validação se possui genérico -->
          <td>
            <span :style="medicamento.tem_generico ? 'color: #27ae60; font-weight: bold;' : 'color: #7f8c8d;'">
              {{ medicamento.tem_generico ? '🟢 Sim' : '❌ Não' }}
            </span>
          </td>
        </tr>
        <tr v-if="medicamentos.length === 0">
          <td colspan="6" style="text-align: center; color: gray;">Nenhum medicamento cadastrado no catálogo.</td>
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
      medicamentos: [],
      loading: true,
      error: null
    };
  },
  mounted() {
    this.buscarMedicamentos();
  },
  methods: {
    async buscarMedicamentos() {
      try {
        this.loading = true;
        const response = await axios.get('http://localhost:8000/medicamento/api/');
        this.medicamentos = response.data;
        this.error = null;
      } catch (err) {
        console.error("Erro ao buscar medicamentos:", err);
        this.error = "Não foi possível carregar o catálogo de medicamentos. Verifique se o servidor Django está ativo em http://localhost:8000/medicamento/api/";
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>