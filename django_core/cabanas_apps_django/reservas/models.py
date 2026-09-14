from decimal import Decimal
"""Modelos para la aplicación de reservas."""

from django.db import models
from django_core.cabanas_apps_django.clientes.models import Cliente
from django_core.cabanas_apps_django.cabanas.models import Cabana


class EstadoReserva(models.TextChoices):
    """Opciones de estado para una reserva."""
    PENDIENTE = "pendiente", "Pendiente"
    CONFIRMADA = "confirmada", "Confirmada"
    CANCELADA = "cancelada", "Cancelada"

    @classmethod
    def default(cls):
        """Devuelve el estado por defecto para una reserva."""
        return cls.PENDIENTE


class Reserva(models.Model):
    """Modelo que representa una reserva de cabaña por un cliente."""
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(
        max_length=20,
        choices=EstadoReserva.choices,
        default=EstadoReserva.PENDIENTE,
    )

    class Meta:
        """Metadatos para el modelo Reserva."""
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return f"Reserva de {self.cliente} en {self.cabana}"

