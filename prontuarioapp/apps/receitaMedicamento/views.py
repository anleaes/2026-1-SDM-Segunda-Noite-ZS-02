from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .serializer import ReceitaMedicamentoSerializer
from .models import ReceitaMedicamento

# Create your views here.

class ReceitaMedicamentoViewSet(viewsets.ModelViewSet):
    queryset = ReceitaMedicamento.objects.all()
    serializer_class = ReceitaMedicamentoSerializer
