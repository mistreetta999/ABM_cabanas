"""
Servicio de gestión de reservas.
Encapsula la lógica de negocio en una clase para mayor organización.
"""

from django.core.exceptions import ValidationError
from datetime import date
from .models import Reserva
from cabanas.models import Cabana
from clientes.models import Cliente


class ReservaService:
    """Clase que centraliza la lógica de gestión de reservas."""

    @staticmethod
    def crear(cliente_id: int, cabana_id: int, fecha_inicio: date, fecha_fin: date, monto_total: float) -> Reserva:
        """Crea una reserva validando disponibilidad y fechas."""
        if fecha_fin < fecha_inicio:
            raise ValidationError("La fecha de fin debe ser posterior a la fecha de inicio.")

        cabana = Cabana.objects.get(pk=cabana_id)

        # Validar solapamiento de reservas
        solapadas = Reserva.objects.filter(
            cabana=cabana,
            fecha_inicio__lte=fecha_fin,
            fecha_fin__gte=fecha_inicio
        ).exclude(estado="cancelada")

        if solapadas.exists():
            raise ValidationError("La cabaña no está disponible en el rango solicitado.")

        cliente = Cliente.objects.get(pk=cliente_id)

        reserva = Reserva.objects.create(
            cliente=cliente,
            cabana=cabana,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            monto_total=monto_total,
            estado="pendiente"
        )
        return reserva

    @staticmethod
    def obtener_por_cliente(cliente_id: int):
        """Devuelve todas las reservas realizadas por un cliente."""
        return Reserva.objects.filter(cliente_id=cliente_id).order_by("-fecha_creacion")

    @staticmethod
    def obtener_por_cabana(cabana_id: int):
        """Devuelve todas las reservas asociadas a una cabaña."""
        return Reserva.objects.filter(cabana_id=cabana_id).order_by("-fecha_creacion")

    @staticmethod
    def confirmar(reserva_id: int) -> Reserva:
        """Confirma una reserva existente."""
        reserva = Reserva.objects.get(pk=reserva_id)
        reserva.confirmar()
        return reserva

    @staticmethod
    def cancelar(reserva_id: int) -> Reserva:
        """Cancela una reserva existente."""
        reserva = Reserva.objects.get(pk=reserva_id)
        reserva.cancelar()
        return reserva

    @staticmethod
    def finalizar(reserva_id: int) -> Reserva:
        """Finaliza una reserva existente."""
        reserva = Reserva.objects.get(pk=reserva_id)
        reserva.finalizar()
        return reserva
