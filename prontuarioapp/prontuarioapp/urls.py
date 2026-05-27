"""
URL configuration for prontuarioapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pessoa.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cid/', include('cid.urls', namespace='cid')),
    path('atestado/', include('atestado.urls', namespace='atestado')),
    path('exameSolicitado/', include('examesolicitado.urls', namespace='examesolicitado')),
    path('paciente/', include('paciente.urls', namespace='paciente')),
    path('medico/', include('medico.urls')),
    path('anamnese/', include('anamnese.urls')),
    path('resultadoexame/', include('resultadoexame.urls')),
    path('consulta/', include('consulta.urls')),
    path('medicamento/', include('medicamento.urls', namespace='medicamento')),
    path('receita/', include('receita.urls', namespace='receita')),
    path('receitaMedicamento/', include('receitaMedicamento.urls', namespace='receitamedicamento')),

]

