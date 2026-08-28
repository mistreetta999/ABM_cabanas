"""
Modelos de la aplicación Facturas.
Integrados con Clientes, Reservas, Cabañas y Pagos.
"""

from django.db import models
from django.utils import timezone
from clientes.models import Cliente
from reservas.models import Reserva
from cabanas.models import Cabana
from pagos.models import Pago


class Factura(models.Model):
    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("pagada", "Pagada"),
        ("vencida", "Vencida"),
        ("cancelada", "Cancelada"),
    ]

    numero = models.CharField(max_length=20, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="facturas")
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE, related_name="facturas")
    reserva = models.ForeignKey(Reserva, on_delete=models.SET_NULL, null=True, blank=True, related_name="facturas")
    fecha_emision = models.DateField(default=timezone.now)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=10, choices=ESTADOS, default="pendiente")

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
        ordering = ["-fecha_emision"]

    def __str__(self):
        return f"Factura {self.numero} - Cliente: {self.cliente} - Estado: {self.estado}"

    def marcar_pagada(self):
        """Marca la factura como pagada si tiene pagos suficientes."""
        total_pagado = sum(p.m