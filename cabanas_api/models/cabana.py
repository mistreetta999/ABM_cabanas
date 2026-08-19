"""Modelo de Cabanas
 para cabanas_api."""
from django.db import models

class CabanaInformacion(models.Model):
    """class cabana informacion"""
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    capacidad = models.PositiveIntegerField(default=2)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        """ class meta"""
        db_table = "Cabanas"
        verbose_name = "Cabana"
        verbose_name_plural = "Cabanas"

    def __str__(self):
        return f"{self.nombre} (Capacidad: {self.capacidad})"

    def precio_total(self, noches: int) -> float:
        """Calcula el precio total según la cantidad de noches."""
        return float(self.precio_base) * noches
