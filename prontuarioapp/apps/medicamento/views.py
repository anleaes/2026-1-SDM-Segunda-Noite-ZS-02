from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from django.db.models import Q

from .models import Medicamento
from .serializer import MedicamentoSerializer
from .forms import MedicamentoForm

# Create your views here.

class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer


def add_medicamento(request):
    template_name = 'medicamento/add_medicamento.html'
    context = {}

    if request.method == 'POST':
        form = MedicamentoForm(request.POST)

        if form.is_valid():
            medicamento = form.save()
            return redirect('medicamento:list_medicamento')

    form = MedicamentoForm()
    context['form'] = form

    return render(request, template_name, context)


def list_medicamento(request):
    template_name = 'medicamento/list_medicamento.html'

    medicamentos = Medicamento.objects.all()

    context = {
        'medicamentos': medicamentos
    }

    return render(request, template_name, context)


def edit_medicamento(request, id_medicamento):
    template_name = 'medicamento/add_medicamento.html'
    context = {}

    medicamento = get_object_or_404(Medicamento, id=id_medicamento)

    if request.method == 'POST':
        form = MedicamentoForm(request.POST, instance=medicamento)

        if form.is_valid():
            form.save()
            return redirect('medicamento:list_medicamento')

    form = MedicamentoForm(instance=medicamento)
    context['form'] = form

    return render(request, template_name, context)


def delete_medicamento(request, id_medicamento):
    template_name = 'medicamento/delete_medicamento.html'

    medicamento = get_object_or_404(Medicamento, id=id_medicamento)

    if request.method == 'POST':
        medicamento.delete()
        return redirect('medicamento:list_medicamento')

    context = {
        'medicamento': medicamento
    }

    return render(request, template_name, context)

def search_medicamento(request):
    template_name = 'medicamento/list_medicamento.html'
    query = request.GET.get('query')

    if query:
        # Busca se o termo está no nome de referência OU no princípio ativo
        medicamentos = Medicamento.objects.filter(
            Q(nome_referencia__icontains=query) | Q(principio_ativo__icontains=query)
        )
    else:
        medicamentos = Medicamento.objects.all()

    context = {
        'medicamentos': medicamentos
    }

    return render(request, template_name, context)