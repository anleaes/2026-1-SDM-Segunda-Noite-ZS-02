<template>
  <div style="padding: 20px; font-family: sans-serif;">
    <h2>💊 Prescrições e Receitas Médicas</h2>
    <p>Histórico de medicamentos prescritos aos pacientes, prazos de validade e instruções de uso.</p>

    <div v-if="loading" style="color: #3498db; font-weight: bold; margin: 20px 0;">
      🔄 Carregando receitas médicas do servidor...
    </div>

    <div v-else-if="error" style="color: #e74c3c; background-color: #fce4e4; padding: 15px; border-radius: 4px; margin: 20px 0;">
      ⚠️ {{ error }}
    </div>

    <table v-else border="1" cellpadding="10" style="width: 100%; border-collapse: collapse; background-color: white; margin-top: 20px; text-align: left;">
      <thead style="background-color: #f2f2f2;">
        <tr>
          <th>ID</th>
          <th>ID da Consulta</th>
          <th>Data de Emissão</th>
          <th>Validade</th>
          <th>Tipo / Formato</th>
          <th>Instruções Gerais</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="receita in receitas" :key="receita.id">
          <td>{{ receita.id }}</td>
          <td>#{{ receita.consulta }}</td>
          <td>{{ formatarData(receita.data_emissao) }}</td>
          <td :style="verificarValidade(receita.validade)">
            {{ formatarData(receita.validade) }}
          </td>
          <td>
            <span :style="receita.e_digital ? 'color: #2980b9; font-weight: bold;' : 'color: #7f8c8d;'">
              {{ receita.e_digital ? '💻 Digital' : '📄 Física (Impressa)' }}
            </span>
          </td>
          <td>{{ receita.instrucoes || 'Sem instruções gerais registradas.' }}</td>
        </tr>
        <tr v-if="receitas.length === 0">
          <td colspan="6" style="text-align: center; color: gray;">Nenhuma receita emitida no banco de dados.</td>
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
      receitas: [],
      loading: true,
      error: null
    };
  },
  mounted() {
    this.buscarReceitas();
  },
  methods: {
    async buscarReceitas() {
      try {
        this.loading = true;
        const response = await axios.get('http://localhost:8000/receita/api/');
        this.receitas = response.data;
        this.error = null;
      } catch (err) {
        console.error("Erro ao buscar receitas:", err);
        this.error = "Não foi possível carregar as receitas médicas. Verifique se a rota http://localhost:8000/receita/api/ está ativa.";
      } finally {
        this.loading = false;
      }
    },
    formatarData(dataString) {
      if (!dataString) return '-';
      const [ano, mes, dia] = dataString.split('-');
      return `${dia}/${mes}/${ano}`;
    },
    verificarValidade(dataValidade) {
      if (!dataValidade) return '';
      const hoje = new Date();
      hoje.setHours(0,0,0,0);
      const dataVal = new Date(dataValidade);
      
      // Se a receita já estiver vencida em relação ao dia de hoje, destaca em vermelho cor de aviso
      if (dataVal < hoje) {
        return 'color: #c0392b; font-weight: bold; background-color: #f9e7e6;';
      }
      return 'color: #27ae60; font-weight: bold;';
    }
  }
};
</script>