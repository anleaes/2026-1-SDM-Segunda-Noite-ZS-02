from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets

from .models import Atestado
from .forms import AtestadoForm
from .serializer import AtestadoSerializer

# Create your views here.
def add_atestado(request):
    template_name = 'atestado/add_atestado.html'
    context = {}

    if request.method == 'POST':
        form = AtestadoForm(request.POST)

        if form.is_valid():
            atestado = form.save(commit=False)
            atestado.save()
            return redirect('atestado:list_atestado')

    form = AtestadoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_atestado(request):
    template_name = 'atestado/list_atestado.html'
    atestados = Atestado.objects.all()

    context = {
        'atestados': atestados
    }

    return render(request, template_name, context)

def edit_atestado(request, id_atestado):
    template_name = 'atestado/add_atestado.html'
    context = {}

    atestado = get_object_or_404(Atestado, id=id_atestado)

    if request.method == 'POST':
        form = AtestadoForm(request.POST, instance=atestado)

        if form.is_valid():
            form.save()
            return redirect('atestado:list_atestado')

    form = AtestadoForm(instance=atestado)
    context['form'] = form

    return render(request, template_name, context)

def delete_atestado(request, id_atestado):
    template_name = 'atestado/delete_atestado.html'

    atestado = get_object_or_404(Atestado, id=id_atestado)

    if request.method == 'POST':
        atestado.delete()
        return redirect('atestado:list_atestado')

    context = {
        'atestado': atestado
    }

    return render(request, template_name, context)
