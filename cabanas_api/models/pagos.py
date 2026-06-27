from django.db import models
from cabanas_apps.clientes.models import Cliente
from cabanas_apps.alquileres.models import Alquiler

class Pago(models.Model):
    METODO_CHOICES = [
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
        ('transferencia', 'Transferencia'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="pagos")
    alquiler = models.ForeignKey(Alquiler, on_delete=models.CASCADE, related_name="pagos")
    fecha_pago = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(max_length=20, choices=METODO_CHOICES)

    def __str__(self):
        return f"Pago {self.id} - {self.cliente} - {self.monto}"
