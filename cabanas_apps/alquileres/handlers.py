"""
Handlers de la aplicación Alquileres.
Contiene funciones auxiliares y lógica de negocio para integrarse con el sistema.
"""

from datetime import date
from django.core.exceptions import ValidationError
from django.db import transaction
from .models import Alquiler
from reservas.models import Reserva
from clientes.models import Cliente
from facturas.models import Factura


def crear_alquiler(cliente_id: int, cabana_id: int, fecha_inicio: date, fecha_fin: date, monto_total: float) -> Alquiler:
    """
    Crea un nuevo alquiler asociado a un cliente y una cabaña.
    """
    if fecha_fin <= fecha_inicio:
        raise ValidationError("La fecha de fin debe ser posterior a la fecha de inicio.")

    cliente = Cliente.objects.get(pk=cliente_id)

    alquiler = Alquiler.objects.create(
        cliente=cliente,
        cabana_id=cabana_id,
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
        monto_total=monto_total,
        estado="activo",
    )
    return alquiler


@transaction.atomic
def generar_factura_alquiler(alquiler_id: int) -> Factura:
    """
    Genera una factura asociada a un alquiler.
    """
    try:
        alquiler = Alquiler.objects.get(pk=alquiler_id)
        cliente = alquiler.cliente

        factura = Factura.objects.create(
            cliente=cliente,
            cabana=alquiler.cabana,
            reserva=None,  # opcional si el alquiler no proviene de una reserva
            fecha_emision=date.today(),
            fecha_vencimiento=alquiler.fecha_fin,
            monto=alquiler.monto_total,
            estado="pendiente",
        )
        return factura
    except Alquiler.DoesNotExist:
        raise ValidationError("El alquiler indicado no existe.")


def validar_alquiler(alquiler: Alquiler) -> None:
    """
    Valida reglas de negocio sobre un alquiler.
    """
    if alquiler.monto_total <= 0:
        raise ValidationError("El monto del alquiler debe ser mayor a cero.")
    if alquiler.fecha_fin <= alquiler.fecha_inicio:
        raise ValidationError("La fecha de fin debe ser posterior a la fecha de inicio.")
    if alquiler.estado not in ["activo", "finalizado", "cancelado"]:
        raise ValidationError("El estado del alquiler no es válido.")
