from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'consulta'

router = routers.SimpleRouter()
router.register('', views.ConsultaViewSet, basename='consulta')

urlpatterns = [
    path('api', include(router.urls)),
    path('list/', views.list_medico, name='list_medico'),
    path('add/', views.add_medico, name='add_medico'),
    path('edit/<int:id_medico>/', views.edit_medico, name='edit_medico'),
    path('delete/<int:id_medico>/', views.delete_medico, name='delete_medico'),
]