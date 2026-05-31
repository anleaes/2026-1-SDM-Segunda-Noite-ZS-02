<template>
  <div style="padding: 20px; font-family: sans-serif;">
    <h2>🩺 Corpo Clínico (Médicos)</h2>
    <p>Gerenciamento de profissionais, especialidades médicas e status de atividade.</p>

    <div v-if="loading" style="color: #3498db; font-weight: bold; margin: 20px 0;">
      🔄 Carregando corpo clínico do servidor...
    </div>

    <div v-else-if="error" style="color: #e74c3c; background-color: #fce4e4; padding: 15px; border-radius: 4px; margin: 20px 0;">
      ⚠️ {{ error }}
    </div>

    <table v-else border="1" cellpadding="10" style="width: 100%; border-collapse: collapse; background-color: white; margin-top: 20px; text-align: left;">
      <thead style="background-color: #f2f2f2;">
        <tr>
          <th>ID</th>
          <th>Nome Completo</th>
          <th>CRM</th>
          <th>Especialidade</th>
          <th>Matrícula</th>
          <th>Cargo</th>
          <th>Data de Contratação</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="medico in medicos" :key="medico.id">
          <td>{{ medico.id }}</td>
          <td style="font-weight: bold; color: #2c3e50;">
            Dr(a). {{ medico.nome || 'Médico' }} {{ medico.sobrenome || '' }}
          </td>
          <td>{{ medico.crm }}</td>
          <td>{{ medico.especialidade }}</td>
          <td>{{ medico.matricula }}</td>
          <td>{{ medico.cargo }}</td>
          <td>{{ formatarData(medico.data_contratacao) }}</td>
          <td>
            <span :style="medico.esta_ativo ? 'color: #27ae60; font-weight: bold;' : 'color: #7f8c8d;'">
              {{ medico.esta_ativo ? '🟢 Ativo' : '🔴 Inativo' }}
            </span>
          </td>
        </tr>
        <tr v-if="medicos.length === 0">
          <td colspan="8" style="text-align: center; color: gray;">Nenhum médico cadastrado no sistema.</td>
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
      medicos: [],
      loading: true,
      error: null
    };
  },
  mounted() {
    this.buscarMedicos();
  },
  methods: {
    async buscarMedicos() {
      try {
        this.loading = true;
        const response = await axios.get('http://localhost:8000/medico/api/');
        this.medicos = response.data;
        this.error = null;
      } catch (err) {
        console.error("Erro ao buscar médicos:", err);
        this.error = "Não foi possível carregar os dados dos médicos. Certifique-se de que a rota http://localhost:8000/medico/api/ está ativa.";
      } finally {
        this.loading = false;
      }
    },
    formatarData(dataString) {
      if (!dataString) return '-';
      const [ano, mes, dia] = dataString.split('-');
      return `${dia}/${mes}/${ano}`;
    }
  }
};
</script>