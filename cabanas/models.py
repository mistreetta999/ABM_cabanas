""" Modelos de la app cabanas """
from django.db import models


class Cabana(models.Model):
    """ Modelo que representa una cabaña """
    id = models.AutoField(primary_key=True)  # clave primaria automática
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        """Metadatos del modelo"""
        db_table = "cabanas"
        verbose_name = "Cabana"
        verbose_name_plural = "Cabanas"

    def __str__(self):
        return str(self.nombre)
    