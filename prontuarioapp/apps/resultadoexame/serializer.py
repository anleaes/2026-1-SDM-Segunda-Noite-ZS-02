from .models import ResultadoExame
from rest_framework import serializers

class ResultadoExameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadoExame
        fields = '__all__'