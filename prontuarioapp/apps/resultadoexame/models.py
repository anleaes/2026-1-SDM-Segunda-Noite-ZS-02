from django.db import models
from examesolicitado.models import ExameSolicitado

# Create your models here.
class ResultadoExame(models.Model):
    data_resultado = models.DateField()
    conclusoes = models.TextField()
    valor = models.FloatField()
    unidade_medida = models.CharField(max_length=50)

    exame_solicitado = models.ForeignKey(ExameSolicitado, on_delete=models.CASCADE)

    def __str__(self):
        return f"Resultado - {self.exame_solicitado.nome_exame}"