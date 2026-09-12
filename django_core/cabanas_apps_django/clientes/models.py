""" archivo de modelos para la app de clientes """
import logging
from typing import Any
from django.db import models

LOGGER = logging.getLogger(__name__)

class Cliente(models.Model):
    """clientes"""
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    class Meta:
        """Metadatos del modelo Cliente."""
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class ClienteDatos(models.Model):
    """ Modelo que representa un cliente """
    dni = models.IntegerField()
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} - DNI: {self.dni}"

    def actualizar(self, **datos: Any) -> "ClienteDatos":
        """Actualiza los campos recibidos del cliente y guarda el cambio."""
        for campo, valor in datos.items():
            setattr(self, campo, valor)
        self.save(update_fields=list(datos.keys()) if datos else None)
        return self

    def eliminar(self):
        """Elimina este cliente de la base de datos."""
        return self.delete()
