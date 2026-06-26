""" models.py - Definición del modelo Reserva. """
from pathlib import Path
from django.db import models
from cabanas_apps.clientes.models import Cliente
from cabanas_apps.cabanas_app.models import Cabana

class Reserva(models.Model):
    """Modelo que representa una reserva de cabaña."""
    id=models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=20, default="pendiente")

    def __str__(self):
        return f"Reserva {self.id} - {self.cliente}"
