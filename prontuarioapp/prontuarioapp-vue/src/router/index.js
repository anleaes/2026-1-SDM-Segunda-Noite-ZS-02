import { createRouter, createWebHistory } from 'vue-router'
import PacienteView from '../views/PacienteView.vue'
import MedicoView from '../views/MedicoView.vue'
import AnamneseView from '../views/AnamneseView.vue'
import ConsultaView from '../views/ConsultaView.vue'
import CidView from '../views/CidView.vue'
import AtestadoView from '../views/AtestadoView.vue'
import MedicamentoView from '../views/MedicamentoView.vue'
import ReceitaView from '../views/ReceitaView.vue'
import ExameSolicitadoView from '../views/ExameSolicitadoView.vue'
import ResultadoExameView from '../views/ResultadoExameView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', redirect: '/cids' },
    { path: '/pacientes', name: 'pacientes', component: PacienteView },
    { path: '/medicos', name: 'medicos', component: MedicoView },
    { path: '/anamneses', name: 'anamneses', component: AnamneseView },
    { path: '/consultas', name: 'consultas', component: ConsultaView },
    { path: '/cids', name: 'cids', component: CidView },
    { path: '/atestados', name: 'atestados', component: AtestadoView },
    { path: '/medicamentos', name: 'medicamentos', component: MedicamentoView },
    { path: '/receitas', name: 'receitas', component: ReceitaView },
    { path: '/exames-solicitados', name: 'examesSolicitados', component: ExameSolicitadoView },
    { path: '/resultados-exames', name: 'resultadosExames', component: ResultadoExameView },
  ],
})

export default router