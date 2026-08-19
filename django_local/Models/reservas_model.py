from django.db import models
from .clientes_models import Cliente
from .cabanas_models import Cabana

class Reserva(models.Model):
    """Modelo de Reserva de cabañas."""

    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="reservas")
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE, related_name="reservas")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cantidad_personas = models.PositiveIntegerField(default=1)
    pagada = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ["fecha_inicio"]

    def __str__(self):
        return f"Reserva {self.id} - {self.cliente} en {self.cabana}"

    def confirmar_pago(self):
        """Marca la reserva como pagada."""
        self.pagada = True
        self.save(update_fields=["pagada"])
        return self

    def actualizar(self, **datos):
        """Actualiza la instancia actual con datos nuevos."""
        for campo, valor in datos.items():
            setattr(self, campo, valor)
        self.save(update_fields=list(datos.keys()) if datos else None)
        return self

    def eliminar(self):
        """Elimina la instancia actual."""
        return self.delete()
