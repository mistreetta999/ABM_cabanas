"""Vistas basadas en clases para la aplicación de reservas."""
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Reserva
from .forms import ReservaForm  # si usás formularios

class ListaReservasView(ListView):
    """Muestra todas las reservas en una lista."""
    model = Reserva
    template_name = "reservas/lista.html"
    context_object_name = "reservas"

class DetalleReservaView(DetailView):
    """Muestra el detalle de una reserva específica."""
    model = Reserva
    template_name = "reservas/detalle.html"
    context_object_name = "reserva"

class CrearReservaView(CreateView):
    """Crea una nueva reserva."""
    model = Reserva
    form_class = ReservaForm
    template_name = "reservas/formulario.html"
    success_url = reverse_lazy("lista_reservas")

class EditarReservaView(UpdateView):
    """Edita una reserva existente."""
    model = Reserva
    form_class = ReservaForm
    template_name = "reservas/formulario.html"
    success_url = reverse_lazy("lista_reservas")

class EliminarReservaView(DeleteView):
    """Elimina una reserva."""
    model = Reserva
    template_name = "reservas/confirmar_eliminar.html"
    success_url = reverse_lazy("lista_reservas")
