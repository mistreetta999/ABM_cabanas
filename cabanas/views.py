"""vistas del proyecto Cabanas."""
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.conf import settings
from django. views import Views
from django.cabanas import Cabana, Cliente, Reserva
from django.shortcuts import render

def pagina_principal(request):
    """
    Vista principal del sistema de gestión de cabañas.
    """
    return render(request, "pagina_principal.html")

class CabanaView(View):
    """Vista de Cabanas."""
    def get(self, request: HttpRequest) -> HttpResponse:
        """Vista de Cabanas."""
        return HttpResponse("Vista de Cabanas.")
    
class ClienteView(View):
    """Vista de Clientes."""
    def get(self, request: HttpRequest) -> HttpResponse:
        """Vista de Clientes."""
        return HttpResponse("Vista de Clientes.")
class ReservaView(View):
    """Vista de Reservas."""
    def get(self, request: HttpRequest) -> HttpResponse:
        """Vista de Reservas."""
        return HttpResponse("Vista de Reservas.")
           
class InicioView(View):
    """Vista de Inicio."""
    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("Bienvenida al sistema de gestión de Cabanas.")
class Views(View):
    """Vista general del sistema."""    
    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("Vista general del sistema.")
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
    return HttpResponse("Proyecto de Gestión de Cabanas con Django.")
