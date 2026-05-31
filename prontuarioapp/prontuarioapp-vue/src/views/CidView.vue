<template>
  <div class="container" style="font-family: sans-serif; padding: 20px;">
    <h2>📋 Cadastro Geral de CIDs</h2>
    <p>Consulte os códigos do sistema consumidos em tempo real para anexar aos prontuários.</p>

    <div style="margin-bottom: 20px;">
      <input 
        v-model="searchQuery" 
        type="text" 
        placeholder="Digite o código ou a descrição do CID..." 
        style="padding: 8px; width: 300px; border-radius: 4px; border: 1px solid #ccc;"
      />
    </div>

    <div v-if="loading" style="color: #3498db; font-weight: bold; margin: 20px 0;">
      🔄 Carregando tabela de CIDs do servidor...
    </div>

    <div v-else-if="error" style="color: #e74c3c; background-color: #fce4e4; padding: 15px; border-radius: 4px; margin: 20px 0;">
      ⚠️ {{ error }}
    </div>

    <table v-else border="1" cellpadding="10" style="width: 100%; border-collapse: collapse; text-align: left; background-color: white;">
      <thead style="background-color: #f2f2f2;">
        <tr>
          <th>ID</th>
          <th>Código CID</th>
          <th>Descrição Diagnóstica</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="cid in filteredCids" :key="cid.id">
          <td>{{ cid.id }}</td>
          <td style="font-weight: bold; color: #2c3e50;">{{ cid.cod_cid || cid.codigo }}</td>
          <td>{{ cid.descricao }}</td>
        </tr>
        <tr v-if="filteredCids.length === 0">
          <td colspan="3" style="text-align: center; color: gray;">Nenhum CID encontrado para a busca.</td>
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
      searchQuery: '',
      cids: [],
      loading: true,
      error: null
    };
  },
  computed: {
    filteredCids() {
      return this.cids.filter(cid => {
        const query = this.searchQuery.toLowerCase();
        const codigo = (cid.cod_cid || cid.codigo || '').toLowerCase();
        const descricao = (cid.descricao || '').toLowerCase();
        return codigo.includes(query) || descricao.includes(query);
      });
    }
  },
  mounted() {
    this.buscarCids();
  },
  methods: {
    async buscarCids() {
      try {
        this.loading = true;
        const response = await axios.get('http://localhost:8000/cid/api/');
        this.cids = response.data;
        this.error = null;
      } catch (err) {
        console.error("Erro ao buscar CIDs:", err);
        this.error = "Não foi possível carregar a lista de CIDs em http://localhost:8000/cid/api/.";
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>