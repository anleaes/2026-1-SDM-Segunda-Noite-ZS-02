from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets

from .models import ResultadoExame
from .forms import ResultadoExameForm
from .serializer import ResultadoExameSerializer
# Create your views here.

class ResultadoExameViewSet(viewsets.ModelViewSet):
    queryset = ResultadoExame.objects.all()
    serializer_class = ResultadoExameSerializer

def list_resultado_exame(request):
    template_name = 'resultadoexame/list_resultado_exame.html'
    resultados = ResultadoExame.objects.all()

    context = {
        'resultados': resultados
    }

    return render(request, template_name, context)

def add_resultado_exame(request):
    template_name = 'resultadoexame/add_resultado_exame.html'
    context = {}

    if request.method == 'POST':
        form = ResultadoExameForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('resultadoexame:list_resultado_exame')

    form = ResultadoExameForm()
    context['form'] = form

    return render(request, template_name, context)

def edit_resultado_exame(request, id_resultado):
    template_name = 'resultadoexame/add_resultado_exame.html'
    context = {}

    resultado = get_object_or_404(ResultadoExame, id=id_resultado)

    if request.method == 'POST':
        form = ResultadoExameForm(request.POST, instance=resultado)

        if form.is_valid():
            form.save()
            return redirect('resultadoexame:list_resultado_exame')

    form = ResultadoExameForm(instance=resultado)
    context['form'] = form

    return render(request, template_name, context)

def delete_resultado_exame(request, id_resultado):
    template_name = 'resultadoexame/delete_resultado_exame.html'
    context = {}

    resultado = get_object_or_404(ResultadoExame, id=id_resultado)

    if request.method == 'POST':
        resultado.delete()
        return redirect('resultadoexame:list_resultado_exame')

    context['resultado'] = resultado

    return render(request, template_name, context)