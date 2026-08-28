"""
Funciones auxiliares para la gestión de registros.
Este archivo sirve como capa de servicios/handlers para la app Registros.
"""

from django.contrib.auth.models import User
from clientes.models import Cliente
from facturas.models import Factura
from reservas.models import Reserva
from alquileres.models import Alquiler
from .models import Registro


def crear_registro(tipo: str, descripcion: str, usuario: User = None,
                   cliente: Cliente = None, factura: Factura = None,
                   reserva: Reserva = None, alquiler: Alquiler = None) -> Registro:
    """
    Crea un registro en el sistema con los datos proporcionados.
    """
    registro = Registro.objects.create(
        usuario=usuario,
        cliente=cliente,
        factura=factura,
        reserva=reserva,
        alquiler=alquiler,
        tipo=tipo,
        descripcion=descripcion
    )
    return registro


def obtener_registros_usuario(usuario_id: int):
    """
    Devuelve todos los registros asociados a un usuario.
    """
    return Registro.objects.filter(usuario_id=usuario_id).order_by("-fecha")


def obtener_registros_cliente(cliente_id: int):
    """
    Devuelve todos los registros asociados a un cliente.
    """
    return Registro.objects.filter(cliente_id=cliente_id).order_by("-fecha")


def resumen_registros(limit: int = 10) -> list:
    """
    Devuelve un resumen de los últimos registros del sistema.
    """
    registros = Registro.objects.all().order_by("-fecha")[:limit]
    return [r.resumen() for r in registros]
