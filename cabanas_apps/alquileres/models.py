"""clientes models"""
from logging import getLogger
from django.db import models
from cabanas_apps.cabanas.models import Cabana
from cabanas_apps.clientes.models import Cliente   # importa el modelo Cliente desde su app
from cabanas_apps.reservas.models import Reserva   # importa Reserva si está en otra app

LOGGER = getLogger(__name__)

class Alquiler(models.Model):
    """Modelo Alquiler"""
    id = models.AutoField(primary_key=True)
    cabanas = models.ForeignKey(Cabana, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    reservas = models.OneToOneField(Reserva, on_delete=models.CASCADE)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField(null=True, blank=True)

    class Meta:
        """ class Meta para definir el nombre del modelo en singular y plural. """
        verbose_name = "Alquiler"
        verbose_name_plural = "Alquileres"

    def __str__(self) -> str:
        return f"Alquiler {self.id} - {self.reservas}"
