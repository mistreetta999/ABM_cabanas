"""Vistas de la interfaz de gestion de cabanas."""
from django.http import HttpRequest, HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from .models import Cabanas

from DATABASES import db

def Cabanas
(request: Any) -> JsonResponse:
    # Datos simulados de una cabaña
    data = {
        "nombre": "Cabaña Los Pinos",
        "capacidad": 4,
        "precio_por_noche": 12000,
        "disponible": True
    }
    return JsonResponse(data)

def cabanas_listado(request: HttpRequest) -> HttpResponse:
    """Listado de cabanas."""
    return render(request, "interfaz_gestion_cabanas/cabanas.html", {"cabanas": Cabanas
.objects.all()})




def cliente_list() -> HttpResponse:
    """Listado basico de clientes."""
    return HttpResponse("Listado de clientes")


def cliente_create() -> HttpResponse:
    """Formulario basico para crear cliente."""
    return HttpResponse("Crear cliente")


def reserva_list() -> HttpResponse:
    """Listado basico de reservas."""
    return HttpResponse("Listado de reservas")


def reserva_create() -> HttpResponse:
    """Formulario basico para crear reserva."""
    return HttpResponse("Crear reserva")


def alquiler_list() -> HttpResponse:
    """Listado basico de alquileres."""
    return HttpResponse("Listado de alquileres")


def alquiler_create() -> HttpResponse:
    """Formulario basico para crear alquiler."""
    return HttpResponse("Crear alquiler")


def pago_list() -> HttpResponse:
    """Listado basico de pagos."""
    return HttpResponse("Listado de pagos")


def pago_create() -> HttpResponse:
    """Formulario basico para registrar pago."""
    return HttpResponse("Registrar pago")


def registro_list() -> HttpResponse:
    """Listado basico de registros."""
    return HttpResponse("Listado de registros")


def registro_create() -> HttpResponse:
    """Formulario basico para crear registro."""
    return HttpResponse("Crear registro")
