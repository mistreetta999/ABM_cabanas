"""
Handlers para la aplicación Public.
Centralizan funciones de la web pública: disponibilidad, reservas y contacto.
"""

from cabanas_apps_django. cabanas.models import Cabana
from cabanas_apps_django.reservas.models import Reserva
from cabanas_apps_django.clientes.models import Cliente
from django.core.exceptions import ValidationError
from datetime import date


class PublicReservaHandler:
    """Handler para operaciones de reservas desde la web pública."""

    @staticmethod
    def verificar_disponibilidad(cabana_id: int, inicio: date, fin: date) -> bool:
        """
        Verifica si una cabaña está disponible en el rango de fechas.
        """
        reservas = Reserva.objects.filter(cabana_id=cabana_id, estado__in=["pendiente", "confirmada"])
        for r in reservas:
            if not (fin <= r.fecha_inicio or inicio >= r.fecha_fin):
                return False
        return True

    @staticmethod
    def crear_reserva(cliente: Cliente, cabana: Cabana, inicio: date, fin: date, monto: float) -> Reserva:
        """
        Crea una reserva pública validando disponibilidad.
        """
        if fin <= inicio:
            raise ValidationError("La fecha de fin debe ser posterior a la fecha de inicio.")
        if not PublicReservaHandler.verificar_disponibilidad(cabana.id, inicio, fin):
            raise ValidationError("La cabaña no está disponible en el rango solicitado.")

        reserva = Reserva.objects.create(
            cliente=cliente,
            cabana=cabana,
            fecha_inicio=inicio,
            fecha_fin=fin,
            monto_total=monto,
            estado="pendiente"
        )
        return reserva


class PublicContactoHandler:
    """Handler para mensajes de contacto desde la web pública."""

    @staticmethod
    def enviar_mensaje(nombre: str, email: str, mensaje: str) -> dict:
        """
        Simula el envío de un mensaje de contacto.
        En un sistema real, aquí se integraría con email o CRM.
        """
        return {
            "status": "ok",
            "detalle": f"Mensaje recibido de {nombre} ({email})",
            "contenido": mensaje
        }
