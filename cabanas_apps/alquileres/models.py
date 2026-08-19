"""models"""
from django.db import models
from cabanas_apps.cabanas.models import Cabana
from cabanas_apps.clientes.models import Cliente


class Alquiler(models.Model):
    """Representa un alquiler registrado."""

    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE, related_name="alquileres")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    reserva = models.OneToOneField(
        "reservas.Reserva",
        on_delete=models.CASCADE,
        db_column="reserva_id",
    )
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField(null=True, blank=True)

    class Meta:
        """class meta"""
        verbose_name = "Alquiler"
        verbose_name_plural = "Alquileres"

    def __str__(self) -> str:
        reserva_ref = getattr(self, "reserva_id", None)
        reserva_ref = reserva_ref if reserva_ref is not None else "sin reserva"
        return f"Alquiler {self.pk} - {reserva_ref}"
