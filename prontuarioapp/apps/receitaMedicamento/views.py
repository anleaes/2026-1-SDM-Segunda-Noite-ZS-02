from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets

from .models import ReceitaMedicamento
from .forms import ReceitaMedicamentoForm
from .serializer import ReceitaMedicamentoSerializer

class ReceitaMedicamentoViewSet(viewsets.ModelViewSet):
    queryset = ReceitaMedicamento.objects.all()
    serializer_class = ReceitaMedicamentoSerializer

def list_receitamedicamento(request):
    template_name = 'receitamedicamento/list_receitamedicamento.html'
    # Como não tem data de emissão aqui, listamos pela receita vinculada
    receitamedicamentos = ReceitaMedicamento.objects.all().select_related('receita', 'medicamento')

    context = {
        'receitamedicamentos': receitamedicamentos
    }

    return render(request, template_name, context)

def add_receitamedicamento(request):
    template_name = 'receitamedicamento/add_receitamedicamento.html'
    context = {}

    if request.method == 'POST':
        form = ReceitaMedicamentoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('receitamedicamento:list_receitamedicamento')

    form = ReceitaMedicamentoForm()
    context['form'] = form

    return render(request, template_name, context)

def edit_receitamedicamento(request, id_receitamedicamento):
    template_name = 'receitamedicamento/add_receitamedicamento.html'
    context = {}

    receitamedicamento = get_object_or_404(ReceitaMedicamento, id=id_receitamedicamento)

    if request.method == 'POST':
        form = ReceitaMedicamentoForm(request.POST, instance=receitamedicamento)

        if form.is_valid():
            form.save()
            return redirect('receitamedicamento:list_receitamedicamento')

    form = ReceitaMedicamentoForm(instance=receitamedicamento)
    context['form'] = form

    return render(request, template_name, context)

def delete_receitamedicamento(request, id_receitamedicamento):
    template_name = 'receitamedicamento/delete_receitamedicamento.html'
    context = {}

    receitamedicamento = get_object_or_404(ReceitaMedicamento, id=id_receitamedicamento)

    if request.method == 'POST':
        receitamedicamento.delete()
        return redirect('receitamedicamento:list_receitamedicamento')

    context['receitamedicamento'] = receitamedicamento

    return render(request, template_name, context)