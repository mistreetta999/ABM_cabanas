from django.db import models

# Create your models here.
from django.db import models
from cabanas_apps.clientes.models import Cliente
from cabanas_apps.cabanas_app.models import Cabana

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=20, default="pendiente")

    def __str__(self):
        return f"Reserva {self.id} - {self.cliente}"

class Alquiler(models.Model):
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Alquiler {self.id} - {self.reserva}"
