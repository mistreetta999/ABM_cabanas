"""Handlers propios de AppConfig."""

from django.http import HttpRequest, HttpResponse


def appconfig_home(request: HttpRequest) -> HttpResponse:
    """Entrada principal de AppConfig."""
    del request
    return HttpResponse("AppConfig OK")


def pagina_principal(request: HttpRequest) -> HttpResponse:
    """Entrada simple para pagina principal."""
    del request
    return HttpResponse("Pagina principal AppConfig")


def rutas_disponibles(request: HttpRequest) -> HttpResponse:
    """Entrada simple para listar rutas de AppConfig."""
    del request
    return HttpResponse("Rutas AppConfig")


def gestion(request: HttpRequest) -> HttpResponse:
    """Entrada de gestion Django."""
    del request
    return HttpResponse("Gestion AppConfig")


def interfaz(request: HttpRequest) -> HttpResponse:
    """Entrada de interfaz Django."""
    del request
    return HttpResponse("Interfaz AppConfig")


def cabanas(request: HttpRequest) -> HttpResponse:
    """Entrada Django para cabanas."""
    del request
    return HttpResponse("Cabanas AppConfig")


def reservas(request: HttpRequest) -> HttpResponse:
    """Entrada Django para reservas."""
    del request
    return HttpResponse("Reservas AppConfig")


def alquileres(request: HttpRequest) -> HttpResponse:
    """Entrada Django para alquileres."""
    del request
    return HttpResponse("Alquileres AppConfig")


def pagos(request: HttpRequest) -> HttpResponse:
    """Entrada Django para pagos."""
    del request
    return HttpResponse("Pagos AppConfig")


def registros(request: HttpRequest) -> HttpResponse:
    """Entrada Django para registros."""
    del request
    return HttpResponse("Registros AppConfig")


def chatbot(request: HttpRequest) -> HttpResponse:
    """Entrada Django para chatbot."""
    del request
    return HttpResponse("Chatbot AppConfig")


def clientes(request: HttpRequest) -> HttpResponse:
    """Entrada Django para clientes."""
    del request
    return HttpResponse("Clientes AppConfig")
