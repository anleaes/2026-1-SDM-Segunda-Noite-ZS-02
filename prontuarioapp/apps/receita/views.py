from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets

from .models import Receita
from .serializer import ReceitaSerializer
from .forms import (
    ReceitaForm,
    ReceitaMedicamentoFormSet
)

# Create your views here.
class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer

def list_receita(request):

    receitas = Receita.objects.all()

    context = {
        'receitas': receitas
    }

    return render(
        request,
        'receita/list_receita.html',
        context
    )


def add_receita(request):

    if request.method == 'POST':

        form = ReceitaForm(request.POST)

        formset = ReceitaMedicamentoFormSet(request.POST)

        if form.is_valid() and formset.is_valid():

            receita = form.save()

            formset.instance = receita
            formset.save()

            return redirect('receita:list_receita')

    else:

        form = ReceitaForm()

        formset = ReceitaMedicamentoFormSet()

    context = {
        'form': form,
        'formset': formset
    }

    return render(
        request,
        'receita/add_receita.html',
        context
    )


def edit_receita(request, id_receita):

    receita = get_object_or_404(
        Receita,
        pk=id_receita
    )

    if request.method == 'POST':

        form = ReceitaForm(
            request.POST,
            instance=receita
        )

        formset = ReceitaMedicamentoFormSet(
            request.POST,
            instance=receita
        )

        if form.is_valid() and formset.is_valid():

            form.save()
            formset.save()

            return redirect('receita:list_receita')

    else:

        form = ReceitaForm(
            instance=receita
        )

        formset = ReceitaMedicamentoFormSet(
            instance=receita
        )

    context = {
        'form': form,
        'formset': formset
    }

    return render(
        request,
        'receita/add_receita.html',
        context
    )


def delete_receita(request, id_receita):

    receita = get_object_or_404(
        Receita,
        pk=id_receita
    )

    receita.delete()

    return redirect('receita:list_receita')