from decimal import Decimal
""" cabana models"""
from django.db import models

class Cabana(models.Model):
    """ class cabans"""
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    class Meta:
        """ class meta"""
        verbose_name = "Cabana"
        verbose_name_plural = "Cabanas"
    def __str__(self):
        return str(self.nombre)
