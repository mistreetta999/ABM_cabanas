"""
Handlers de la aplicación Cabañas.
Contiene funciones auxiliares y lógica de negocio para integrarse con el sistema.
"""

from django.core.exceptions import ValidationError
from .models import Cabana
from reservas.models import Reserva


def crear_cabana(nombre: str, capacidad: int, precio_base: float, descripcion: str = "") -> Cabana:
    """
    Crea una nueva cabaña en el sistema.
    """
    if capacidad <= 0:
        raise ValidationError("La capacidad de la cabaña debe ser mayor a cero.")
    if precio_base <= 0:
        raise ValidationError("El precio base debe ser mayor a cero.")

    cabana = Cabana.objects.create(
        nombre=nombre,
        capacidad=capacidad,
        precio_base=precio_base,
        descripcion=descripcion,
        estado="disponible",
    )
    return cabana


def validar_disponibilidad(cabana_id: int, fecha_inicio, fecha_fin) -> bool:
    """
    Verifica si una cabaña está disponible en un rango de fechas.
    """
    reservas = Reserva.objects.filter(cabana_id=cabana_id, estado="activa")
    for reserva in reservas:
        if not (fecha_fin <= reserva.fecha_inicio or fecha_inicio >= reserva.fecha_fin):
            return False
    return True


def cambiar_estado_cabana(cabana_id: int, nuevo_estado: str) -> None:
    """
    Cambia el estado de una cabaña (disponible, ocupada, mantenimiento).
    """
    estados_validos = ["disponible", "ocupada", "mantenimiento"]
    if nuevo_estado not in estados_validos:
        raise ValidationError("El estado de la cabaña no es válido.")

    cabana = Cabana.objects.get(pk=cabana_id)
    cabana.estado = nuevo_estado
    cabana.save()
