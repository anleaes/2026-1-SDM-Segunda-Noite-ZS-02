from django.urls import path
from . import views

app_name = 'atestado'

urlpatterns = [
    path('', views.list_atestado, name='list_atestado'),
    path('add/', views.add_atestado, name='add_atestado'),
    path('edit/<int:id_atestado>/', views.edit_atestado, name='edit_atestado'),
    path('delete/<int:id_atestado>/', views.delete_atestado, name='delete_atestado'),
]
