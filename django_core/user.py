"""Modelo que representa a un usuario registrado."""

from django.db import models


class Usuario(models.Model):
    """Representa a un usuario registrado."""

    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.nombre)
