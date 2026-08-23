"""models Cabanas"""
from django.db import models


class Cabanas(models.Model):
    """clase Cabanas"""
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    class Meta:
        """class meta para el nombre"""
        verbose_name = "Cabanas"
        verbose_name_plural = "Cabanas"

    def __str__(self) -> str:
        return str(self.nombre)


class CabanaCreate(models.Model):
    """clase Cabanas"""
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.nombre)


class CabanaDelete(models.Model):
    """classe Cabanas borrar"""
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.nombre)


class CabanaUpdate(models.Model):
    """clase Cabanas"""
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)


class EditarCabana(models.Model):
    """class editar cabana"""
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)


class GuardarCabana(models.Model):
    """clase Cabanas"""
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)


class ImprimirCabana(models.Model):
    """clase Cabanas"""
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.nombre)


class DetailCabana(models.Model):
    """clase Cabanas"""
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.nombre)