from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets

from .models import Paciente
from .forms import PacienteForm
from .serializer import PacienteSerializer

# Create your views here.
class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

def add_paciente(request):
    template_name = 'paciente/add_paciente.html'
    context = {}

    if request.method == 'POST':
        form = PacienteForm(request.POST)

        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.save()
            return redirect('paciente:list_paciente')

    form = PacienteForm()
    context['form'] = form

    return render(request, template_name, context)

def list_paciente(request):
    template_name = 'paciente/list_paciente.html'
    pacientes = Paciente.objects.all()

    context = {
        'pacientes': pacientes
    }

    return render(request, template_name, context)

def edit_paciente(request, id_paciente):
    template_name = 'paciente/add_paciente.html'
    context = {}

    paciente = get_object_or_404(Paciente, id=id_paciente)

    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)

        if form.is_valid():
            form.save()
            return redirect('paciente:list_paciente')

    form = PacienteForm(instance=paciente)
    context['form'] = form

    return render(request, template_name, context)

def delete_paciente(request, id_paciente):
    template_name = 'paciente/delete_paciente.html'

    paciente = get_object_or_404(Paciente, id=id_paciente)

    if request.method == 'POST':
        paciente.delete()
        return redirect('paciente:list_paciente')

    context = {
        'paciente': paciente
    }

    return render(request, template_name, context)