from django.db import models
from core.models import TimestampedModel
# Create your models here.

class Equipamento(TimestampedModel):
    codigo = models.CharField('Código', null=False, blank=False, max_length=255)
    locacao_anterior = models.DateField(null=True, blank=True)
    modelo = models.CharField(max_length=255, null=True, blank=True)
    data_compra = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.modelo)