from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'cid'

router = routers.SimpleRouter()
router.register('', views.CidViewSet, basename='cid')

urlpatterns = [
    path('', include(router.urls) )
]