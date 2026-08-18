"""models Cabanas
"""
from django.db import models


class Cabanas
(models.Model):

    """class Cabanas
"""
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio_por_noche = models.IntegerField()
    disponible = models.BooleanField(default=True)
    class Meta:
        """Meta informacion para Cabanas
 model"""
        app_label = "cabanas"
        verbose_name = "Cabanas
"
        verbose_name_plural = "Cabanas"

    def __str__(self) -> str:
        return str(self.nombre)


class CabanaLista(models.Model):

    """class Cabanas
"""
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio_por_noche = models.IntegerField()
    disponible = models.BooleanField(default=True)
class CabanaEliminar(models.Model):

    """class Cabanas
"""
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio_por_noche = models.IntegerField()
    disponible = models.BooleanField(default=True)
class CabanaGuardar(models.Model):

    """class Cabanas
"""
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio_por_noche = models.IntegerField()
    disponible = models.BooleanField(default=True)

class CabanaImprimir(models.Model):

    """class Cabanas
"""
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio_por_noche = models.IntegerField()
    disponible = models.BooleanField(default=True)

class CabanaEliminar(models.Model):

    """class Cabanas
"""
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio_por_noche = models.IntegerField()
    disponible = models.BooleanField(default=True)



