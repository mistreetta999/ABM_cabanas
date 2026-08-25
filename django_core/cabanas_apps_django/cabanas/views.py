"""Vistas para la app de cabañas"""
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cabana


class CabanaDetailView(DetailView):
    """ class detalle"""
    model = Cabana
    template_name = "cabanas/detalle_cabana.html"
    context_object_name = "cabana"


class CabanaListView(ListView):
    """Lista todas las cabañas"""
    model = Cabana

    template_name = "cabanas/lista.html"
    context_object_name = "cabanas"

class CabanaCreateView(CreateView):
    """Crea una nueva cabaña"""
    model = Cabana

    fields = ["nombre", "descripcion", "capacidad", "precio"]
    template_name = "cabanas/form.html"
    success_url = reverse_lazy("cabana_list")

class CabanaUpdateView(UpdateView):
    """Edita una cabaña existente"""
    model = Cabana

    fields = ["nombre", "descripcion", "capacidad", "precio"]
    template_name = "cabanas/form.html"
    success_url = reverse_lazy("cabana_list")

class CabanaDeleteView(DeleteView):
    """Elimina una cabaña"""
    model = Cabana

    template_name = "cabanas/confirm_delete.html"
    success_url = reverse_lazy("cabana_list")
