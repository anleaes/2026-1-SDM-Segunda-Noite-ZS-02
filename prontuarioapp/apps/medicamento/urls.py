from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'medicamento'

router = routers.SimpleRouter()
router.register('', views.MedicamentoViewSet, basename='medicamento')

urlpatterns = [
    path('', include(router.urls)),
]