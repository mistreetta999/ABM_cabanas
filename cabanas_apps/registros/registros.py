""" archivo de registros de actividad   """
from django.db import models
class Registos:
    """ class registros"""
    def __init__(self, usuario, accion, detalle=None):
        self.usuario = usuario
        self.accion = accion
        self.detalle = detalle

class RegistroActividad(models.Model):
    """ class registro de actividad"""
    usuario = models.CharField(max_length=100)
    accion = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
    detalle = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name = "Registro de Actividad"
        verbose_name_plural = "Registros de Actividad"
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.usuario} - {self.accion} ({self.fecha})"
