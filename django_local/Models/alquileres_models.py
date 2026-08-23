""" alquileres models"""
from django.db import models
from .clientes_models import Cliente


class Alquiler(models.Model):
    """Modelo de Alquiler de cabañas."""

    id = models.AutoField(primary_key=True)
    cabana = models.ForeignKey("Models.Cabana", on_delete=models.CASCADE, related_name="alquileres")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="alquileres")
    reserva = models.OneToOneField("Models.Reserva", on_delete=models.CASCADE, related_name="alquiler")
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField(null=True, blank=True)

    class Meta:
        """ class meta nombres"""
        verbose_name = "Alquiler"
        verbose_name_plural = "Alquileres"

    def __str__(self):
        return f"Alquiler {self.id} - {self.cliente} ({self.cabana})"

    def actualizar(self, **datos):
        """Actualiza la instancia actual con datos nuevos."""
        for campo, valor in datos.items():
            setattr(self, campo, valor)
        self.save(update_fields=list(datos.keys()) if datos else None)
        return self

    def eliminar(self):
        """Elimina la instancia actual."""
        return self.delete()
