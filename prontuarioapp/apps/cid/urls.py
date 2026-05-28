from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'cid'

router = routers.SimpleRouter()
router.register('api', views.CidViewSet, basename='cid')

urlpatterns = [
    path('', include(router.urls) ),
    path('list/', views.list_cid, name='list_cid'),
    path('add/', views.add_cid, name='add_cid'),
    path('edit/<int:id_cid>/', views.edit_cid, name='edit_cid'),
    path('delete/<int:id_cid>/', views.delete_cid, name='delete_cid'),
    path('buscar/', views.search_cid, name='search_cid'),
]