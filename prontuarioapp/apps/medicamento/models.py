from django.db import models

class Medicamento(models.Model):
    nome_referencia = models.CharField(max_length=200)

    principio_ativo = models.CharField(max_length=200)

    categoria = models.CharField(max_length=150)

    e_controlado = models.BooleanField(default=False)

    tem_generico = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_referencia