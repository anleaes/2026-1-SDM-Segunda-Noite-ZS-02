from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets

from .models import Medico
from .serializer import MedicoSerializer
from .forms import MedicoForm

# Create your views here.
class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

def add_medico(request):
    template_name = 'medico/add_medico.html'
    context = {}

    if request.method == 'POST':
        form = MedicoForm(request.POST)

        if form.is_valid():
            medico = form.save()
            return redirect('medico:list_medico')

    form = MedicoForm()
    context['form'] = form

    return render(request, template_name, context)

def list_medico(request):
    template_name = 'medico/list_medico.html'

    medicos = Medico.objects.all()

    context = {
        'medicos': medicos
    }

    return render(request, template_name, context)

def edit_medico(request, id_medico):
    template_name = 'medico/add_medico.html'
    context = {}

    medico = get_object_or_404(Medico, id=id_medico)

    if request.method == 'POST':
        form = MedicoForm(request.POST, instance=medico)

        if form.is_valid():
            form.save()
            return redirect('medico:list_medico')

    form = MedicoForm(instance=medico)
    context['form'] = form

    return render(request, template_name, context)

def delete_medico(request, id_medico):
    template_name = 'medico/delete_medico.html'

    medico = get_object_or_404(Medico, id=id_medico)

    if request.method == 'POST':
        medico.delete()
        return redirect('medico:list_medico')

    context = {
        'medico': medico
    }

    return render(request, template_name, context)
