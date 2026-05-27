from django import forms
from .models import ExameSolicitado


class ExameSolicitadoForm(forms.ModelForm):
    class Meta:
        model = ExameSolicitado
        fields = '__all__'