from decimal import Decimal

"""Modelos de la app pagos."""
from django.db import models

from django_core.cabanas_apps_django.alquileres.models import Alquiler


class Pago(models.Model):
    """Modelo que representa un pago."""

    fecha = models.DateField()
    forma = models.CharField(max_length=50)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    alquiler = models.ForeignKey(
        Alquiler, on_delete=models.CASCADE, related_name="pagos_alquiler"
    )
    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pago {self.pk} - {self.alquiler}"
