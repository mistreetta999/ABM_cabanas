""" views de cabanas"""
from typing import Any

from django.views.generic import ListView   
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from pathlib import Path

from cabanas_apps.clientes.models import Cliente
from .models import Cabana
directories = Path(".").parents

class CabanaListView(ListView):
    """Vista para listar todas las cabañas disponibles."""
    Cabana = Cabana
    model = Cabana
    template_name = "cabanas/formulario_cabanaListView.html"
    context_object_name = "cabanas"
class ClienteCabanasView(ListView):
    """Vista para listar todas las cabañas de un cliente específico."""
    Cliente= Cliente
    Cabana = Cabana
    model = Cabana
    template_name = "cabanas/formulario_cabanaListView.html"
    context_object_name = "cabanas"

    def get_queryset(self):
        """Obtiene el queryset de cabañas filtradas por cliente."""
        cliente_id = self.kwargs.get("cliente_id")
        return self.Cabana.objects.filter(cliente__id=cliente_id)

def cliente_home(_request)->HttpResponse:
    """Vista para el home de la aplicación de clientes."""
    return render(_request, "clientes/lista_clientes.html")

def lista_clientes(_request)->Any:
    """Vista para obtener la lista de todos los clientes en formato JSON."""
    clientes = list(Cliente.objects.all().values("id", "nombre", "email", "telefono"))
    return JsonResponse(clientes, safe=False)






