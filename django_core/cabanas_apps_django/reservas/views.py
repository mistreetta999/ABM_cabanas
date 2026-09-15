"""Vistas basadas en clases para la aplicación de reservas."""

import os

from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from rest_framework import viewsets  # ← IMPORTAR viewsets

from django_core.cabanas_apps_django.reservas.models import (
    Reserva,
)  # ← IMPORTAR el modelo

from .forms import ReservaForm
from .serializers import ReservaSerializer


def get_reserva(pk):
    """Obtiene una reserva específica por su clave primaria."""
    return Reserva.objects.get(pk=pk)


class ReservaViewSet(viewsets.ModelViewSet):
    """API REST para reservas"""

    queryset = Reserva.objects.all()  # pylint: disable=no-member
    serializer_class = ReservaSerializer


class ReservasDetailView(DetailView):
    """Muestra el detalle de una reserva específica."""

    model = Reserva
    template_name = "reservas/detalle.html"
    context_object_name = "reserva"


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
