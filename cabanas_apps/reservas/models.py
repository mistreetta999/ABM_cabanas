"""
Modelos de la aplicación Reservas.
"""

from django.db import models
from django.core.validators import MinValueValidator
from clientes.models import Cliente
from cabanas.models import Cabana


class Reserva(models.Model):
    """Modelo que representa una reserva de cabaña."""

    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("confirmada", "Confirmada"),
        ("cancelada", "Cancelada"),
        ("finalizada", "Finalizada"),
    ]

    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="reservas")
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE, related_name="reservas")
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de fin")
    estado = models.CharField(max_length=20, choices=ESTADOS, default="pendiente", verbose_name="Estado de la reserva")
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)], verbose_name="Monto total")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return f"Reserva #{self.id} - {self.cliente} - {self.cabana}"

    def duracion(self) -> int:
        """Devuelve la cantidad de días de la reserva."""
        return (self.fecha_fin - self.fecha_inicio).days

    def confirmar(self):
        """Confirma la reserva cambiando su estado."""
        self.estado = "confirmada"
        self.save(update_fields=["estado"])

    def cancelar(self):
        """Cancela la reserva cambiando su estado."""
        self.estado = "cancelada"
        self.save(update_fields=["estado"])

    def finalizar(self):
        """Finaliza la reserva cambiando su estado."""
        self.estado = "finalizada"
        self.save(update_fields=["estado"])
