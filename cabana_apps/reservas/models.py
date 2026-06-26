from django.db import models
from cabana_apps.clientes_app.models import Cliente
from cabana_apps.cabanas_app.models import Cabana

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=20, default="pendiente")

    def __str__(self):
        return f"Reserva {self.id} - {self.cliente}"
