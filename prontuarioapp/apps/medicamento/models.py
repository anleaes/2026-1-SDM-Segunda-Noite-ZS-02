from django.db import models

class Medicamento(models.Model):
    principio_ativo = models.CharField(max_length=200)
    e_controlado = models.BooleanField(default=False)
    categoria = models.CharField(max_length=150)
    nome_referencia = models.CharField(max_length=200)
    tem_generico = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Pessoa"
        verbise_name_plural = "Medicamentos"
        ordering =  ['id']
        
    def __str__(self):
        return self.nome_referencia