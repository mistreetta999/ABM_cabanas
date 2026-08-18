"""Vistas para la app de alquileres"""
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Alquiler

class AlquilerListView(ListView):
    """Lista todos los alquileres"""
    model = Alquiler
    template_name = "alquileres/lista.html"
    context_object_name = "alquileres"

class AlquilerCreateView(CreateView):
    """Crea un nuevo alquiler"""
    model = Alquiler
    fields = ["cliente", "Cabanas
", "fecha_inicio", "fecha_fin", "monto"]
    success_url = reverse_lazy("alquiler_list")

class AlquilerUpdateView(UpdateView):
    """Edita un alquiler existente"""
    model = Alquiler
    fields = ["cliente", "Cabanas
", "fecha_inicio", "fecha_fin", "monto"]
    success_url = reverse_lazy("alquiler_list")

class AlquilerDeleteView(DeleteView):
    """Elimina un alquiler"""
    model = Alquiler
    success_url = reverse_lazy("alquiler_list")
class AlquilerPrintView(DeleteView):
    """Elimina un alquiler"""
    model = Alquiler

    success_url = reverse_lazy("alquiler_list")
    
class AlquilerGuardarView(UpdateView):
    """Edita un alquiler existente"""
    model = Alquiler
    fields = ["cliente", "Cabanas
", "fecha_inicio", "fecha_fin", "monto"]