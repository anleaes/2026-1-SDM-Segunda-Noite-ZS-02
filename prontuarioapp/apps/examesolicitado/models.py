from django.db import models
from consulta.models import Consulta

# Create your models here.
class ExameSolicitado(models.Model):
    nome_exame = models.CharField(max_length=100)
    descricao = models.TextField()
    preparo = models.TextField()
    exige_jejum = models.BooleanField(default=False)

    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Exame solicitado'
        verbose_name_plural = 'Exames solicitados'
        ordering =['id']


    def __str__(self):
        return self.nome_exame
