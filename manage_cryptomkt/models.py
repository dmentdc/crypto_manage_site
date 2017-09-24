import datetime

from django.db import models
from decimal import Decimal
from django.utils import timezone

# Create your models here.

class Coin(models.Model):
    """data para Coin"""
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre

class Precio(models.Model):
    """Precio en un instante de una crypto moneda en un mercado"""
    coin = models.ForeignKey(Coin, on_delete=models.DO_NOTHING, null=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    tipo = models.CharField(max_length=10, null=True)
    moneda = models.CharField(max_length=5, null=True)
    mercado = models.CharField(max_length=200, null=True)
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.coin + self.valor