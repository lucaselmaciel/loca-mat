from django.db import models
from core.models import TimestampedModel

# Create your models here.


class Pessoa(TimestampedModel):
    nome = models.CharField('Nome', null=False, blank=False, max_length=255)
    cpf = models.CharField('CPF/CNPJ', null=True, blank=True, max_length=255)
    data_nascimento = models.DateField('Data de Nascimento')
    status_atraso_pagamento = models.BooleanField(default=False, null=False)

    def concat_nome_cpf(self):
        return self.nome + ' ' + self.cpf

# class Usuario(TimestampedModel):



