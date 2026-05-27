from .models import ReceitaMedicamento
from rest_framework import serializers

class ReceitaMedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceitaMedicamento
        fields = '__all__'