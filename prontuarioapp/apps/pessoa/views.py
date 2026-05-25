from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets

from .models import Pessoa
from .serializer import PessoaSerializer
from .forms import PessoaForm

# Create your views here.
class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

def add_pessoa(request):
    template_name = 'pessoa/add_pessoa.html'
    context = {}

    if request.method == 'POST':
        form = PessoaForm(request.POST)

        if form.is_valid():
            pessoa = form.save(commit=False)
            pessoa.save()
            return redirect('pessoa:list_pessoa')

    form = PessoaForm()
    context['form'] = form

    return render(request, template_name, context)

def list_pessoa(request):
    template_name = 'pessoa/list_pessoa.html'
    pessoas = Pessoa.objects.all()

    context = {
        'pessoas': pessoas
    }

    return render(request, template_name, context)

def edit_pessoa(request, id_pessoa):
    template_name = 'pessoa/add_pessoa.html'
    context = {}

    pessoa = get_object_or_404(Pessoa, id=id_pessoa)

    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)

        if form.is_valid():
            form.save()
            return redirect('pessoa:list_pessoa')

    form = PessoaForm(instance=pessoa)
    context['form'] = form

    return render(request, template_name, context)

def delete_pessoa(request, id_pessoa):
    template_name = 'pessoa/delete_pessoa.html'

    pessoa = get_object_or_404(Pessoa, id=id_pessoa)

    if request.method == 'POST':
        pessoa.delete()
        return redirect('pessoa:list_pessoa')

    context = {
        'pessoa': pessoa
    }

    return render(request, template_name, context)