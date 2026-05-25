from .models import Cid
from rest_framework import serializers

class CidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cid
        fields = '__all__'