from django.db import models
from .reservas import Reserva
from .clientes_models import Cliente

class Registro(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    detalle = models.TextField()

    def __str__(self):
        return f"Registro {self.id} - {self.cliente.nombre}"
