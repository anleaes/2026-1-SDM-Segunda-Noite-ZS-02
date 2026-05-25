from django.db import models
from pessoa.models import Pessoa

# Create your models here.

class Medico(Pessoa):
    crm = models.CharField('CRM', max_length=20, unique=True)
    especialidade = models.CharField('Especialidade', max_length=200, default='Clinico Geral')
    matricula = models.CharField('Matrícula', max_length=20, unique=True)
    data_contratacao = models.DateField('Data de contratação')
    cargo = models.CharField('Cargo', max_length=50)
    esta_ativo = models.BooleanField('Está ativo', default=True)

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"

    def __str__(self):
        return f"Dr(a). {self.nome} {self.sobrenome}"