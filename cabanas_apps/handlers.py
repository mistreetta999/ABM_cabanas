"""
Módulo de handlers generales para la gestión de cabañas.
Centraliza funciones comunes entre las distintas apps.
"""

from reservas.models import Reserva
from pagos.models import Pago
from facturas.models import Factura
from registros.models import Registro


class ReservaHandler:
    """Handler para operaciones relacionadas con reservas."""

    @staticmethod
    def confirmar_reserva(reserva: Reserva, usuario=None):
        reserva.confirmar()
        Registro.objects.create(
            usuario=usuario,
            reserva=reserva,
            tipo="reserva",
            descripcion=f"Reserva #{reserva.id} confirmada."
        )
        return reserva

    @staticmethod
    def cancelar_reserva(reserva: Reserva, usuario=None):
        reserva.cancelar()
        Registro.objects.create(
            usuario=usuario,
            reserva=reserva,
            tipo="reserva",
            descripcion=f"Reserva #{reserva.id} cancelada."
        )
        return reserva


class PagoHandler:
    """Handler para operaciones relacionadas con pagos."""

    @staticmethod
    def registrar_pago(pago: Pago, usuario=None):
        pago.marcar_factura_pagada()
        Registro.objects.create(
            usuario=usuario,
            factura=pago.factura,
            tipo="pago",
            descripcion=f"Pago #{pago.id} registrado por {pago.monto}."
        )
        return pago


class FacturaHandler:
    """Handler para operaciones relacionadas con facturas."""

    @staticmethod
    def generar_factura(reserva: Reserva, monto: float, usuario=None):
        factura = Factura.objects.create(
            cliente=reserva.cliente,
            reserva=reserva,
            monto=monto,
            estado="pendiente"
        )
        Registro.objects.create(
            usuario=usuario,
            factura=factura,
            tipo="factura",
            descripcion=f"Factura #{factura.id} generada para reserva #{reserva.id}."
        )
        return factura
