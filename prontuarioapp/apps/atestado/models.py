from django.db import models
from cid.models import Cid
from consulta.models import Consulta

# Create your models here.
class Atestado(models.Model):
    codigo_autenticacao = models.CharField(max_length=50, unique=True)
    data_inicio_afastamento = models.DateField()
    quantidade_dias = models.IntegerField()
    tipo_atestado = models.CharField('Tipo de Atestado', max_length=40, choices=[
        ('MEDICO', 'Médico'),
        ('ODONTO', 'Odontológico'),
        ('OUTRO', 'Outro'),
    ])
    consulta = models.OneToOneField(Consulta, on_delete=models.CASCADE)
    cid = models.ForeignKey(Cid, on_delete=models.PROTECT)

    def __str__(self):
        return f"Atestado {self.codigo_autenticacao}"