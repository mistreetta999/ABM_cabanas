""" Models for the cabanas app."""
from django.db import models

class Cabana(models.Model):
    """Model representing a cabin."""
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self:Cabana) -> str:
        return self.nombre
