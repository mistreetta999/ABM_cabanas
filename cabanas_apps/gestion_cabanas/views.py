"""
Vistas de la aplicación Gestión de Cabañas.
Permite administrar las cabañas, su disponibilidad y estados.
"""

from django.views.generic import ListView, DetailView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from cabanas.models import Cabana
from reservas.models import Reserva


class GestionHomeView(TemplateView):
    """Vista principal del módulo de gestión de cabañas."""
    template_name = "gestion_cabanas/home.html"


class CabanaGestionListView(ListView):
    """Lista todas las cabañas disponibles para gestión."""
    model = Cabana
    template_name = "gestion_cabanas/cabana_list.html"
    context_object_name = "cabanas"


class CabanaGestionDetailView(DetailView):
    """Muestra el detalle de una cabaña en gestión."""
    model = Cabana
    template_name = "gestion_cabanas/cabana_detail.html"
    context_object_name = "cabana"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cabana = self.get_object()
        context["reservas"] = Reserva.objects.filter(cabana=cabana).order_by("-fecha_inicio")
        return context


class CabanaGestionUpdateView(UpdateView):
    """Permite actualizar datos de una cabaña."""
    model = Cabana
    template_name = "gestion_cabanas/cabana_form.html"
    fields = ["nombre", "capacidad", "precio_base", "estado", "descripcion"]
    success_url = reverse_lazy("gestion_cabanas:cabana_list")


def cambiar_estado_cabana(request, pk, nuevo_estado):
    """
    Función auxiliar para cambiar el estado de una cabaña desde la vista.
    """
    cabana = get_object_or_404(Cabana, pk=pk)
    estados_validos = ["disponible", "ocupada", "mantenimiento"]

    if nuevo_estado not in estados_validos:
        # Podrías mostrar un mensaje de error en el template
        return redirect("gestion_cabanas:cabana_detail", pk=pk)

    cabana.estado = nuevo_estado
    cabana.save()
    return redirect("gestion_cabanas:cabana_detail", pk=pk)
