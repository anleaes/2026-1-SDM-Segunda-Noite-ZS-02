from django import forms
from .models import Anamnese

class AnamneseForm(forms.ModelForm):
    class Meta:
        model = Anamnese

        fields = [
            'paciente',
            'medico',
            'alergias',
            'alcool',
            'fumante',
            'medicamentos',
            'queixa_principal',
        ]

        widgets = {
            'paciente': forms.Select(),
            'medico': forms.Select(),

            'alergias': forms.Textarea(attrs={'rows': 3}),
            'medicamentos': forms.Textarea(attrs={'rows': 3}),
            'queixa_principal': forms.Textarea(attrs={'rows': 3}),
        }