""" models de cabanas"""
from django.db import models

class Cabana(models.Model):
    """class cabana"""
    nombre = models.CharField(max_length=100, unique=True)
    capacidad = models.PositiveIntegerField()
    descripcion = models.TextField(blank=True, null=True)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    class Meta:
        """class meta"""
        verbose_name = "Cabaña"
        verbose_name_plural = "Cabañas"

    def __str__(self) -> str:
        return str(self.nombre)


class Cliente(models.Model):
    """ class cliente"""
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        """class meta"""
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["apellido"]

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Reserva(models.Model):
    """class reserva"""
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="reservas")
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE, related_name="reservas")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cantidad_personas = models.PositiveIntegerField(default=1)
    pagada = models.BooleanField(default=False)

    class Meta:
        """class meta"""
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ["fecha_inicio"]

    def __str__(self):
        return f"Reserva de {self.cliente} en {self.cabana}"
