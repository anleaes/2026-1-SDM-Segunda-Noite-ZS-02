from django.db import models

class Receita(models.Model):
    data_emissao = models.DateField(verbose_name="Data de Emissão")
    validade = models.DateField(verbose_name="Validade")
    instrucoes = models.TextField(verbose_name="Instruções")
    e_digital = models.BooleanField(default=False, verbose_name="É Digital?")
    
   
    consulta = models.ForeignKey('consulta.Consulta', on_delete=models.CASCADE, related_name='receitas')
    medicamentos = models.ManyToManyField('medicamento.Medicamento', related_name='receitas', blank=True)

    def __str__(self):
        return f"Receita da Consulta {self.consulta.id} - Emitida em {self.data_emissao.strftime('%d/%m/%Y')}"