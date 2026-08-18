"""models Cabanas
"""
from django.db import models

class Cabanas
(models.Model):

    """clase Cabanas
"""
    id=models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    class Meta:
        """ class meta para el nombre"""
        verbose_name = "Cabanas
"
        verbose_name_plural = "Cabanas"
     def __str__(self: Cabanas
) -> str:
        return self.nombre

class CabanaCreate (models.Model):

    """clase Cabanas
"""
    id=models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)


class CabanaDelete (models.Model):

    """classe Cabanas
 delete"""
    id=models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

class  CabanaUpdate(models.Model):

    """clase Cabanas
"""
    id=models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)


class  EditarCabana(models.Model):

    """clase Cabanas
"""
    id=models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
  
  
class  GuardarCabana(models.Model):

    """clase Cabanas
"""
    id=models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

class ImprimirCabana(models.Model):

    """clase Cabanas
"""
    id=models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    
class DetailCabana(models.Model):

    """clase Cabanas
"""
    id=models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

