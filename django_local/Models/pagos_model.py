"""models de pago"""
from django.db import models
from .facturas_models import Factura

class Pago(models.Model):
    """Modelo de Pago asociado a una Factura."""

    id = models.AutoField(primary_key=True)
    fecha_pago = models.DateField(auto_now_add=True)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(
        max_length=20,
        choices=[
            ("efectivo", "Efectivo"),
            ("tarjeta", "Tarjeta"),
            ("transferencia", "Transferencia"),
        ],
    )
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name="pagos")

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"

    def __str__(self):
        return f"Pago {self.id} - {self.metodo} - {self.monto_total}"

    def actualizar(self, **datos):
        """Actualiza la instancia actual con datos nuevos."""
        for campo, valor in datos.items():
            setattr(self, campo, valor)
        self.save(update_fields=list(datos.keys()) if datos else None)
        return self

    def eliminar(self):
        """Elimina la instancia actual."""
        return self.delete()
