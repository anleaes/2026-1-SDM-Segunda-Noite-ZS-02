from django.db import models

# Create your models here.
class Cid(models.Model):
    cod_cid = models.CharField(max_length=10, unique=True)
    descricao = models.CharField(max_length=255)
    sintomas = models.TextField()
    tipo = models.CharField(max_length=100)
    status_ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'cid'
        verbose_name_plural = 'cids'
        ordering =['id']

    def __str__(self):
        return f"{self.cod_cid} - {self.descricao}"
