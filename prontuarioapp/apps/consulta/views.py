from rest_framework import viewsets
from .models import Consulta
from .serializer import ConsultaSerializer

# Create your views here.
class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer