from django import forms
from .models import Receita

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['consulta', 'data_emissao', 'validade', 'instrucoes', 'e_digital']
        
        labels = {
            'consulta': 'Consulta Relacionada',
            'data_emissao': 'Data de Emissão',
            'validade': 'Validade da Receita',
            'instrucoes': 'Instruções Gerais',
            'e_digital': 'Receita Digital?',
        }
        
        widgets = {
            'consulta': forms.Select(attrs={
                'class': 'form-control'
            }),
            'data_emissao': forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date'  # Renderiza um calendário no HTML5
            }),
            'validade': forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date'  # Renderiza um calendário no HTML5
            }),
            'instrucoes': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4,
                'placeholder': 'Observações ou instruções gerais (opcional)'
            }),
            'e_digital': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }