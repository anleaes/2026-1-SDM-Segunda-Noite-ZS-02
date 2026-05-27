from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import ExameSolicitado
from .serializer import ExameSolicitadoSerializer
from .forms import ExameSolicitadoForm

# Create your views here.
class ExameSolicitadoViewSet(viewsets.ModelViewSet):
    queryset = ExameSolicitado.objects.all()
    serializer_class = ExameSolicitadoSerializer 

def add_exame_solicitado(request):
    template_name = 'exameSolicitado/add_exame_solicitado.html'
    context = {}

    if request.method == 'POST':
        form = ExameSolicitadoForm(request.POST)

        if form.is_valid():
            exame = form.save(commit=False)
            exame.save()
            return redirect('exameSolicitado:list_exame_solicitado')

    form = ExameSolicitadoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_exame_solicitado(request):
    template_name = 'exameSolicitado/list_exame_solicitado.html'
    exames = ExameSolicitado.objects.all()

    context = {
        'exames': exames
    }

    return render(request, template_name, context)

def edit_exame_solicitado(request, id_exame_solicitado):
    template_name = 'exameSolicitado/add_exame_solicitado.html'
    context = {}

    exame = get_object_or_404(ExameSolicitado, id=id_exame_solicitado)

    if request.method == 'POST':
        form = ExameSolicitadoForm(request.POST, instance=exame)

        if form.is_valid():
            form.save()
            return redirect('exameSolicitado:list_exame_solicitado')

    form = ExameSolicitadoForm(instance=exame)
    context['form'] = form

    return render(request, template_name, context)

def delete_exame_solicitado(request, id_exame_solicitado):
    template_name = 'exameSolicitado/delete_exame_solicitado.html'

    exame = get_object_or_404(ExameSolicitado, id=id_exame_solicitado)

    if request.method == 'POST':
        exame.delete()
        return redirect('exameSolicitado:list_exame_solicitado')

    context = {
        'exame': exame
    }

    return render(request, template_name, context)