from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'anamnese'

router = routers.SimpleRouter()
router.register('api', views.AnamneseViewSet, basename='anamnese')

urlpatterns = [
    path('', include(router.urls)),

    path('list/', views.list_anamnese, name='list_anamnese'),
    path('add/', views.add_anamnese, name='add_anamnese'),
    path('edit/<int:id_anamnese>/', views.edit_anamnese, name='edit_anamnese'),
    path('delete/<int:id_anamnese>/', views.delete_anamnese, name='delete_anamnese'),
]
