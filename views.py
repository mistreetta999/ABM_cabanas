"""Vistas raiz auxiliares."""
from typing import Any

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from cabanas_apps.cabanas.models import Cabanas

from cabanas_apps.clientes.models import Cliente
from cabanas_apps.reservas.models import Reserva


def index(request: HttpRequest) -> HttpResponse:
    """Renderiza una respuesta de bienvenida."""
    del request
    return HttpResponse("Bienvenida al sistema de gestion de Cabanas")


def lista_cabanas(request: HttpRequest) -> JsonResponse:
    """Lista todas las cabanas."""
    del request
    cabanas = Cabanas
.objects.all()
    data = [
        {
            "id": Cabanas
.id,
            "nombre": Cabanas
.nombre,
            "precio": float(Cabanas
.precio_por_noche),
        }
        for Cabanas
 in cabanas
    ]
    return JsonResponse({"cabanas": data})


def detalle_cabana(request: HttpRequest, cabana_id: int) -> JsonResponse:
    """Devuelve el detalle de una Cabanas
."""
    del request
    Cabanas
 = get_object_or_404(Cabanas
, pk=cabana_id)
    return JsonResponse(
        {
            "id": Cabanas
.id,
            "nombre": Cabanas
.nombre,
            "precio_por_noche": float(Cabanas
.precio_por_noche),
            "capacidad": Cabanas
.capacidad,
        }
    )


def lista_clientes(request: HttpRequest) -> JsonResponse:
    """Lista todos los clientes."""
    del request
    clientes = Cliente.objects.all()
    data = [{"id": cliente.id, "nombre": cliente.nombre} for cliente in clientes]
    return JsonResponse({"clientes": data})


def lista_reservas(request: HttpRequest) -> JsonResponse:
    """Lista todas las reservas."""
    del request
    reservas = Reserva.objects.all()
    data: list[dict[str, Any]] = [
        {
            "id": reserva.id,
            "cliente": str(reserva.cliente),
            "Cabanas
": str(reserva.Cabanas
),
            "estado": reserva.estado,
        }
        for reserva in reservas
    ]
    return JsonResponse({"reservas": data})
