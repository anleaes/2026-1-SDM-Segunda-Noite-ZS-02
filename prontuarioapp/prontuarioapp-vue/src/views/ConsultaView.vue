<template>
  <div style="padding: 20px; font-family: sans-serif;">
    <h2>📅 Registro de Consultas</h2>
    <p>Gerenciamento de horários, status e prioridade de atendimento clínico.</p>

    <div v-if="loading" style="color: #3498db; font-weight: bold; margin: 20px 0;">
      🔄 Carregando consultas do servidor...
    </div>

    <div v-else-if="error" style="color: #e74c3c; background-color: #fce4e4; padding: 15px; border-radius: 4px; margin: 20px 0;">
      ⚠️ {{ error }}
    </div>

    <table v-else border="1" cellpadding="10" style="width: 100%; border-collapse: collapse; background-color: white; margin-top: 20px; text-align: left;">
      <thead style="background-color: #f2f2f2;">
        <tr>
          <th>ID</th>
          <th>Data e Hora</th>
          <th>Paciente</th>
          <th>Médico</th>
          <th>Prioridade</th>
          <th>Status</th>
          <th>Motivo</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="consulta in consultas" :key="consulta.id">
          <td>{{ consulta.id }}</td>
          <td>{{ formatarDataHora(consulta.data_agendada) }}</td>
          <td>{{ consulta.paciente_nome || consulta.paciente }}</td>
          <td>{{ consulta.medico_nome || consulta.medico }}</td>
          <td><span :style="getEstiloPrioridade(consulta.nivel_prioridade)">{{ traduzirPrioridade(consulta.nivel_prioridade) }}</span></td>
          <td><span :style="getEstiloStatus(consulta.status)">{{ traduzirStatus(consulta.status) }}</span></td>
          <td>{{ consulta.motivo }}</td>
        </tr>
        <tr v-if="consultas.length === 0">
          <td colspan="7" style="text-align: center; color: gray;">Nenhuma consulta agendada no banco de dados.</td>
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
      consultas: [],
      loading: true,
      error: null
    };
  },
  mounted() {
    this.buscarConsultas();
  },
  methods: {
    async buscarConsultas() {
      try {
        this.loading = true;
        const response = await axios.get('http://localhost:8000/consulta/api/');
        this.consultas = response.data;
        this.error = null;
      } catch (err) {
        console.error("Erro ao buscar consultas:", err);
        this.error = "Não foi possível carregar os dados em http://localhost:8000/consulta/api/";
      } finally {
        this.loading = false;
      }
    },
    formatarDataHora(dataString) {
      if (!dataString) return '-';
      const data = new Date(dataString);
      return data.toLocaleString('pt-BR');
    },
    traduzirStatus(status) {
      const opcoes = { 'AG': 'Agendada', 'RE': 'Realizada', 'CA': 'Cancelada' };
      return opcoes[status] || status;
    },
    getEstiloStatus(status) {
      const cores = { 'AG': 'color: #3498db; font-weight: bold;', 'RE': 'color: #2ecc71; font-weight: bold;', 'CA': 'color: #95a5a6; text-decoration: line-through;' };
      return cores[status] || '';
    },
    traduzirPrioridade(nivel) {
      const opcoes = { 'B': 'Baixa', 'N': 'Normal', 'A': 'Alta', 'U': 'Urgência' };
      return opcoes[nivel] || nivel;
    },
    getEstiloPrioridade(nivel) {
      const cores = {
        'B': 'background-color: #ecf0f1; padding: 3px 8px; border-radius: 4px;',
        'N': 'background-color: #dff0d8; color: #3c763d; padding: 3px 8px; border-radius: 4px;',
        'A': 'background-color: #fcf8e3; color: #8a6d3b; padding: 3px 8px; border-radius: 4px; font-weight: bold;',
        'U': 'background-color: #f2dede; color: #a94442; padding: 3px 8px; border-radius: 4px; font-weight: bold;'
      };
      return cores[nivel] || '';
    }
  }
};
</script>