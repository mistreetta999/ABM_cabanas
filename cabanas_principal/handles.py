"""Handlers locales simples para vistas de reservas.
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
Este modulo no define modelos ni URLs. Solo contiene funciones reutilizables
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
que pueden ser llamadas desde archivos de rutas o vistas.
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
"""
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
from __future__ import annotations
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
from typing import Any
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
from django.http import HttpRequest, HttpResponse, JsonResponse
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
from django.shortcuts import render
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
DEFAULT_BUTTONS: list[dict[str, str]] = [
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    {"label": "pagina_principal", "action": "home", "url_name": "pagina_principal"},
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    {"label": "Listar reservas", "action": "list", "url_name": "listar_reservas"},
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    {"label": "Crear reserva", "action": "create", "url_name": "crear_reserva"},
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
]
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
RESERVAS_DEMO: list[dict[str, Any]] = [
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    {"id": 1, "cliente": "Carolina", "Cabanas
": "Cabanas
 1"},
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    {"id": 2, "cliente": "Juan", "Cabanas
": "Cabanas
 2"},
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
]
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
class handles:
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    """Clase base para manejar solicitudes HTTP."""
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    buttons = DEFAULT_BUTTONS
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    def handles_request(self, request: HttpRequest) -> HttpResponse:
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        """Maneja una solicitud HTTP en subclases concretas."""
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        raise NotImplementedError("Este metodo debe ser implementado por subclases.")
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    def get_context(self, **extra: Any) -> dict[str, Any]:
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        """Devuelve contexto comun para respuestas que necesiten botones."""
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        context = {"buttons": self.buttons}
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        context.update(extra)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        return context
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
handler = handles
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
def pagina_principal(request: HttpRequest) -> HttpResponse:
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    """Define la vista de la pagina principal del proyecto."""
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    return render(request, "pagina_principal.html")
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
def listar_reservas(request: HttpRequest) -> JsonResponse:
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    """Define la vista para listar todas las reservas."""
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    del request
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    return JsonResponse(
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        {"buttons": DEFAULT_BUTTONS, "reservas": RESERVAS_DEMO},
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        json_dumps_params={"ensure_ascii": True},
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    )
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
def detalle_reserva(request: HttpRequest, reserva_id: int) -> JsonResponse:
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    """Define la vista para mostrar el detalle de una reserva."""
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    del request
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    reserva = next((item for item in RESERVAS_DEMO if item["id"] == reserva_id), None)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    if reserva is None:
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        return JsonResponse({"error": "Reserva no encontrada"}, status=404)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    return JsonResponse({"buttons": DEFAULT_BUTTONS, "reserva": reserva})
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
def crear_reserva(request: HttpRequest, cliente_id: int, cabana_id: int) -> JsonResponse:
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    """Define la vista para crear una nueva reserva."""
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    return JsonResponse(
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        {
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
            "buttons": DEFAULT_BUTTONS,
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
            "method": request.method,
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
            "message": f"Reserva creada para cliente {cliente_id} en Cabanas
 {cabana_id}",
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
            "cliente_id": cliente_id,
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
            "cabana_id": cabana_id,
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        }
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    )
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
def borrar_reserva(request: HttpRequest, reserva_id: int) -> JsonResponse:
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    """Define la vista para borrar una reserva."""
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    return JsonResponse(
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        {
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
            "buttons": DEFAULT_BUTTONS,
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
            "method": request.method,
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
            "message": f"Reserva {reserva_id} borrada",
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
            "reserva_id": reserva_id,
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        }
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    )
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
