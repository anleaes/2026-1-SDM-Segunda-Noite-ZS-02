from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'medico'

router = routers.SimpleRouter()
router.register('api', views.MedicoViewSet, basename='medico')

urlpatterns = [
    path('', include(router.urls)),

    path('list/', views.list_medico, name='list_medico'),
    path('add/', views.add_medico, name='add_medico'),
    path('edit/<int:id_medico>/', views.edit_medico, name='edit_medico'),
    path('delete/<int:id_medico>/', views.delete_medico, name='delete_medico'),
]