from django import forms
from .models import ReceitaMedicamento

class ReceitaMedicamentoForm(forms.ModelForm):
    class Meta:
        model = ReceitaMedicamento
        fields = ['receita', 'medicamento', 'frequencia', 'duracao_dias', 'dose', 'concentracao']
        
        labels = {
            'receita': 'Receita',
            'medicamento': 'Medicamento Prescrito',
            'frequencia': 'Frequência',
            'duracao_dias': 'Duração (em dias)',
            'dose': 'Dose',
            'concentracao': 'Concentração',
        }
        
        widgets = {
            'receita': forms.Select(attrs={
                'class': 'form-control'
            }),
            'medicamento': forms.Select(attrs={
                'class': 'form-control'
            }),
            'frequencia': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: De 8 em 8 horas'
            }),
            'duracao_dias': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1', # Impede que o usuário digite 0 ou dias negativos no HTML
                'placeholder': 'Ex: 7'
            }),
            'dose': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 1 comprimido, 5ml, 2 gotas'
            }),
            'concentracao': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 500mg, 10mg/ml'
            }),
        }