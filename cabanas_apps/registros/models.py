"""
Modelos de la aplicación Registros.
Permite almacenar eventos y acciones realizadas en el sistema.
"""

from django.db import models
from django.contrib.auth.models import User
from clientes.models import Cliente
from facturas.models import Factura
from reservas.models import Reserva
from alquileres.models import Alquiler


class Registro(models.Model):
    """Modelo que representa un registro de actividad en el sistema."""

    TIPOS = [
        ("creacion", "Creación"),
        ("actualizacion", "Actualización"),
        ("eliminacion", "Eliminación"),
        ("pago", "Pago"),
        ("reserva", "Reserva"),
        ("alquiler", "Alquiler"),
        ("factura", "Factura"),
        ("login", "Inicio de sesión"),
        ("logout", "Cierre de sesión"),
    ]

    id = models.AutoField(primary_key=True)
    usuario = models