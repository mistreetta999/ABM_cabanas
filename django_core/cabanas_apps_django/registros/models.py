from decimal import Decimal

"""Modelos para el registro de acciones del sistema."""
from django.db import models


class Registro(models.Model):
    """registros"""

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    class Meta:
        """Metadatos del modelo."""

        verbose_name = "Registro"
        verbose_name_plural = "Registros"
        ordering = ["-fecha"]

    def __str__(self):
        return f"{self.nombre} ({'Activo' if self.activo else 'Inactivo'})"


class ActividadCabana(models.Model):
    """actividades de las cabañas"""

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        """Metadatos del modelo."""

        verbose_name = "Actividad de Cabaña"
        verbose_name_plural = "Actividades de Cabañas"
        ordering = ["nombre"]

    def __str__(self):
        return str(self.nombre)
