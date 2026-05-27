from .models import ExameSolicitado
from rest_framework import serializers

class ExameSolicitadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExameSolicitado
        fields = '__all__'