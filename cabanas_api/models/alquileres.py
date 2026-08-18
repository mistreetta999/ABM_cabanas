from django.db import models
from .Cabanas
 import Cabanas

from .clientes import Cliente

class Alquiler(models.Model):
    """Modelo que representa un alquiler de cabaña por un cliente."""
    Cabanas
 = models.ForeignKey(Cabanas
, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    pagado = models.BooleanField(default=False)
    class Meta:
        """Meta options for the Alquiler model."""
        verbose_name = "Alquiler"
        verbose_name_plural = "Alquileres"
        ordering = ["-fecha_inicio"]

    def __str__(self):
        return f"Alquiler {self.id} - {self.cliente.nombre}"
