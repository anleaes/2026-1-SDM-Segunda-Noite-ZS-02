from django.db import models

class ReceitaMedicamento(models.Model):
    frequencia = models.CharField(max_length=100, verbose_name="Frequência")
    duracao_dias = models.IntegerField(verbose_name="Duração em dias")
    dose = models.CharField(max_length=100, verbose_name="Dose")
    concentracao = models.CharField(max_length=100, verbose_name="Concentração")
    
    
    receita = models.ForeignKey('receita.Receita', on_delete=models.CASCADE, related_name='itens_receita')
    medicamento = models.ForeignKey('medicamento.Medicamento', on_delete=models.CASCADE, related_name='itens_receita')

    def __str__(self):
        return f"{self.medicamento} - {self.dose} (Receita: {self.receita.id})"