<template>
  <div style="padding: 20px; font-family: sans-serif;">
    <h2>📊 Resultados de Exames</h2>
    <p>Laudos técnicos, valores de referência e conclusões diagnósticas anexadas aos exames.</p>

    <div v-if="loading" style="color: #3498db; font-weight: bold; margin: 20px 0;">
      🔄 Carregando laudos e resultados do servidor...
    </div>

    <div v-else-if="error" style="color: #e74c3c; background-color: #fce4e4; padding: 15px; border-radius: 4px; margin: 20px 0;">
      ⚠️ {{ error }}
    </div>

    <table v-else border="1" cellpadding="10" style="width: 100%; border-collapse: collapse; background-color: white; margin-top: 20px; text-align: left;">
      <thead style="background-color: #f2f2f2;">
        <tr>
          <th>ID</th>
          <th>ID do Exame Solicitado</th>
          <th>Data do Resultado</th>
          <th>Valor Medido</th>
          <th>Conclusões / Laudo</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="resultado in resultados" :key="resultado.id">
          <td>{{ resultado.id }}</td>
          <td>#{{ resultado.exame_solicitado }}</td>
          <td>formatarData(resultado.data_resultado)</td>
          <td style="font-weight: bold; color: #2c3e50;">
            {{ resultado.valor }} <span style="font-size: 12px; color: #7f8c8d;">{{ resultado.unidade_medida }}</span>
          </td>
          <td style="white-space: pre-line;">{{ resultado.conclusoes }}</td>
        </tr>
        <tr v-if="resultados.length === 0">
          <td colspan="5" style="text-align: center; color: gray;">Nenhum resultado de exame lançado no banco de dados.</td>
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
      resultados: [],
      loading: true,
      error: null
    };
  },
  mounted() {
    this.buscarResultados();
  },
  methods: {
    async buscarResultados() {
      try {
        this.loading = true;
        const response = await axios.get('http://localhost:8000/resultadoexame/api/');
        this.resultados = response.data;
        this.error = null;
      } catch (err) {
        console.error("Erro ao buscar resultados de exames:", err);
        this.error = "Não foi possível carregar os resultados de exames. Verifique se a rota está ativa.";
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