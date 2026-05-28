from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets

from rest_framework import viewsets

from .models import Anamnese
from .serializer import AnamneseSerializer
from .forms import AnamneseForm

from django.db.models import Q


# Create your views here.

class AnamneseViewSet(viewsets.ModelViewSet):
    queryset = Anamnese.objects.all()
    serializer_class = AnamneseSerializer

def add_anamnese(request):
    template_name = 'anamnese/add_anamnese.html'
    context = {}

    if request.method == 'POST':
        form = AnamneseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('anamnese:list_anamnese')

    form = AnamneseForm()
    context['form'] = form

    return render(request, template_name, context)

def list_anamnese(request):
    template_name = 'anamnese/list_anamnese.html'

    anamneses = Anamnese.objects.select_related('paciente', 'medico').all()

    context = {
        'anamneses': anamneses
    }

    return render(request, template_name, context)

def edit_anamnese(request, id_anamnese):
    template_name = 'anamnese/add_anamnese.html'
    context = {}

    anamnese = get_object_or_404(Anamnese, id=id_anamnese)

    if request.method == 'POST':
        form = AnamneseForm(request.POST, instance=anamnese)

        if form.is_valid():
            form.save()
            return redirect('anamnese:list_anamnese')

    form = AnamneseForm(instance=anamnese)
    context['form'] = form

    return render(request, template_name, context)

def delete_anamnese(request, id_anamnese):
    template_name = 'anamnese/delete_anamnese.html'

    anamnese = get_object_or_404(Anamnese, id=id_anamnese)

    if request.method == 'POST':
        anamnese.delete()
        return redirect('anamnese:list_anamnese')

    context = {
        'anamnese': anamnese
    }

    return render(request, template_name, context)


def search_anamnese(request):
    template_name = 'anamnese/list_anamnese.html'
    query = request.GET.get('query')

    if query:
        # Busca relacional por paciente, médico ou termos da queixa principal
        anamneses = Anamnese.objects.select_related('paciente', 'medico').filter(
            Q(paciente__nome__icontains=query) | 
            Q(medico__nome__icontains=query) |
            Q(queixa_principal__icontains=query)
        )
    else:
        anamneses = Anamnese.objects.select_related('paciente', 'medico').all()

    context = {
        'anamneses': anamneses
    }

    return render(request, template_name, context)
