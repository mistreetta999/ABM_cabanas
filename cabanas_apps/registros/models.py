"""Modelos para la aplicación de registros."""

from django.db import models

from cabanas_apps.cabanas.models import Cabana
from cabanas_apps.clientes.models import Cliente


class ActividadCabanas(models.Model):
    """ esta class representa una actividad realizada en una Cabana por un cliente."""
    id = models.AutoField(primary_key=True)
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Metadatos del modelo ActividadCabanas."""
        verbose_name = "Actividad de Cabaña"
        verbose_name_plural = "Actividades de Cabañas"
        ordering = ["-fecha"]

    def __str__(self):
        return f"{self.cabana} - {str(self.descripcion)[:30]}"
