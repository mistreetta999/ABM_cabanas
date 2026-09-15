from decimal import Decimal

from django.db import models

from django_core.cabanas_apps_django.alquileres.models import Alquiler
from django_core.cabanas_apps_django.cabanas.models import Cabana
from django_core.cabanas_apps_django.clientes.models import Cliente
from django_core.cabanas_apps_django.reservas.models import Reserva


class Factura(models.Model):
    numero = models.CharField(max_length=20)
    fecha_emision = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name="facturas_cliente"
    )
    cabana = models.ForeignKey(
        Cabana, on_delete=models.CASCADE, related_name="facturas_cabana"
    )
    reserva = models.ForeignKey(
        Reserva, on_delete=models.CASCADE, related_name="facturas_reserva"
    )
    alquiler = models.ForeignKey(
        Alquiler, on_delete=models.CASCADE, related_name="facturas_alquiler"
    )
    fecha_emision = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Factura {self.pk} - {self.cliente}"
