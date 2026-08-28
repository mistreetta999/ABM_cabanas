"""
Handlers generales para la instancia django_local.
Centraliza funciones comunes entre las distintas apps locales.
"""

from reservas.models import Reserva
from clientes.models import Cliente
from facturas.models import Factura
from pagos.models import Pago
from registros.models import Registro


class ClienteHandler:
    """Handler para operaciones relacionadas con clientes."""

    @staticmethod
    def crear_cliente(nombre: str, apellido: str, email: str) -> Cliente:
        cliente = Cliente.objects.create(nombre=nombre, apellido=apellido, email=email)
        Registro.objects.create(
            tipo="cliente",
            descripcion=f"Cliente {cliente.nombre} {cliente.apellido} creado."
        )
        return cliente


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
