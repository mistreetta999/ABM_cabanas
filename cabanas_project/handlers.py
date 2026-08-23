""" handles cabanas_project """
from typing import Any

from django.http import HttpRequest, HttpResponse, JsonResponse


# Página principal
def pagina_principal(_request: HttpRequest) -> HttpResponse:
    """Página principal de la gestión de cabañas"""
    return HttpResponse("Página principal de la gestión de cabañas")

# -------------------
# RESERVAS
# -------------------
def listar_reservas(_request: HttpRequest) -> HttpResponse:
    """Todas las reservas"""
    lista_reservas: list[dict[str, Any]] = []
    return JsonResponse(lista_reservas, safe=False)


def detalle_reserva(_request: HttpRequest, reserva_id: int) -> HttpResponse:
    """Detalle de una reserva"""
    return HttpResponse(f"Detalle de la reserva {reserva_id}")


def crear_reserva(_request: HttpRequest, cliente_id: int, cabana_id: int) -> HttpResponse:
    """Crear una nueva reserva"""
    return HttpResponse(f"Reserva creada para cliente {cliente_id} en cabaña {cabana_id}")


def borrar_reserva(_request: HttpRequest, reserva_id: int) -> HttpResponse:
    """Borrar una reserva"""
    return HttpResponse(f"Reserva {reserva_id} borrada")

# -------------------
# ALQUILERES
# -------------------
def listar_alquileres(_request: HttpRequest) -> HttpResponse:
    """Lista todos los alquileres"""
    alquileres = [
        {"id": 1, "cliente": "Carolina", "cabaña": "Premium"},
        {"id": 2, "cliente": "Pedro", "cabaña": "Standard"},
    ]
    return JsonResponse(alquileres, safe=False)


def detalle_alquiler(_request: HttpRequest, reserva_id: int) -> HttpResponse:
    """Detalle de un alquiler"""
    return HttpResponse(f"Detalle del alquiler {reserva_id}")


def crear_alquiler(_request: HttpRequest, cliente_id: int, cabana_id: int) -> HttpResponse:
    """Crear un nuevo alquiler"""
    return HttpResponse(f"Alquiler creado para cliente {cliente_id} en cabaña {cabana_id}")


def borrar_alquiler(_request: HttpRequest, reserva_id: int) -> HttpResponse:
    """Borrar un alquiler"""
    return HttpResponse(f"Alquiler {reserva_id} borrado")

# -------------------
# PAGOS
# -------------------
def listar_pagos(_request: HttpRequest) -> HttpResponse:
    """Lista todos los pagos"""
    pagos = [
        {"id": 1, "reserva": 1, "monto": 5000},
        {"id": 2, "reserva": 2, "monto": 7000},
    ]
    return JsonResponse(pagos, safe=False)


def detalle_pago(_request: HttpRequest, reserva_id: int) -> HttpResponse:
    """Detalle de un pago"""
    return HttpResponse(f"Detalle del pago para reserva {reserva_id}")


def crear_pago(_request: HttpRequest, cliente_id: int, cabana_id: int) -> HttpResponse:
    """Crear un nuevo pago"""
    return HttpResponse(f"Pago registrado para cliente {cliente_id} en cabaña {cabana_id}")


def borrar_pago(_request: HttpRequest, reserva_id: int) -> HttpResponse:
    """Borrar un pago"""
    return HttpResponse(f"Pago de reserva {reserva_id} borrado")
