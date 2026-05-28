from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'medicamento'

router = routers.SimpleRouter()
router.register('api', views.MedicamentoViewSet, basename='medicamento')

urlpatterns = [
    path('', include(router.urls)),
    path('list/', views.list_medicamento, name='list_medicamento'),
    path('add/', views.add_medicamento, name='add_medicamento'),
    path('edit/<int:id_medicamento>/', views.edit_medicamento, name='edit_medicamento'),
    path('delete/<int:id_medicamento>/', views.delete_medicamento, name='delete_medicamento'),
    path('buscar/', views.search_medicamento, name='search_medicamento'),
]