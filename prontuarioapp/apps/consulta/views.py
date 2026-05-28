from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets

from .models import Consulta
from .forms import ConsultaForm
from .serializer import ConsultaSerializer
from django.db.models import Q

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

def list_consulta(request):
    template_name = 'consulta/list_consulta.html'
    consultas = Consulta.objects.all().order_by('-data_agendada')

    context = {
        'consultas': consultas
    }

    return render(request, template_name, context)

def add_consulta(request):
    template_name = 'consulta/add_consulta.html'
    context = {}

    if request.method == 'POST':
        form = ConsultaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('consulta:list_consulta')

    form = ConsultaForm()
    context['form'] = form

    return render(request, template_name, context)

def edit_consulta(request, id_consulta):
    template_name = 'consulta/add_consulta.html'
    context = {}

    consulta = get_object_or_404(Consulta, id=id_consulta)

    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)

        if form.is_valid():
            form.save()
            return redirect('consulta:list_consulta')

    form = ConsultaForm(instance=consulta)
    context['form'] = form

    return render(request, template_name, context)

def delete_consulta(request, id_consulta):
    template_name = 'consulta/delete_consulta.html'
    context = {}

    consulta = get_object_or_404(Consulta, id=id_consulta)

    if request.method == 'POST':
        consulta.delete()
        return redirect('consulta:list_consulta')

    context['consulta'] = consulta

    return render(request, template_name, context)


def search_consulta(request):
    template_name = 'consulta/list_consulta.html'
    query = request.GET.get('query')

    if query:
        # Busca nome do paciente, nome do médico ou pelo motivo da consulta
        consultas = Consulta.objects.filter(
            Q(paciente__nome__icontains=query) | 
            Q(medico__nome__icontains=query) |
            Q(motivo__icontains=query)
        ).order_by('-data_agendada')
    else:
        consultas = Consulta.objects.all().order_by('-data_agendada')

    context = {
        'consultas': consultas
    }

    return render(request, template_name, context)