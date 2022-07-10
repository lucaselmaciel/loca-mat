from django.db import models

# Create your models here.

class TimestampedModel(models.Model):
    criado = models.DateTimeField(auto_now=True)
    modificado = models.DateTimeField(auto_now_add=True)