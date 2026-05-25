from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'consulta'

router = routers.SimpleRouter()
router.register('', views.ConsultaViewSet, basename='consulta')

urlpatterns = [
    path('', include(router.urls)),
]