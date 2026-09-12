""" models"""
from django.db import models


class Cliente(models.Model):
    """Representa a un cliente que realiza alquileres."""

    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.dni})"


class Alojamiento(models.Model):
    """Representa un alojamiento disponible para alquiler."""

    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    capacidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        """Metadatos del modelo Alojamiento."""
        verbose_name = "Alojamiento"
        verbose_name_plural = "Alojamientos"

    def __str__(self):
        return f"{self.nombre} - {self.direccion}"


class Alquiler(models.Model):
    """ alquileres"""
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="alquileres")
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(
        max_length=20,
        choices=[
            ("reservado", "Reservado"),
            ("ocupado", "Ocupado"),
            ("finalizado", "Finalizado"),
            ("cancelado", "Cancelado"),
        ],
        default="reservado"
    )

    class Meta:
        """Metadatos del modelo Alquiler."""
        verbose_name = "Alquiler"
        verbose_name_plural = "Alquileres"

    def __str__(self):
        return f"{self.cliente} -  ({self.fecha_ingreso} → {self.fecha_salida})"
