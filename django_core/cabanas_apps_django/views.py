"""Vistas principales de cabanas_apps_django"""

from django.http import HttpResponse
from django.views import View


# Ejemplo de vista principal
class HomeView(View):
    """Vista de inicio general del sistema de cabañas."""

    def get(self, request):
        return HttpResponse("Bienvenido al sistema de cabañas")


# Ejemplo de vista de prueba para verificar que todo funciona
def ping(request):
    """Vista simple para testear que el proyecto corre sin errores."""
    return HttpResponse("pong")
