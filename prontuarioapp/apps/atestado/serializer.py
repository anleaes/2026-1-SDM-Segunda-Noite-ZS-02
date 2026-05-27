from .models import Atestado
from rest_framework import serializers

class AtestadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atestado
        fields = '__all__'
