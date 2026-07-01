"""Handles (manejadores) principales de Django y Chatbot."""

import json
from django.http import JsonResponse, HttpRequest
from django.shortcuts import render
from django.template import loader
from django.template.exceptions import TemplateDoesNotExist
from django.views.decorators.csrf import csrf_exempt


def _render_with_fallback(request: HttpRequest, template_names: list[str]):
    """Renderiza la primera plantilla disponible y usa pagina_principal como respaldo."""
    for template_name in template_names:
        try:
            loader.get_template(template_name)
            return render(request, template_name)
        except TemplateDoesNotExist:
            continue
    return render(request, "pagina_principal.html")


def pagina_principal(request: HttpRequest):
    """Render de la página principal aprobada."""
    return render(request, "pagina_principal.html")


def gestion_cabanas(request: HttpRequest):
    """Handle directo para el acceso didáctico principal."""
    return render(request, "pagina_principal.html")


def panel_django(request: HttpRequest):
    """Panel principal de gestión Django."""
    return _render_with_fallback(request, ["cabanas_apps/panel_django.html", "pagina_principal.html"])


def dashboard(request: HttpRequest):
    return _render_with_fallback(request, ["cabanas_apps/panel_django.html", "pagina_principal.html"])


def clientes(request: HttpRequest):
    return _render_with_fallback(request, ["clientes.html", "lista.html", "pagina_principal.html"])


def reservas(request: HttpRequest):
    return _render_with_fallback(request, ["reservas.html", "pagina_principal.html"])


def pagos(request: HttpRequest):
    return _render_with_fallback(request, ["pagos.html", "consultas.html", "pagina_principal.html"])


def cabanas(request: HttpRequest):
    return _render_with_fallback(request, ["cabanas.html", "pagina_principal.html"])


def alquileres(request: HttpRequest):
    return _render_with_fallback(request, ["alquileres.html", "lista.html", "pagina_principal.html"])


def registros(request: HttpRequest):
    return _render_with_fallback(request, ["registros.html", "consultas.html", "pagina_principal.html"])


def chatbot_home(request: HttpRequest):
    """Interfaz HTML del chatbot (embebida por iframe)."""
    return render(request, "chatbot/chatbot.html")


@csrf_exempt
def chatbot_api(request: HttpRequest):
    """API simple del chatbot para consultas básicas."""
    if request.method != "POST":
        return JsonResponse({"reply": "Enviá una consulta para recibir información."})

    try:
        data = json.loads(request.body or "{}")
    except json.JSONDecodeError:
        data = {}

    message = str(data.get("message", "")).lower()

    if "precio" in message or "tarifa" in message:
        reply = "Las tarifas dependen de fecha y cantidad de huéspedes. Escribinos al WhatsApp 3544562397."
    elif "ubicacion" in message or "donde" in message or "dirección" in message:
        reply = "Estamos en Mina Clavero, Córdoba, cerca del centro y balnearios principales."
    elif "reserva" in message or "disponibilidad" in message:
        reply = "Para reservas y disponibilidad, compartinos fecha, cantidad de personas y teléfono."
    else:
        reply = "Gracias por tu consulta. Puedo ayudarte con ubicación, tarifas y reservas."

    return JsonResponse({"reply": reply})
