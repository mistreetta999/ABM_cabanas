"""Vistas para la aplicación de cabañas."""
from typing import TypeVar
from os import path
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from cabanas_apps.cabanas.models import Cabanas

from cabanas_apps.cabanas.views import Views
from cabanas_apps.cabanas.views.views import CabanaDeleteView

_T = TypeVar("_T")
class Views:
    """Clase para manejar las vistas de la aplicación de cabañas."""
    def __init__(self):
        self.model = Cabanas

        self.CabanaListViews = CabanaListView
        self.CabanaDetailViews = CabanaDetailView
        self.CabanaDeleteView = CabanaDeleteView
        self.CabanaDetailViews = CabanaDetailView
        self.CabanaCreateView = CabanaCreateView
        return self.Views
class CabanaListView(ListView):
    """ vista para listar las cabañas"""
    model = Cabanas

    template_name = "cabanas/list.html"
    context_object_name = "cabanas"
   
# Vista basada en clase: detalle de una cabaña
class CabanaDetailView(DetailView):
    """ vista para mostrar el detalle de una cabaña"""
    model = Cabanas

    template_name = "cabanas/detail.html"
    context_object_name = "Cabanas
"

# Vista basada en clase: creación de una cabaña
class CabanaCreateView(CreateView):
    """ vista para crear una nueva cabaña"""
    model = Cabanas

    template_name = "cabanas/form.html"
    fields = ["nombre", "descripcion", "capacidad", "precio"]
    success_url = reverse_lazy("cabanas:list")

# Vista basada en clase: edición de una cabaña
class CabanaUpdateView(UpdateView):
    """ vista para editar una cabaña existente"""
    model = Cabanas

    template_name = "cabanas/form.html"
    fields = ["nombre", "descripcion", "capacidad", "precio"]
    success_url = reverse_lazy("cabanas:list")

# Vista basada en clase: eliminación de una cabaña
class CabanaDeleteView(DeleteView):
    """ vista para eliminar una cabaña"""
    model = Cabanas

    template_name = "cabanas/confirm_delete.html"
    success_url = reverse_lazy("cabanas:list")

# Ejemplo de vista basada en función
def start_cabanas(request):

    """Vista simple para mostrar página de pagina_principal de cabañas."""
    cabanas = Cabanas
.objects.all()
    return render(request, "cabanas/pagina_principal.html", {"cabanas": cabanas})
