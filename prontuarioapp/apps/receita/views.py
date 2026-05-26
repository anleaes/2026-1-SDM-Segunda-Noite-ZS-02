from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets

from .models import Receita
from .serializer import ReceitaSerializer
from .forms import ReceitaForm

# Create your views here.
class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer

def list_receita(request):
    template_name = 'receita/list_receita.html'
    receitas = Receita.objects.all().order_by('-data_emissao')

    context = {
        'receitas': receitas
    }

    return render(request, template_name, context)

def add_receita(request):
    template_name = 'receita/add_receita.html'
    context = {}

    if request.method == 'POST':
        form = ReceitaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('receita:list_receita')

    form = ReceitaForm()
    context['form'] = form

    return render(request, template_name, context)

def edit_receita(request, id_receita):
    template_name = 'receita/add_receita.html'
    context = {}

    receita = get_object_or_404(Receita, id=id_receita)

    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=receita)

        if form.is_valid():
            form.save()
            return redirect('receita:list_receita')

    form = ReceitaForm(instance=receita)
    context['form'] = form

    return render(request, template_name, context)

def delete_receita(request, id_receita):
    template_name = 'receita/delete_receita.html'
    context = {}

    receita = get_object_or_404(Receita, id=id_receita)

    if request.method == 'POST':
        receita.delete()
        return redirect('receita:list_receita')

    context['receita'] = receita

    return render(request, template_name, context)