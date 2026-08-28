"""
Vistas de la aplicación Alquileres.
CRUD completo con clases basadas en vistas genéricas.
"""

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Alquiler


class AlquilerListView(ListView):
    """Lista todos los alquileres."""
    model = Alquiler
    template_name = "alquileres/alquiler_list.html"
    context_object_name = "alquileres"


class AlquilerDetailView(DetailView):
    """Muestra el detalle de un alquiler específico."""
    model = Alquiler
    template_name = "alquileres/alquiler_detail.html"
    context_object_name = "alquiler"


class AlquilerCreateView(CreateView):
    """Crea un nuevo alquiler."""
    model = Alquiler
    template_name = "alquileres/alquiler_form.html"
    fields = ["cliente", "cabana", "fecha_inicio", "fecha_fin", "monto_total", "estado"]
    success_url = reverse_lazy("alquileres:alquiler_list")


class AlquilerUpdateView(UpdateView):
    """Edita un alquiler existente."""
    model = Alquiler
    template_name = "alquileres/alquiler_form.html"
    fields = ["cliente", "cabana", "fecha_inicio", "fecha_fin", "monto_total", "estado"]
    success_url = reverse_lazy("alquileres:alquiler_list")


class AlquilerDeleteView(DeleteView):
    """Elimina un alquiler."""
    model = Alquiler
    template_name = "alquileres/alquiler_confirm_delete.html"
    success_url = reverse_lazy("alquileres:alquiler_list")
