from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'consulta'

router = routers.SimpleRouter()
router.register('api', views.ConsultaViewSet, basename='consulta')

urlpatterns = [
    path('', include(router.urls)),

    path('list/', views.list_consulta, name='list_consulta'),
    path('add/', views.add_consulta, name='add_consulta'),
    path('edit/<int:id_consulta>/', views.edit_consulta, name='edit_consulta'),
    path('delete/<int:id_consulta>/', views.delete_consulta, name='delete_consulta'),
]