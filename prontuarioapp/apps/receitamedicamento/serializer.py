from rest_framework import serializers
from .models import ReceitaMedicamento

class ReceitaMedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceitaMedicamento
        fields = '__all__'