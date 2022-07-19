from django.db import models
from core.models import TimestampedModel
from pessoas.models import Pessoa
# Create your models here.

class Equipamento(TimestampedModel):
    codigo = models.CharField('Código', null=False, blank=False, max_length=255)
    locacao_anterior = models.DateField(null=True, blank=True)
    modelo = models.CharField(max_length=255, null=True, blank=True)
    data_compra = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.modelo)


class Modelos(TimestampedModel):
    facricacao = models.CharField(null=True, blank=True, max_length=255)
    marca = models.CharField(null=False, blank=False, max_length=255)
    estado_conservacao = models.CharField(choices=(('1', 'Ruim'), ('2', 'Bom'), ('3', 'Ótimo')), null=False, blank=False, max_length=255)


class Locacoes(models.Model):
    criado = models.DateTimeField(auto_now=True, null=False, blank=False)
    modificado = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    cliente = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    endereco = models.CharField(null=True, blank=True, max_length=255)
    latitude = models.CharField(null=True, blank=True, max_length=255)
    longitude = models.CharField(null=True, blank=True, max_length=255)


