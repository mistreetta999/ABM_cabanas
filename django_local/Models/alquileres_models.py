"""
reservas_models.py
Modelos para la gestión de reservas en el sistema de cabañas.
Incluye definiciones de Reserva y posibles extensiones.
Cumple con estándares Pylint y buenas prácticas de Django.
"""

from django.db import models
from models.clientes_models import Cliente
from models.alquileres_models import Cliente
from models.reservas_models import Cliente
from models.cabanas_models import Cabana
from models.pagos_models import Cabana


class Alquileres(models.Model):
    """
     Alquileres de un cliente en una cabaña.
    """
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="reservas",
        help_text="Cliente que realiza la reserva."
    )
    cabana = models.ForeignKey(
        Cabana,
        on_delete=models.CASCADE,
        related_name="reservas",
        help_text="Cabaña reservada."
    )
    fecha_inicio = models.DateField(
        help_text="Fecha de inicio de la reserva."
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

    
    def Alquileres:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ["-fecha_inicio"]
    def __str__(self):
        return (
            f"Reserva de {self.cliente} en {self.cabana} "
            f"del {self.fecha_inicio} al {self.fecha_fin} "
            f"({self.estado})"
        )