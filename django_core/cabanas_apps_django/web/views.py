"""Vistas de la aplicación web principal."""

from django.http import HttpResponse
from django.views import View

# Vista principal del sitio web
class WebHomeView(View):
    """Página de inicio del sistema web."""
    def get(self, request):
        """ get"""
        return HttpResponse("Bienvenido al sistema de cabañas")

# Vista de contacto
class WebContactView(View):
    """Página de contacto."""
    def get(self, request):
        """ get form for contact page"""
        return HttpResponse("Formulario de contacto")

# Vista de información general
class WebInfoView(View):
    """Página de información general."""
    def get(self, request):
        """ get information page"""
        return HttpResponse("Información sobre el sistema")

# Vista de ayuda
class WebHelpView(View):
    """Página de ayuda y soporte."""
    def get(self, request):
        """ get help page"""
        return HttpResponse("Sección de ayuda y soporte")

# Vista de prueba simple
def ping(request):
    """Endpoint de prueba para verificar que la app responde."""
    return HttpResponse("pong")
