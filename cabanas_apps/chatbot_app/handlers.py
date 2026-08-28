"""Vistas HTTP para la gestión de cabañas."""
from typing import Any

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render


def pagina_principal(request) -> Any:
    """Renderiza la plantilla pagina_principal.html"""
    contexto = {
        "titulo": "Panel Principal",
        "mensaje": "Bienvenida al sistema de gestión de cabañas"
    }
    return render(request, "cabanas/pagina_principal.html", contexto)


def listar_reservas(_request)->Any:
    """ lista reservas"""
    reservas = [
        {"id": 1, "cliente": "Carolina", "cabaña": "Premium"},
        {"id": 2, "cliente": "Juan", "cabaña": "Standard"},
    ]
    return JsonResponse(reservas, safe=False)

def detalle_reserva(_request, reserva_id)->Any:
    """Muestra el detalle de una reserva específica."""
    return HttpResponse(f"Detalle de la reserva {reserva_id}")

def crear_reserva(_request, cliente_id, cabana_id)->Any:
    """Crea una nueva reserva para un cliente en una cabaña específica."""
    return HttpResponse(f"Reserva creada para cliente {cliente_id} en cabaña {cabana_id}")

def borrar_reserva(_request, reserva_id)->Any:
    """Borra una reserva específica."""
    del _request
    return HttpResponse(f"Reserva {reserva_id} borrada")

# -------------------
# ALQUILERES
# -------------------
def listar_alquileres(_request)->Any:
    """Lista todos los alquileres."""
    alquileres = [
        {"id": 1, "cliente": "Pedro", "cabaña": "1"},
        {"id": 2, "cliente": "Lucía", "cabaña": "2"},
    ]
    return JsonResponse(alquileres, safe=False)

def detalle_alquiler(_request, reserva_id)->Any:
    """ detalle"""
    return HttpResponse(f"Detalle del alquiler {reserva_id}")

def crear_alquiler(_request, cliente_id, cabana_id)->Any:
    """ crear"""
    return HttpResponse(f"Alquiler creado para cliente {cliente_id} en cabaña {cabana_id}")

def borrar_alquiler(_request, reserva_id)->Any:
    """ borrar"""
    return HttpResponse(f"Alquiler {reserva_id} borrado")

def listar_pagos(_request)->Any:
    """ lista"""
    pagos = [
        {"id": 1, "reserva": 1, "monto": 5000},
        {"id": 2, "reserva": 2, "monto": 7000},
    ]
    return JsonResponse(pagos, safe=False)

def detalle_pago(_request, reserva_id)->Any:
    """ detalle"""
    return HttpResponse(f"Detalle del pago para reserva {reserva_id}")

def crear_pago(_request, cliente_id, cabana_id)->Any:
    """ crear"""
    return HttpResponse(f"Pago registrado para cliente {cliente_id} en cabaña {cabana_id}")

def borrar_pago(_request, reserva_id)->Any:
    """ borrar"""
    return HttpResponse(f"Pago de reserva {reserva_id} borrado")
