<template>
  <div style="padding: 20px; font-family: sans-serif;">
    <h2>👥 Gerenciamento de Pacientes</h2>
    <p>Dados consumidos em tempo real do sistema de prontuários.</p>

    <div v-if="loading" style="color: #3498db; font-weight: bold; margin: 20px 0;">
      🔄 Carregando pacientes do servidor...
    </div>

    <div v-else-if="error" style="color: #e74c3c; background-color: #fce4e4; padding: 15px; border-radius: 4px; margin: 20px 0;">
      ⚠️ {{ error }}
    </div>

    <table v-else border="1" cellpadding="10" style="width: 100%; border-collapse: collapse; background-color: white; margin-top: 20px; text-align: left;">
      <thead style="background-color: #f2f2f2;">
        <tr>
          <th>ID</th>
          <th>Nome</th>
          <th>CPF</th>
          <th>Data de Nascimento</th>
          <th>Peso (kg)</th>
          <th>Altura (m)</th>
          <th>Endereço completo</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="paciente in pacientes" :key="paciente.id">
          <td>{{ paciente.id }}</td>
          <td>{{ paciente.nome || 'Não informado' }}</td>
          <td>{{ paciente.cpf || 'Não informado' }}</td>
          <td>{{ formatarData(paciente.data_nascimento) }}</td>
          <td>{{ paciente.peso }} kg</td>
          <td>{{ paciente.altura }} m</td>
          <td>{{ paciente.endereco }}</td>
        </tr>
        <tr v-if="pacientes.length === 0">
          <td colspan="7" style="text-align: center; color: gray;">Nenhum paciente cadastrado no banco de dados.</td>
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
      pacientes: [],
      loading: true,
      error: null
    };
  },
  mounted() {
    this.buscarPacientes();
  },
  methods: {
    async buscarPacientes() {
      try {
        this.loading = true;
        const response = await axios.get('http://localhost:8000/paciente/api/');
        this.pacientes = response.data;
        this.error = null;
      } catch (err) {
        console.error("Erro ao buscar pacientes:", err);
        this.error = "Não foi possível carregar os dados. Verifique se o Django está ativo em http://localhost:8000/paciente/api/";
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