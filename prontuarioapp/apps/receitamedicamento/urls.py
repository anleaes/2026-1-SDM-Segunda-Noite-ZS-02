from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'receitamedicamento'

router = routers.SimpleRouter()
router.register('', views.ReceitaMedicamentoViewSet, basename='receitamedicamento')

urlpatterns = [
    path('', include(router.urls)),
]