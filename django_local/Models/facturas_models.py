from django.db import models
from .alquileres_models import Alquiler
from .reservas_models import Reserva

class Factura(models.Model):
    """Modelo de Factura asociada a un Alquiler o Reserva."""

    id = models.AutoField(primary_key=True)
    fecha_emision = models.DateField(auto_now_add=True)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    pagada = models.BooleanField(default=False)

    # Relaciones
    alquiler = models.OneToOneField(
        Alquiler,
        on_delete=models.CASCADE,
        related_name="factura_alquiler",
        null=True,
        blank=True
    )
    reserva = models.OneToOneField(
        Reserva,
        on_delete=models.CASCADE,
        related_name="factura_reserva",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"

    def __str__(self):
        return f"Factura {self.id} - Total: {self.monto_total} - Pagada: {self.pagada}"

    def marcar_pagada(self):
        """Marca la factura como pagada."""
        self.pagada = True
        self.save(update_fields=["pagada"])
        return self

    def actualizar(self, **datos):
        """Actualiza la instancia actual con datos nuevos."""
        for campo, valor in datos.items():
            setattr(self, campo, valor