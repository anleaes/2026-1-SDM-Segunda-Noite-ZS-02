from django.urls import path

app_name = 'receitamedicamento'

router = routers.SimpleRouter()
#Registra APENAS a rota da API (/receitaMedicamento/api/)
router.register('api', views.ReceitaMedicamentoViewSet, basename='receitamedicamento-api')

urlpatterns = [
    path('', include(router.urls)),
]