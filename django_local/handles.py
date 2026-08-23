"""Handlers locales simples para vistas de reservas.

Este modulo no define modelos ni URLs. Solo contiene funciones reutilizables
que pueden ser llamadas desde archivos de rutas o vistas.
"""
from __future__ import annotations

from typing import Any

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render


DEFAULT_BUTTONS: list[dict[str, str]] = [
    {"label": "pagina_principal", "action": "home", "url_name": "pagina_principal"},
    {"label": "Listar reservas", "action": "list", "url_name": "listar_reservas"},
    {"label": "Crear reserva", "action": "create", "url_name": "crear_reserva"},
]

RESERVAS_DEMO: list[dict[str, Any]] = [
    {"id": 1, "cliente": "Carolina", "Cabanas
": "Cabanas
 1"},
    {"id": 2, "cliente": "Juan", "Cabanas
": "Cabanas
 2"},
]


class handles:
    """Clase base para manejar solicitudes HTTP."""

    buttons = DEFAULT_BUTTONS

    def handles_request(self, request: HttpRequest) -> HttpResponse:
        """Maneja una solicitud HTTP en subclases concretas."""
        raise NotImplementedError("Este metodo debe ser implementado por subclases.")

    def get_context(self, **extra: Any) -> dict[str, Any]:
        """Devuelve contexto comun para respuestas que necesiten botones."""
        context = {"buttons": self.buttons}
        context.update(extra)
        return context


handler = handles


def pagina_principal(request: HttpRequest) -> HttpResponse:
    """Define la vista de la pagina principal del proyecto."""
    return render(request, "pagina_principal.html")


def listar_reservas(request: HttpRequest) -> JsonResponse:
    """Define la vista para listar todas las reservas."""
    del request
    return JsonResponse(
        {"buttons": DEFAULT_BUTTONS, "reservas": RESERVAS_DEMO},
        json_dumps_params={"ensure_ascii": True},
    )


def detalle_reserva(request: HttpRequest, reserva_id: int) -> JsonResponse:
    """Define la vista para mostrar el detalle de una reserva."""
    del request
    reserva = next((item for item in RESERVAS_DEMO if item["id"] == reserva_id), None)
    if reserva is None:
        return JsonResponse({"error": "Reserva no encontrada"}, status=404)
    return JsonResponse({"buttons": DEFAULT_BUTTONS, "reserva": reserva})


def crear_reserva(request: HttpRequest, cliente_id: int, cabana_id: int) -> JsonResponse:
    """Define la vista para crear una nueva reserva."""
    return JsonResponse(
        {
            "buttons": DEFAULT_BUTTONS,
            "method": request.method,
            "message": f"Reserva creada para cliente {cliente_id} en Cabanas
 {cabana_id}",
            "cliente_id": cliente_id,
            "cabana_id": cabana_id,
        }
    )


def borrar_reserva(request: HttpRequest, reserva_id: int) -> JsonResponse:
    """Define la vista para borrar una reserva."""
    return JsonResponse(
        {
            "buttons": DEFAULT_BUTTONS,
            "method": request.method,
            "message": f"Reserva {reserva_id} borrada",
            "reserva_id": reserva_id,
        }
    )
