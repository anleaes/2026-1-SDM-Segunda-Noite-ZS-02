from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'exameSolicitado'

router = routers.SimpleRouter()
router.register('api', views.ExameSolicitadoViewSet, basename='exameSolicitado')

urlpatterns = [
    path('', include(router.urls)),
    path('list/', views.list_exame_solicitado, name='list_exame_solicitado'),
    path('add/', views.add_exame_solicitado, name='add_exame_solicitado'),
    path('edit/<int:id_exame_solicitado>/', views.edit_exame_solicitado, name='edit_exame_solicitado'),
    path('delete/<int:id_exame_solicitado>/', views.delete_exame_solicitado, name='delete_exame_solicitado'),
    path('buscar/', views.search_exame_solicitado, name='search_exame_solicitado'),
]