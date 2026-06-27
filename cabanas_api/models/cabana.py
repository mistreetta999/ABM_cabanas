"""Este archivo contiene el modelo de la app cabanas_api.
"""
from django.db import models

class Cabana(models.Model):
    """Modelo que representa una Cabana en la aplicación.
    """
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    precio_por_cabana = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return str(self.nombre)
