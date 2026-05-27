from django.db import models
from medico.models import Medico
from paciente.models import Paciente

# Create your models here.

class Anamnese(models.Model):
    
    freqencia_choices = [
        ('NAO', 'Não consome'),
        ('EVE', 'Eventual'),
        ('DIA', 'Diário'),
    ]
    
    # auto_now_add=True grava automaticamente a data e hora do momento da criação do registro
    data_criacao = models.DateTimeField('Data de criação', auto_now_add=True)
    alergias = models.TextField('Alergias')
    alcool = models.CharField('Consumo de álcool', max_length=3, choices=freqencia_choices, default='NAO')
    fumante = models.CharField('Fumante', max_length=3, choices=freqencia_choices, default='NAO')
    medicamentos = models.TextField('Medicamentos em uso')
    queixa_principal = models.TextField('Queixa principal')
    
    
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name='Paciente')
    
    # on_delete=models.PROTECT impede a exclusão do médico caso ele já possua anamneses registradas
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT, verbose_name='Médico')

    class Meta:
        verbose_name = "Anamnese"
        verbose_name_plural = "Anamneses"

    def __str__(self):
        return f"""
        Paciente: {self.paciente} | Médico: {self.medico} | Data da Anamnese: {self.data_criacao.strftime('%d/%m/%Y')}
        Queixa Principal: {self.queixa_principal}
        Alergias: {self.alergias}
        Medicamentos em Uso: {self.medicamentos}
        Consumo de Álcool: {self.get_alcool_display()}
        Fumante: {self.get_fumante_display()}
        --------------------------------------------------
        """