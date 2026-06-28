"""reservas models"""
from django.db import models
from .cabana import Cabana
from .clientes import Cliente

class Reserva(models.Model):
    """ class reserva"""
    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("confirmada", "Confirmada"),
        ("cancelada", "Cancelada"),
    ]
    id = models.AutoField(primary_key=True)
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default="pendiente")
    def __str__(self):
        return f"Reserva {self.id} - {self.cliente}"
