from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'atestado'

router = routers.SimpleRouter()
router.register('api', views.AtestadoViewSet, basename='atestado')

urlpatterns = [
    path('', include(router.urls)),
    path('add/', views.add_atestado, name='add_atestado'),
    path('list/', views.list_atestado, name='list_atestado'),
    path('edit/<int:id_atestado>/', views.edit_atestado, name='edit_atestado'),
    path('delete/<int:id_atestado>/', views.delete_atestado, name='delete_atestado'),
    path('buscar/', views.search_atestado, name='search_atestado'),
]
