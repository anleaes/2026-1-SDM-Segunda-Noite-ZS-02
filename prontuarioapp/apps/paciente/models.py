from django.db import models
from pessoa.models import Pessoa

# Create your models here.


class Paciente(Pessoa):
    data_nascimento = models.DateField('Data de nascimento', null=False, blank=False)
    peso = models.FloatField('Peso (kg)', null=False, blank=False)
    altura = models.FloatField('Altura (m)', null=False, blank=False)
    endereco = models.CharField('Endereço completo', max_length=200)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return super().__str__()