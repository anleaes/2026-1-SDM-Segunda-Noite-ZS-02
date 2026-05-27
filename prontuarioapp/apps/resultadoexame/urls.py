from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'resultadoexame'

router = routers.SimpleRouter()
router.register('api', views.ResultadoExameViewSet, basename='resultadoexame')

urlpatterns = [
    path('', include(router.urls)),

    path('list/', views.list_resultado_exame, name='list_resultado_exame'),
    path('add/', views.add_resultado_exame, name='add_resultado_exame'),
    path('edit/<int:id_resultado>/', views.edit_resultado_exame, name='edit_resultado_exame'),
    path('delete/<int:id_resultado>/', views.delete_resultado_exame, name='delete_resultado_exame'),
]