""" archivo: cabanas_api/models/clientes.py"""
from django.db import models

class Cliente(models.Model):
    """Modelo que representa un cliente en el sistema."""
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    class Meta:
        """Meta options for the Cliente model."""
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self) -> str:
        return str(self.nombre)
