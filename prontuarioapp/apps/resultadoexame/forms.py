from django import forms
from .models import ResultadoExame


class ResultadoExameForm(forms.ModelForm):

    class Meta:
        model = ResultadoExame
        fields = [
            'data_resultado',
            'conclusoes',
            'valor',
            'unidade_medida',
            'exame_solicitado',
        ]

        widgets = {
            'data_resultado': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'conclusoes': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 4}
            ),
            'valor': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'unidade_medida': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'exame_solicitado': forms.Select(
                attrs={'class': 'form-control'}
            ),
        }