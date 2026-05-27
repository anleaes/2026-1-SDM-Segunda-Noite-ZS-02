from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .serializer import ReceitaMedicamentoSerializer
from .models import ReceitaMedicamento

# Create your views here.

class ReceitaMedicamentoViewSet(viewsets.ModelViewSet):
    queryset = ReceitaMedicamento.objects.all()
    serializer_class = ReceitaMedicamentoSerializer

#FUNÇÕES DAS TELAS COMEÇAM AQUI

def list_receitamedicamento(request):
    # Busca todas as ligações de receita e medicamento no banco
    receitas_med = ReceitaMedicamento.objects.all()
    
    context = {
        'receitas_med': receitas_med
    }
    # Manda os dados para a tela HTML
    return render(request, 'receitaMedicamento/list.html', context)