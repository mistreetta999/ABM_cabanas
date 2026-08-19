""" Modelos principales para la gestión de cabañas """

from django.db import models


class Cabana(models.Model):
    """ class cabanas"""
    nombre = models.CharField(max_length=100, unique=True)
    capacidad = models.IntegerField()
    descripcion = models.TextField(blank=True)
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    """ class clientes"""
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Reserva(models.Model):
    """ class reservas"""
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return f