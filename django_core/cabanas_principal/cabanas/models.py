"""este archivo no se debe borrar por que es el modelo de cabanas"""
from django.db import models


class Cabanas
:
    """Modelo de cabaña"""  
    def __init__(self):
        pass
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    capacidad = models.PositiveIntegerField(default=1)
    precio_dia = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    precio_por_persona = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    ocupada = models.BooleanField(default=True)
    habilitada = models.BooleanField(default=True)
    descripcion = models.TextField(blank=True)
    class Meta:
        """ class para los nombres"""
        label = 'Cabaña'
        db_table = 'cabanas'
        managed = True
        verbose_name = 'cabaña'
        verbose_name_plural = 'cabañas'

    def __str__(self):
        
        return f"{self.nombre} (Capacidad: {self.capacidad})"
