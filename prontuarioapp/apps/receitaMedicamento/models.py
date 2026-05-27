from django.db import models
from receita.models import Receita
from medicamento.models import Medicamento

class ReceitaMedicamento(models.Model):
    # Chaves estrangeiras obrigatórias para a tabela intermediária
    receita = models.ForeignKey(
        Receita, 
        on_delete=models.CASCADE, 
        related_name='detalhes_medicamentos',
        verbose_name="Receita"
    )
    medicamento = models.ForeignKey(
        'medicamento.Medicamento', 
        on_delete=models.PROTECT,  # Impede a exclusão do medicamento se ele constar em uma receita
        related_name='detalhes_receitas',
        verbose_name="Medicamento"
    )
    
    # Atributos específicos da prescrição contidos no diagrama
    frequencia = models.CharField(max_length=100, verbose_name="Frequência (Ex: 8h em 8h)")
    duracao_dias = models.PositiveIntegerField(verbose_name="Duração (Dias)")
    dose = models.CharField(max_length=50, verbose_name="Dose (Ex: 1 comprimido)")
    concentracao = models.CharField(max_length=50, verbose_name="Concentração (Ex: 500mg)")

    class Meta:
        verbose_name = "Medicamento da Receita"
        verbose_name_plural = "Medicamentos da Receita"
        unique_together = ('receita', 'medicamento')

    def __str__(self):
        return f"{self.medicamento} na Receita {self.receita_id}"