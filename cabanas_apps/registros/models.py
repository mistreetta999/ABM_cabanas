""" registros/models"""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Registro(models.Model):
    """ Modelo para registrar acciones en el sistema de gestión de cabañas."""
    ACCIONES = [
        ('RESERVA', 'Reserva creada'),
        ('PAGO', 'Pago registrado'),
        ('CLIENTE', 'Cliente actualizado'),
        ('CABAÑA', 'Cabaña modificada'),
        ('OTRO', 'Otra acción'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    accion = models.CharField(max_length=20, choices=ACCIONES)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.accion} - {self.fecha.strftime('%d/%m/%Y %H:%M') if self.fecha else 'N/A'}"

    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"
        ordering = ['-fecha']
