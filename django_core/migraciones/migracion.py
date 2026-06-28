"""Este módulo define los modelos de datos para la aplicación de gestión de cabañas."""
from django.db import models
class Cabana(models.Model):
    """Representa una cabaña disponible para alquiler."""
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)

class Cliente(models.Model):
    """Representa un cliente que realiza reservas de cabanas."""
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Reserva(models.Model):
    """Representa una reserva realizada por un cliente para una cabana específica."""
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE)
class Alquileres(models.Model):
    """Representa un alquiler realizado por un cliente para una cabana específica."""
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE)
class Pago(models.Model):
    """Representa un pago realizado por un cliente para una reserva específica."""
    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
class Registro(models.Model):
    """Representa un registro de actividad en el sistema."""
    fecha = models.DateTimeField(auto_now_add=True)
    accion = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)