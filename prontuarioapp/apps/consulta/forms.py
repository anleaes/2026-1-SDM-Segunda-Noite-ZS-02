from django import forms
from .models import Consulta


class ConsultaForm(forms.ModelForm):

    class Meta:
        model = Consulta
        fields = [
            'data_agendada',
            'status',
            'motivo',
            'nivel_prioridade',
            'paciente',
            'medico',
        ]

        widgets = {
            'data_agendada': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            ),

            'status': forms.Select(
                attrs={'class': 'form-control'}
            ),

            'motivo': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 4}
            ),

            'nivel_prioridade': forms.Select(
                attrs={'class': 'form-control'}
            ),

            'paciente': forms.Select(
                attrs={'class': 'form-control'}
            ),

            'medico': forms.Select(
                attrs={'class': 'form-control'}
            ),
        }