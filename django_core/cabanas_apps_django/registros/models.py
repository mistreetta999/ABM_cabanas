from django.db import models
from django.contrib.auth.models import User

class Registro(models.Model):
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
        return f"{self.get_accion_display()} - {self.fecha.strftime('%d/%m/%Y %H:%M')}"

    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"
        ordering = ['-fecha']
