from django import forms
from django.forms import inlineformset_factory

from receita.models import Receita
from receitaMedicamento.models import ReceitaMedicamento


class ReceitaForm(forms.ModelForm):

    class Meta:
        model = Receita

        fields = [
            'consulta',
            'data_emissao',
            'validade',
            'instrucoes',
            'e_digital'
        ]


class ReceitaMedicamentoForm(forms.ModelForm):

    class Meta:
        model = ReceitaMedicamento

        fields = [
            'medicamento',
            'frequencia',
            'duracao_dias',
            'dose',
            'concentracao'
        ]


ReceitaMedicamentoFormSet = inlineformset_factory(
    Receita,
    ReceitaMedicamento,
    form=ReceitaMedicamentoForm,
    extra=1,
    can_delete=True
)