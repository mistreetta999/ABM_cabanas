"""
Handlers de la aplicación Interfaz de Gestión de Cabañas.
Contiene funciones auxiliares para interactuar con la capa de gestión.
"""

from django.core.exceptions import ValidationError
from cabanas.models import Cabana
from gestion_cabanas.views import cambiar_estado_cabana
from reservas.models import Reserva


def obtener_cabanas_disponibles():
    """
    Devuelve todas las cabañas que están en estado 'disponible'.
    """
    return Cabana.objects.filter(estado="disponible")


def obtener_reservas_cabana(cabana_id: int):
    """
    Devuelve todas las reservas asociadas a una cabaña específica.
    """
    return Reserva.objects.filter(cabana_id=cabana_id).order_by("-fecha_inicio")


def actualizar_estado_cabana(cabana_id: int, nuevo_estado: str):
    """
    Actualiza el estado de una cabaña usando la lógica de gestión.
    """
    estados_validos = ["disponible", "ocupada", "mantenimiento"]
    if nuevo_estado not in estados_validos:
        raise ValidationError("El estado de la cabaña no es válido.")

    return cambiar_estado_cabana(None, cabana_id, nuevo_estado)


def resumen_cabana(cabana_id: int) -> dict:
    """
    Devuelve un resumen con datos clave de una cabaña.
    """
    cabana = Cabana.objects.get(pk=cabana_id)
    reservas = obtener_reservas_cabana(cabana_id)

    return {
        "nombre": cabana.nombre,
        "capacidad": cabana.capacidad,
        "precio_base": cabana.precio_base,
        "estado": cabana.estado,
        "reservas_activas": reservas.count(),
    }
