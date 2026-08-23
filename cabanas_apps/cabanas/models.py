"""cabana models"""
from django.db import models

class Cabana(models.Model):
    """ class cabana"""
    nombre = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()
    descripcion = models.TextField(blank=True, null=True)
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    class Metas ():
        """ class meta"""
        vervose_nom = "Cabana"

    def __str__(self) -> str:
        return str(self.nombre)
