""""Views for the cabanass_api project.
"""
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.shortcuts import render

def gestion(request):
    return render(request, "gestion.html")


def pagina_principal(request):
    return render(request, "pagina_principal.html")

class InicioView(View):
    """View for the inicio page."""
    def get(self, request):
        """"Handle GET requests for the inicio page.
        """
        request.session['user'] = ''
        return HttpResponse("Bienvenidos  💙, tu app cabanas_api está funcionando.")
class ClienteListView(View)         :
    """View for the cliente list page."""
    def get(self, request):
        """"Handle GET requests for the cliente list page.
        """
        request.session['user'] = ''
        return HttpResponse("Vista de Clientes")
class ReservaListView(View):
    """View for the reserva list page."""
    def get(self, request):
        """"Handle GET requests for the reserva list page.
        """
        request.session['user'] = ''
        return HttpResponse("Vista de Reservas")
class AlquilerListView(View):
    """View for the alquiler list page."""
    def get(self, request):
        """"Handle GET requests for the alquiler list page.
        """
        request.session['user'] = ''
        return HttpResponse("Vista de Alquileres")
class PagoListView(View)    :
    """View for the pago list page."""          
    def get(self, request):
        """"Handle GET requests for the pago list pago"""
        request.session['user'] = ''
        return HttpResponse("pagos")     
    print("Vista de Pagos")  
class RegistroListView(View):
    """View for the registro list page."""
    def get(self, request):
        """"Handle GET requests for the registro list page."""
        request.session['user'] = ''
        return HttpResponse("Vista de Registros")  

def index(request):
    """View for the index page."""
    request.session['user'] = ''
    return HttpResponse("Bienvenidos, tu app cabanas_api está funcionando.")

def clientes(request):
    """View for the cliente list page."""
    request.session['user'] = ''
    return HttpResponse("Vista de Clientes")

def reservas(request):
    """View for the reserva list page."""
    request.session['user'] = ''
    return HttpResponse("Vista de Reservas")

def alquileres(request):
    """View for the alquiler list page."""
    request.session['user'] = ''
    return HttpResponse("Vista de Alquileres")

def registros(request):
    """View for the registro list page."""
    request.session['user'] = ''
    return HttpResponse("Vista de Registros")
