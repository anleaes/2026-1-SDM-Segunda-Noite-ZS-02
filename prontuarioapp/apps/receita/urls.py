from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'receita'

router = routers.SimpleRouter()
router.register('', views.ReceitaViewSet, basename='receita')

urlpatterns = [
    path('', include(router.urls)),
]