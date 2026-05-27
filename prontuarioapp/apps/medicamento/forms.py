from django import forms
from .models import Medicamento


class MedicamentoForm(forms.ModelForm):

    class Meta:
        model = Medicamento
        fields = [
            'principio_ativo',
            'e_controlado',
            'categoria',
            'nome_referencia',
            'tem_generico',
        ]

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'rows': 3}),
            'concentracao': forms.TextInput(attrs={'class': 'form-control'}),
            'forma_farmaceutica': forms.TextInput(attrs={'class': 'form-control'}),
        }