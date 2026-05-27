from django.urls import path, include
from . import views
from rest_framework import routers  # <-- É essa linha aqui que estava faltando!

app_name = 'receitamedicamento'

router = routers.SimpleRouter()
router.register('api', views.ReceitaMedicamentoViewSet, basename='receitamedicamento-api')

urlpatterns = [
   
    path('', include(router.urls)),
    
   
    path('list/', views.list_receitamedicamento, name='list_receitamedicamento'),
]