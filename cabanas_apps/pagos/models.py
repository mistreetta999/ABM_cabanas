"""
Modelos de la aplicación Pagos.
"""

from django.db import models
from django.core.validators import MinValueValidator
from facturas.models import Factura
from clientes.models import Cliente


class Pago(models.Model):
    """Modelo que representa un pago realizado por un cliente."""

    METODOS = [
        ("efectivo", "Efectivo"),
        ("tarjeta", "Tarjeta de crédito/débito"),
        ("transferencia", "Transferencia bancaria"),
        ("mercadopago", "MercadoPago"),
    ]

    id = models.AutoField(primary_key=True)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name="pagos")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="pagos")
    fecha_pago = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de pago")
    monto = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        verbose_name="Monto pagado"
    )
    metodo = models.CharField(
        max_length=20,
        choices=METODOS,
        default="efectivo",
        verbose_name="Método de pago"
    )
    referencia = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Referencia/Comprobante"
    )

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
        ordering = ["-fecha_pago"]

    def __str__(self):
        return f"Pago #{self.id} - Factura {self.factura.id} - Cliente {self.cliente.nombre_completo()}"

    def marcar_factura_pagada(self):
        """Marca la factura asociada como pagada si el monto cubre el total."""
        if self.monto >= self.factura.monto:
            self.factura.marcar_como_pagada()
