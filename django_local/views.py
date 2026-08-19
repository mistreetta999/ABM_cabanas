""" Vistas principales de la app django_local """
from typing import Any

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Vista simple para probar que todo funciona
def inicio():
    """Vista de bienvenida."""
    return HttpResponse("Bienvenida a Gestión de Cabañas")


# Ejemplo de vista que renderiza un template
def pagina_principal(request):
    """Vista que renderiza un template principal."""
    return render(request, "pagina_principal.html")


# Ejemplo con clase basada en vistas
class CabanaView(View):
    """Vista de listado de cabañas."""

    def get(self, _request, *_args, **_kwargs) -> Any:
        """Devuelve el listado de cabañas."""
        return HttpResponse("Listado de cabañas")
