"""
Funciones auxiliares para la gestión de pagos.
Este archivo sirve como capa de servicios/handlers para la app Pagos.
"""

from django.core.exceptions import ValidationError
from facturas.models import Factura
from clientes.models import Cliente
from .models import Pago


def registrar_pago(cliente_id: int, factura_id: int, monto: float, metodo: str, referencia: str = None) -> Pago:
    """
    Registra un pago en el sistema y actualiza el estado de la factura si corresponde.
    """
    cliente = Cliente.objects.get(pk=cliente_id)
    factura = Factura.objects.get(pk=factura_id)

    if monto <= 0:
        raise ValidationError("El monto del pago debe ser mayor a cero.")

    pago = Pago.objects.create(
        cliente=cliente,
        factura=factura,
        monto=monto,
        metodo=metodo,
        referencia=referencia
    )

    # Si el pago cubre el monto de la factura, marcar como pagada
    pago.marcar_factura_pagada()

    return pago


def obtener_pagos_cliente(cliente_id: int):
    """
    Devuelve todos los pagos realizados por un cliente.
    """
    return Pago.objects.filter(cliente_id=cliente_id).order_by("-fecha_pago")


def obtener_pagos_factura(factura_id: int):
    """
    Devuelve todos los pagos asociados a una factura.
    """
    return Pago.objects.filter(factura_id=factura_id).order_by("-fecha_pago")


def resumen_pagos_cliente(cliente_id: int) -> dict:
    """
    Devuelve un resumen de pagos de un cliente.
    """
    pagos = obtener_pagos_cliente(cliente_id)
    total_pagado = sum([p.monto for p in pagos])
    return {
        "total_pagos": pagos.count(),
        "total_pagado": total_pagado,
        "ultimo_pago": pagos.first().fecha_pago if pagos.exists() else None,
    }
