"""vistas del proyecto Cabañas."""
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

def inicio(request: HttpRequest) -> HttpResponse:
    """
    Vista principal del proyecto Cabañas.
    """
    return HttpResponse("Bienvenida al sistema de gestión de cabañas.")

def dashboard(request: HttpRequest) -> HttpResponse:
    """
    Vista de dashboard general.
    """
    context = {
        "titulo": "Panel de Control",
        "mensaje": "Aquí puedes acceder a clientes, reservas, pagos y más."
    }
    return render(request, "dashboard.html", context)

def acerca_de(request: HttpRequest) -> HttpResponse:
    """
    Vista de información sobre el proyecto.
    """
    return HttpResponse("Proyecto de Gestión de Cabañas con Django.")
