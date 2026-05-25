from rest_framework import viewsets
from .models import ReceitaMedicamento
from .serializer import ReceitaMedicamentoSerializer


# Create your views here.
class ReceitaMedicamentoViewSet(viewsets.ModelViewSet):
    queryset = ReceitaMedicamento.objects.all()
    serializer_class = ReceitaMedicamentoSerializer