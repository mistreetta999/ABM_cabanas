"""Modelos para la aplicación de registros."""

from django.db import models

from cabanas_apps.models import Cabana, Cliente


class ActividadCabanas(models.Model):
    """ esta class representa una actividad realizada en una Cabana por un cliente."""
    id = models.AutoField(primary_key=True)
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cabana} - {str(self.descripcion)[:30]}"
