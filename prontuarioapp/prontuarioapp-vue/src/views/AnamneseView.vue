<template>
  <div style="padding: 20px; font-family: sans-serif;">
    <h2>📝 Histórico de Anamneses</h2>
    <p>Histórico de entrevistas iniciais e queixas clínicas dos pacientes.</p>

    <div v-if="loading" style="color: #3498db; font-weight: bold; margin: 20px 0;">
      🔄 Carregando anamneses do servidor...
    </div>

    <div v-else-if="error" style="color: #e74c3c; background-color: #fce4e4; padding: 15px; border-radius: 4px; margin: 20px 0;">
      ⚠️ {{ error }}
    </div>

    <table v-else border="1" cellpadding="10" style="width: 100%; border-collapse: collapse; background-color: white; margin-top: 20px; text-align: left;">
      <thead style="background-color: #f2f2f2;">
        <tr>
          <th>ID</th>
          <th>Data de Criação</th>
          <th>Paciente</th>
          <th>Médico</th>
          <th>Queixa Principal</th>
          <th>Alergias</th>
          <th>Medicamentos em Uso</th>
          <th>Consumo de Álcool</th>
          <th>Fumante</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="anamnese in anamneses" :key="anamnese.id">
          <td>{{ anamnese.id }}</td>
          <td>{{ formatarDataHora(anamnese.data_criacao) }}</td>
          <td>{{ anamnese.paciente_nome || anamnese.paciente }}</td>
          <td>{{ anamnese.medico_nome || anamnese.medico }}</td>
          <td>{{ anamnese.queixa_principal }}</td>
          <td>{{ anamnese.alergias }}</td>
          <td>{{ anamnese.medicamentos }}</td>
          <td>{{ traduzirFrequencia(anamnese.alcool) }}</td>
          <td>{{ traduzirFrequencia(anamnese.fumante) }}</td>
        </tr>
        <tr v-if="anamneses.length === 0">
          <td colspan="9" style="text-align: center; color: gray;">Nenhuma anamnese registrada no banco de dados.</td>
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
      anamneses: [],
      loading: true,
      error: null
    };
  },
  mounted() {
    this.buscarAnamneses();
  },
  methods: {
    async buscarAnamneses() {
      try {
        this.loading = true;
        const response = await axios.get('http://localhost:8000/anamnese/api/');
        this.anamneses = response.data;
        this.error = null;
      } catch (err) {
        console.error("Erro ao buscar anamneses:", err);
        this.error = "Não foi possível carregar as anamneses. Verifique o servidor em http://localhost:8000/anamnese/api/";
      } finally {
        this.loading = false;
      }
    },
    formatarDataHora(dataString) {
      if (!dataString) return '-';
      const data = new Date(dataString);
      return data.toLocaleString('pt-BR');
    },
    traduzirFrequencia(sigla) {
      const opcoes = { 'NAO': 'Não consome', 'EVE': 'Eventual', 'DIA': 'Diário' };
      return opcoes[sigla] || sigla;
    }
  }
};
</script>