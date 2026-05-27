from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'pessoa'

router = routers.SimpleRouter()
router.register('api', views.PessoaViewSet, basename='pessoa')

urlpatterns = [
    path('', include(router.urls)),
    path('list/', views.list_pessoa, name='list_pessoa'),
    path('add/', views.add_pessoa, name='add_pessoa'),
    path('edit/<int:id_pessoa>/', views.edit_pessoa, name='edit_pessoa'),
    path('delete/<int:id_pessoa>/', views.delete_pessoa, name='delete_pessoa'),
]