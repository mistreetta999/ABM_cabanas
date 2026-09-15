"""Vistas para la app de alquileres"""

from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Alquiler


class AlquilerListView(ListView):
    """class alquiler vista"""

    model = Alquiler
    template_name = "alquileres/lista.html"
    context_object_name = "alquileres"
    fields = ["cliente", "cabana", "fecha_inicio", "fecha_fin", "monto"]


class AlquilerCreateView(CreateView):
    """Crea un nuevo alquiler"""

    model = Alquiler
    fields = ["cliente", "cabanas", "fecha_inicio", "fecha_fin", "monto"]
    success_url = reverse_lazy("alquiler_list")


class AlquilerUpdateView(UpdateView):
    """Edita un alquiler existente"""

    model = Alquiler
    fields = ["cliente", "cabanas", "fecha_inicio", "fecha_fin", "monto"]
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
    fields = ["cliente", "cabanas", "fecha_inicio", "fecha_fin", "monto"]
