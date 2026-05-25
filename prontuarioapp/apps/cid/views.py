from django.shortcuts import render
from .models import Employee
from rest_framework import viewsets
from .serializer import CidSerializer

# Create your views here.

class CidViewSet(viewsets.ModelViewSet):
    queryset = Cid.objects.all()
    serializer_class = CidSerializer  
