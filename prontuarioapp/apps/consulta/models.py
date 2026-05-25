from django.db import models

class Consulta(models.Model):
    STATUS_CHOICES = [
        ('AG', 'Agendada'),
        ('RE', 'Realizada'),
        ('CA', 'Cancelada'),
    ]

    PRIORIDADE_CHOICES = [
        ('B', 'Baixa'),
        ('N', 'Normal'),
        ('A', 'Alta'),
        ('U', 'Urgência'),
    ]

    data_agendada = models.DateTimeField(verbose_name="Data e Hora Agendada")
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='AG')
    motivo = models.TextField(verbose_name="Motivo da Consulta")
    nivel_prioridade = models.CharField(max_length=1, choices=PRIORIDADE_CHOICES, default='N')
    
    # Chaves Estrangeiras
    paciente = models.ForeignKey('paciente.Paciente', on_delete=models.CASCADE, related_name='consultas')
    medico = models.ForeignKey('medico.Medico', on_delete=models.CASCADE, related_name='consultas')

    def __str__(self):
        return f"Consulta de {self.paciente} com {self.medico} em {self.data_agendada.strftime('%d/%m/%Y %H:%M')}"