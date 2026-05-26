from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'receitamedicamento'

router = routers.DefaultRouter()
router.register('api', views.ReceitaMedicamentoViewSet, basename='api-receitamedicamento')

urlpatterns = [
    path('', include(router.urls)),
    
    path('list/', views.list_receitamedicamento, name='list_receitamedicamento'),
    path('add/', views.add_receitamedicamento, name='add_receitamedicamento'),
    path('edit/<int:id_receitamedicamento>/', views.edit_receitamedicamento, name='edit_receitamedicamento'),
    path('delet/<int:id_receitamedicamento>/', views.delete_receitamedicamento, name='delete_receitamedicamento'),
]