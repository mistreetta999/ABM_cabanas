"""Vistas de la app de alquileres."""
from typing import Any
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from cabanas_apps.reservas.models import Reserva
from .forms import AlquilerForm
from .models import Alquiler
def alquileres (_request)->Any:
    """ def alquileres"""
    return alquileres_list(_request)

def alquiler_buttons(view):
    """Construye los botones para las vistas de alquileres."""
    buttons = []
    if view == "list":
        buttons.append(
            {
                "text": "Crear alquiler",
                "url": reverse_lazy("alquileres:crear_alquiler"),
            }
        )
    elif view in {"form", "detail"}:
        buttons.append(
            {
                "text": "Volver",
                "url": reverse_lazy("alquileres:lista_alquileres"),
            }
        )
    return buttons


def crear_alquileres(request):
    """Vista para crear un nuevo alquiler."""
    if request.method == "POST":
        form = AlquilerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("alquileres:lista_alquileres")
    else:
        form = AlquilerForm()
    return render(request, "alquileres/crear.html", {"buttons": alquiler_buttons("form"), "form": form})


def reservas_list(request):
    """Vista para listar las reservas."""
    reservas = Reserva.objects.all()
    return render(request, "reservas_alquileres/reservas_list.html", {"reservas": reservas})


def alquileres_list(request):
    """Vista para listar los alquileres."""
    return AlquilerListView.as_view()(request)


class AlquilerListView(ListView):
    """Vista para listar los alquileres."""
    model = Alquiler
    template_name = "alquileres/panel.html"
    context_object_name = "alquileres"

    def get_context_data(self, **kwargs):
        """Agrega botones al listado."""
        context = super().get_context_data(**kwargs)
        context["buttons"] = alquiler_buttons("list")
        return context


class AlquilerCreateView(CreateView):
    """Vista para crear un nuevo alquiler."""
    model = Alquiler
    form_class = AlquilerForm
    template_name = "reservas_alquileres/alquiler_form.html"
    success_url = reverse_lazy("alquileres:lista_alquileres")

    def get_context_data(self, **kwargs):
        """Agrega botones al formulario."""
        context = super().get_context_data(**kwargs)
        context["buttons"] = alquiler_buttons("form")
        return context


class AlquilerUpdateView(UpdateView):
    """Vista para actualizar un alquiler existente."""
    model = Alquiler
    form_class = AlquilerForm
    template_name = "reservas_alquileres/alquiler_form.html"
    success_url = reverse_lazy("alquileres:lista_alquileres")

    def get_context_data(self, **kwargs):
        """Agrega botones al formulario."""
        context = super().get_context_data(**kwargs)
        context["buttons"] = alquiler_buttons("form")
        return context


class AlquilerDeleteView(DeleteView):
    """Vista para eliminar un alquiler."""
    model = Alquiler
    template_name = "reservas_alquileres/alquiler_confirm_delete.html"
    success_url = reverse_lazy("alquileres:lista_alquileres")

    def get_context_data(self, **kwargs):
        """Agrega botones a la confirmacion de borrado."""
        context = super().get_context_data(**kwargs)
        context["buttons"] = alquiler_buttons("detail")
        return context
