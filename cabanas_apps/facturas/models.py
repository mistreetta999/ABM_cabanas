"""
Modelos de la aplicación Facturas.
"""

from django.db import models
from django.core.validators import MinValueValidator
from clientes.models import Cliente
from reservas.models import Reserva
from alquileres.models import Alquiler


class Factura(models.Model):
    """Modelo que representa una factura emitida en el sistema."""

    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("pagada", "Pagada"),
        ("vencida", "Vencida"),
        ("cancelada", "Cancelada"),
    ]

    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="facturas")
    reserva = models.ForeignKey(Reserva, on_delete=models.SET_NULL, null=True, blank=True, related_name="facturas")
    alquiler = models.ForeignKey(Alquiler, on_delete=models.SET_NULL, null=True, blank=True, related_name="facturas")
    fecha_emision = models.DateField(auto_now_add=True, verbose_name="Fecha de emisión")
    fecha_vencimiento = models.DateField(verbose_name="Fecha de vencimiento")
    monto = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)], verbose_name="Monto total")
    estado = models.CharField(max_length=20, choices=ESTADOS, default="pendiente", verbose_name="Estado")

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
        ordering = ["-fecha_emision"]

    def __str__(self):
        return f"Factura #{self.id} - Cliente: {self.cliente.nombre_completo()} - Estado: {self.estado}"

    def marcar_como_pagada(self):
        """Marca la factura como pagada."""
        self.estado = "pagada"
        self.save(update_fields=["estado"])

    def marcar_como_vencida(self):
        """Marca la factura como vencida."""
        self.estado = "vencida"
        self.save(update_fields=["estado"])

    def cancelar(self):
        """Cancela la factura."""
        self.estado = "cancelada"
        self.save(update_fields=["estado"])
