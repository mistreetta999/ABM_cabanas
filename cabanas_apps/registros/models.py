"""
    Modelos para la aplicación de registros.
"""
from os import path
from django.db import models
from cabanas_apps.clientes.models import Cliente

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class ActividadCabana(models.Model):
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cabana} - {str(self.descripcion)[:30]}"
