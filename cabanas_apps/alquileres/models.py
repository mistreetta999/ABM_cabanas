from django.db import models
from cabanas_apps.cabanas.models import Cabana
from cabanas_apps.reservas.models import Reserva
from cabanas_apps.clientes import Cliente
from cabanas_apps.clientes.models import Cliente

class Alquiler(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = models.AutoField(primary_key=True)
        self.cabanas = models.ForeignKey(Cabana, on_delete=models.CASCADE)
        self.cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
        self.reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE)
        self.monto_total = models.DecimalField(max_digits=10, decimal_places=2)
        self.fecha_pago = models.DateField(null=True, blank=True)
    def Alquiler(self, cabanas, cliente, reserva, monto_total, fecha_pago)->Any:
        id=models.AutoField(primary_key=True)
        cabanas=models.ForeignKey(Cabana, on_delete=models.CASCADE)
        cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
        reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE)
        monto_total = models.DecimalField(max_digits=10, decimal_places=2)
        fecha_pago = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Alquiler {self.id} - {self.reserva}"
