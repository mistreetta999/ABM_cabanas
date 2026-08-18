"""Vistas para la aplicación de cabañas."""
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from cabanas_principal.models import Cabanas

from django.http import HttpResponse, HttpRequest
from django.views import View
from django.views.generic import TemplateView

def pagina_principal(request: HttpRequest) -> HttpResponse:
    """
    Vista principal del sistema de gestión de cabañas.
    """
    return render(request, "pagina_principal.html")

class CabanaListView(ListView):
    """ vista para listar las cabañas"""
    model = Cabanas

    template_name = "cabanas/list.html"
    context_object_name = "cabanas"
# Lista de cabañas: uso normal de ListView
# Vista basada en clase: detalle de una cabaña
class CabanaDetailView(DetailView):
    """ vista para mostrar el detalle de una cabaña"""
    model = Cabanas

    template_name = "cabanas/detail.html"
    context_object_name = "Cabanas
"
# Detalle de cabaña: uso normal de DetailView

# Vista basada en clase: creación de una cabaña
class CabanaCreateView(CreateView):
    """ vista para crear una nueva cabaña"""
    model = Cabanas

    template_name = "cabanas/form.html"
    fields = ["nombre", "descripcion", "capacidad", "precio"]
    success_url = reverse_lazy("cabanas:list")
# CreateView: uso normal

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
