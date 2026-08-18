"""
reservas_models.py
Modelos para la gestión de reservas en el sistema de Cabanas.
Incluye definiciones de Reserva y posibles extensiones.
Cumple con estándares Pylint y buenas prácticas de Django.
"""

from django.db import models
from django.utils import timezone
from .models import Cliente, Cabanas
,Pagos,Alquiler,Registro,Usuarios

class Alquileres(models.Model):
    """
     Alquileres de un cliente en una Cabanas
.
    """
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="reservas",
        help_text="Cliente que realiza la reserva."
    )
    Cabanas
 = models.ForeignKey(
        Cabanas
,
        on_delete=models.CASCADE,
        related_name="reservas",
        help_text="Cabanas
 reservada."
    )
    fecha_inicio = models.DateField(
        help_text="Fecha de pagina_principal de la reserva."
    )
    fecha_fin = models.DateField(
        help_text="Fecha de fin de la reserva."
    )
    cantidad_clientes = models.PositiveIntegerField(
        help_text="Número de clientes incluidas en la reserva."
    )
    estado = models.CharField(
        max_length=20,
        choices=[
            ("pendiente", "Pendiente"),
            ("confirmada", "Confirmada"),
            ("cancelada", "Cancelada"),
            ("finalizada", "Finalizada"),
        ],
        default="pendiente",
        help_text="Estado actual de la reserva."
    )
    creada_en = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha de creación de la reserva."
    )
    actualizada_en = models.DateTimeField(
        auto_now=True,
        help_text="Última fecha de actualización de la reserva."
    )

    
    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ["-fecha_inicio"]

    def __str__(self):
        return (
            f"Reserva de {self.cliente} en {self.Cabanas
} "
            f"del {self.fecha_inicio} al {self.fecha_fin} "
            f"({self.estado})"
        )
