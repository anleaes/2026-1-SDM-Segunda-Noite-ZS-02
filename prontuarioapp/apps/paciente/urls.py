from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'paciente'

router = routers.SimpleRouter()
router.register('api', views.PacienteViewSet, basename='paciente')

urlpatterns = [
    path('', include(router.urls)),
    path('list/', views.list_paciente, name='list_paciente'),
    path('add/', views.add_paciente, name='add_paciente'),
    path('edit/<int:id_paciente>/', views.edit_paciente, name='edit_paciente'),
    path('delete/<int:id_paciente>/', views.delete_paciente, name='delete_paciente'),
]