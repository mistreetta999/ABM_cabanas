"""archivio models.py para la app alquileres"""

from django.db import models
from cabanas_apps.cabanas.models import Cabanas

from cabanas_apps.clientes.models import Cliente
from cabanas_apps.reservas.models import Reserva



class Alquiler(models.Model):
    """class Alquiler models"""
    id = models.AutoField(primary_key=True)
    cabanas = models.ForeignKey(Cabanas
, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField(null=True, blank=True)
    fecha_imprimir = models.DateField(null=True, blank=True)
    class Meta:
        verbose_name = "Alquiler"

    def __str__(self):
        return f"Alquiler {self.id} - {self.reserva}"

class AlquilerCrear(models.Model):
    """class Alquiler models"""
    id = models.AutoField(primary_key=True)
    cabanas = models.ForeignKey(Cabanas
, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return f"Alquiler {self.id} - {self.reserva}"

class AlquilerEditar(models.Model):
    """class Alquiler models"""
    id = models.AutoField(primary_key=True)
    cabanas = models.ForeignKey(Cabanas
, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField(null=True, blank=True)
    fecha_imprimir = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return f"Alquiler {self.id} - {self.reserva}"
    
class AlquilerBorrar(models.Model):
    """class Alquiler models"""
    id = models.AutoField(primary_key=True)
    cabanas = models.ForeignKey(Cabanas
, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return f"Alquiler {self.id} - {self.reserva}"

class AlquilerImprimir(models.Model):
    """class Alquiler models"""
    id = models.AutoField(primary_key=True)
    cabanas = models.ForeignKey(Cabanas
, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return f"Alquiler {self.id} - {self.reserva}"