"""este archivo no se debe borrar por que es el modelo de cabanas"""
from django.db import models


class Cabana:
    def __init__(self):
        pass
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    capacidad = models.PositiveIntegerField(default=1)
    precio_dia = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    precio_por_persona = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    ocupada = models.BooleanField(default=False)
    habilitada = models.BooleanField(default=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        
        return f"{self.nombre} (Capacidad: {self.capacidad})"
