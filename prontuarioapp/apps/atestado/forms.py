from django import forms
from .models import Atestado


class AtestadoForm(forms.ModelForm):
    class Meta:
        model = Atestado
        fields = '__all__'