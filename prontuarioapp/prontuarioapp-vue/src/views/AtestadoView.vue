<template>
  <div style="padding: 20px; font-family: sans-serif;">
    <h2>📄 Emissão e Consulta de Atestados Médicos</h2>
    <p>Histórico de justificativas de afastamento e chaves de autenticação do sistema.</p>

    <div v-if="loading" style="color: #3498db; font-weight: bold; margin: 20px 0;">
      🔄 Carregando atestados do servidor...
    </div>

    <div v-else-if="error" style="color: #e74c3c; background-color: #fce4e4; padding: 15px; border-radius: 4px; margin: 20px 0;">
      ⚠️ {{ error }}
    </div>

    <table v-else border="1" cellpadding="10" style="width: 100%; border-collapse: collapse; background-color: white; margin-top: 20px; text-align: left;">
      <thead style="background-color: #f2f2f2;">
        <tr>
          <th>ID</th>
          <th>Código de Autenticação</th>
          <th>Tipo de Atestado</th>
          <th>Início do Afastamento</th>
          <th>Quantidade de Dias</th>
          <th>ID da Consulta</th>
          <th>CID Vinculado</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="atestado in atestados" :key="atestado.id">
          <td>{{ atestado.id }}</td>
          <td style="font-family: monospace; font-weight: bold; color: #2c3e50;">{{ atestado.codigo_autenticacao }}</td>
          <td>{{ traduzirTipo(atestado.tipo_atestado) }}</td>
          <td>{{ formatarData(atestado.data_inicio_afastamento) }}</td>
          <td>{{ atestado.quantidade_dias }} dias</td>
          <td>#{{ atestado.consulta }}</td>
          <td>{{ atestado.cid_codigo || atestado.cid }}</td>
        </tr>
        <tr v-if="atestados.length === 0">
          <td colspan="7" style="text-align: center; color: gray;">Nenhum atestado registrado no banco de dados.</td>
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
      atestados: [],
      loading: true,
      error: null
    };
  },
  mounted() {
    this.buscarAtestados();
  },
  methods: {
    async buscarAtestados() {
      try {
        this.loading = true;
        const response = await axios.get('http://localhost:8000/atestado/api/');
        this.atestados = response.data;
        this.error = null;
      } catch (err) {
        console.error("Erro ao buscar atestados:", err);
        this.error = "Não foi possível carregar os atestados em http://localhost:8000/atestado/api/";
      } finally {
        this.loading = false;
      }
    },
    formatarData(dataString) {
      if (!dataString) return '-';
      const [ano, mes, dia] = dataString.split('-');
      return `${dia}/${mes}/${ano}`;
    },
    traduzirTipo(tipo) {
      const opcoes = { 'MEDICO': 'Médico', 'ODONTO': 'Odontológico', 'OUTRO': 'Outro' };
      return opcoes[tipo] || tipo;
    }
  }
};
</script>