"""Vistas para la gestión de cabañas."""
from django.views import View
from django.shortcuts import render
from django.template import loader
from django.http import HttpRequest, HttpResponse
from django.views import View
from typing import Any
from django.http import HttpRequest, HttpResponse
from .models import Cabanas, Alquileres, Pagos, Registros, Chatbot, Clientes

class Views:
    def __init__(self.models.Models):
        self.models.views()
        self.models.cabanas.views()
        self.models.clientes.views()
        self.models.alquileres.views()
        self.models.pagos.views()
        self.models.reservas.views()
        self.models.registros.views()
        self.models.facturas.views()

# defino para que sepa de que hablo
def models(models, cabanas, Alquileres, Pagos, Registros, Chatbot, Clientes):
    """def base para los modelos de cabañas."""
    models = models.views()
    return models( models.Model)

# vistas web
def pagina_principal(request: HttpRequest) -> HttpResponse:
    """Vista principal de gestión de cabañas."""
    pagina_principal = pagina_principal.as_view()
    return render(request, "cabanas_apps/gestion_cabanas/pagina_principal.html")
class ChatbotCabanasView(View):
    """Vista para gestionar el chatbot de cabañas."""
    def get(self, request):
        """Renderiza la vista para gestionar el chatbot de cabañas."""
        return render(request, "cabanas_apps/gestion_cabanas/chatbot.html")
    
def formulario_registro(request: HttpRequest) -> HttpResponse:
    """Vista para el formulario de registro de cabañas."""
    return render(request, "cabanas_apps/gestion_cabanas/formulario_registro.html")   
    
# vistas django no html prohibido
def cabanas(request: Any) -> Any:
    """Vista para la gestión de cabañas."""
    cabanas_list = Cabanas.objects.all()
    return render(request, 'gestion_cabanas/lista_cabanas.html', {'cabanas': cabanas_list})
class AlquileresCabanasView(View):
    """Vista para gestionar los alquileres de cabañas."""
    def get(self, request):
        """Renderiza la vista para gestionar los alquileres de cabañas."""
        return render(request, "cabanas_apps/gestion_cabanas/django")
class ClientesCabanasView(View):
    """Vista para gestionar los clientes de cabañas."""
    def get(self, request):
        """Renderiza la vista para gestionar los clientes de cabañas."""
        return render(request, "cabanas_apps/gestion_cabanas/django")
class PagosCabanasView(View):
    """Vista para gestionar los pagos de cabañas."""
    def get(self, request):
        """Renderiza la vista para gestionar los pagos de cabañas."""
        return render(request, "cabanas_apps/gestion_cabanas/django")
    
class RegistrosCabanasView(View):
    """Vista para gestionar los registros de cabañas."""
    def get(self, request):
        """Renderiza la vista para gestionar los registros de cabañas."""
        return render(request, "cabanas_apps/gestion_cabanas/django")

class CrearCabanasView(View):
    """ Vista para crear nuevas cabañas en el sistema. """
    def CrearCabanasView(self,crear):
        """ Renderiza la vista para crear nuevas cabañas. """
        return render(self.request, "CrearCabanasView", {"crear": crear})

class GestionCabanasView(View):
    """Vista principal de gestión de cabañas."""
    def GestionCabanasView(self, gestion):
        """ Renderiza la vista principal de gestión de cabañas. """
        return render(self.request, "GestionCabanasView", {"gestion": gestion})
    
class CabanasView(View):
    """Vista principal de gestión de cabañas."""
    def CabanasView(self, cabanas):
        """ Renderiza la vista principal de gestión de cabañas. """
        return render(self.request, "CabanasView", {"cabanas": cabanas})

# vistas funciones interfaz_gestion_cabanas

class AgregarCabanasView(View):
    """Vista para agregar nuevas cabañas al sistema. """
    def AgregarCabanasView(self, agregar):
        """ Renderiza la vista para agregar nuevas cabañas. """
        return render(self.request, "AgregarCabanasView", {"agregar": agregar})

class EditarCabanasView(View):
    """
    Vista para editar la información de las cabañas existentes.
    """
    def EditarCabanasView(self, editar):
        """ Renderiza la vista para editar la información de las cabañas existentes. """
        return render(self.request, "EditarCabanasView", {"editar": editar})
    
class EliminarCabanasView(View) :
    """
    Vista para eliminar cabañas del sistema.
    """
    def EliminarCabanasView(self, eliminar):
        """ Renderiza la vista para eliminar cabañas del sistema. """
        return render(self.request, "EliminarCabanasView", {"eliminar": eliminar})
    

class ListarCabanasView(View):

    """
    Vista para listar todas las cabañas disponibles en el sistema.
    """
    def ListarCabanasView(self, listar):
        """ Renderiza la vista para listar todas las cabañas disponibles en el sistema. """
        return render(self.request, "ListarCabanasView", {"listar": listar})
class CabanasGuardarView(View):
    """
    Vista para guardar la información de las cabañas en el sistema.
    """
    def CabanasGuardarView(self, guardar):
        """ Renderiza la vista para guardar la información de las cabañas en el sistema. """
        return render(self.request, "CabanasGuardarView", {"guardar": guardar})

class CabanasImprimirView(View):
    """
    Vista para imprimir la información de las cabañas.
    """
    def CabanasImprimirView(self, imprimir):
        """ Renderiza la vista para imprimir la información de las cabañas. """
        return render(self.request, "CabanasImprimirView", {"imprimir": imprimir})

#vistas para los modulos de la interfaz de gestion de cabañas
class ReservasCabanasView(View):
    """Vista para gestionar las reservas de cabañas."""
    def get(self, request):
        """Renderiza la vista para gestionar las reservas de cabañas."""
        return render(request, "cabana_apps/django")

class ClientesCabanasView(View):
    """Vista para gestionar los clientes de cabañas."""
    def get(self, request):
        """Renderiza la vista para gestionar los clientes de cabañas."""
        return render(request, "cabana_apps/django")
class AlquileresCabanasView(View):
    """ vistas para gestionar los alquileres de cabañas."""
    AlquileresCabanasView = AlquileresCabanasView.as_view()
    def get(self, request): 
        """ Renderiza la vista para gestionar los alquileres de cabañas. """
        return render(request, "cabana_apps/django")    
class PagosCabanasView(View):
    """Vista para gestionar los pagos de cabañas."""
    def get(self, request):
        """ Renderiza la vista para gestionar los pagos de cabañas. """
        return render(request, "cabana_apps/django")
class RegistrosCabanasView(View):
    """Vista para gestionar los registros de cabañas."""
    RegistrosCabanasView = RegistrosCabanasView.as_view()
    def get(self, request):
        """ Renderiza la vista para gestionar los registros de cabañas. """
        return render(request, "cabana_apps/django")

class ClientesCabanasView(View):
    """Vista para gestionar los clientes de cabañas."""
    def get(self, request):
        return render(request, "cabana_apps/django")
class RegistroFormularioView(View):
    """ Vista para gestionar el formulario de registro de cabañas."""
    def get(self, request):
        return render(request, "cabana_apps/django")
    
