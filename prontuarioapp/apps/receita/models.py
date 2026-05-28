from django.db import models
class Receita(models.Model):
    consulta = models.ForeignKey(
        'consulta.Consulta', 
        on_delete=models.CASCADE, 
        related_name='receitas',
        verbose_name="Consulta"
    )
    data_emissao = models.DateField(verbose_name="Data de Emissão")
    validade = models.DateField(verbose_name="Validade")
    instrucoes = models.TextField(blank=True, null=True, verbose_name="Instruções Gerais")
    e_digital = models.BooleanField(default=True, verbose_name="É Digital?")
    
    medicamentos = models.ManyToManyField(
        'medicamento.Medicamento',
        through='receitaMedicamento.ReceitaMedicamento',
        related_name='receitas',
        verbose_name="Medicamentos"
    )

    class Meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"
        ordering = ['-data_emissao']

    def __str__(self):
        return f"Receita {self.id} - Consulta {self.consulta_id} ({self.data_emissao})"
    
    