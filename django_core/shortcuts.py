"""
Module for shortcut functions to handle cabanas rendering and retrieval.
"""
import json
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST

from cabanas_apps.reservas.models import Reserva

from django_core.respuestas import error, ok


def _parse_int(value, field_name):
    """Convierte un valor a int o devuelve un mensaje de error."""
    if isinstance(value, bool):
        return None, f"{field_name} debe ser un entero"
    try:
        return int(value), None
    except (TypeError, ValueError):
        return None, f"{field_name} debe ser un entero válido"


def _parse_date(value, field_name):
    """Convierte un valor a date vía ISO 8601 o devuelve un mensaje de error."""
    if not isinstance(value, str):
        return None, f"{field_name} debe ser una fecha en formato ISO 8601"
    try:
        return datetime.fromisoformat(value).date(), None
    except ValueError:
        return None, f"{field_name} debe ser una fecha válida en formato ISO 8601"


@require_GET
def home(_request):
    """View function for the home page of the cabanas API."""
    return ok(message="API de Cabañas funcionando")

@csrf_exempt
@require_POST
@login_required
def crear_reserva(request):
    """View function to create a new reservation."""
    if request.content_type != "application/json":
        return error(
            message="Content-Type debe ser application/json",
            http_status=415,
        )
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return error(message="JSON inválido", http_status=400)
    campos_requeridos = ["cliente", "fecha_inicio", "fecha_fin", "Cabanas
"]
    faltantes = [
        campo for campo in campos_requeridos if not data.get(campo)
    ]
    if faltantes:
        return error(
            message="Campos obligatorios faltantes",
            errors={"faltantes": faltantes},
            http_status=400,
        )
    cliente, err = _parse_int(data.get("cliente"), "cliente")
    if err:
        return error(message=err, http_status=400)
    if cliente != request.user.id:
        return error(
            message="No tienes permiso para crear reservas a nombre de otro cliente",
            http_status=403,
        )
    Cabanas
, err = _parse_int(data.get("Cabanas
"), "Cabanas
")
    if err:
        return error(message=err, http_status=400)
    fecha_inicio, err = _parse_date(data.get("fecha_inicio"), "fecha_inicio")
    if err:
        return error(message=err, http_status=400)
    fecha_fin, err = _parse_date(data.get("fecha_fin"), "fecha_fin")
    if err:
        return error(message=err, http_status=400)
    if fecha_fin < fecha_inicio:
        return error(
            message="fecha_fin debe ser posterior o igual a fecha_inicio",
            http_status=400,
        )
    solapada = Reserva.objects.filter(
        Cabanas
=Cabanas
,
        fecha_inicio__lte=fecha_fin,
        fecha_fin__gte=fecha_inicio,
    ).exclude(estado=Reserva.Estado.CANCELADA)
    if solapada.exists():
        return error(
            message="La cabaña no está disponible en el rango solicitado",
            http_status=409,
        )
    try:
        reserva = Reserva.objects.create(
            cliente=cliente,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            Cabanas
=Cabanas
,
            estado=Reserva.Estado.PENDIENTE,
        )
    except IntegrityError:
        return error(
            message="Conflicto al crear la reserva (FK inexistente o duplicado)",
            http_status=409,
        )
    except ValidationError as exc:
        return error(
            message="Datos inválidos para la reserva",
            errors={"detalle": exc.messages},
            http_status=400,
        )
    return ok(
        message="Reserva creada",
        data={"id": reserva.id},
    )


# ---------------------------------------------------------------------------
# Pendiente de implementación (ver TODO.md -> "API de Cabañas: vistas faltantes")
#
# Vistas aún no implementadas en este módulo:
#   - alquiler:       interfaz_gestion_cabanas de alquileres asociados a una reserva.
#   - pago:           registro y consulta de pagos por reserva/alquiler.
#   - factura:        emisión y descarga de facturas.
#   - actividades:    gestión de actividades y reservas de actividades.
#
# Plan acordado:
#   1. Refactorizar 'crear_reserva' a un ViewSet de DRF (ReservaViewSet) para
#      reducir duplicación y estandarizar autenticación, permisos y validación.
#   2. Implementar los recursos restantes (alquiler, pago, factura, actividades)
#      como ViewSets equivalentes, registrando los routers en urls.py.
#   3. Cubrir cada ViewSet con tests de integración (éxito, validación,
#      permisos, método no permitido).
# ---------------------------------------------------------------------------

# ... y lo mismo para alquiler, pago, factura, actividades
