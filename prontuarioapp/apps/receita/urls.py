from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'receita'

router = routers.SimpleRouter()
router.register('', views.ReceitaViewSet, basename='receita')

urlpatterns = [
    # path('', include(router.urls)),
    path('list/', views.list_receita, name='list_receita'),
    path('add/', views.add_receita, name='add_receita'),
    path('edit/<int:id_receita>/', views.edit_receita, name='edit_receita'),
    path('delete/<int:id_receita>/', views.delete_receita, name='delete_receita'),
]