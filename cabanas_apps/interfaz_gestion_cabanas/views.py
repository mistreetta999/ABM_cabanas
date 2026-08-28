"""
Vistas de la aplicación Interfaz de Gestión de Cabañas.
Permite mostrar la interfaz visual para administración de cabañas.
"""

from django.views.generic import TemplateView, ListView, DetailView
from cabanas.models import Cabana
from reservas.models import Reserva
from interfaz_gestion_cabanas.handles import obtener_cabanas_disponibles, resumen_cabana


class InterfazHomeView(TemplateView):
    """Vista principal de la interfaz de gestión."""
    template_name = "interfaz_gestion_cabanas/home.html"


class InterfazCabanaListView(ListView):
    """Lista todas las cabañas disponibles en la interfaz."""
    model = Cabana
    template_name = "interfaz_gestion_cabanas/cabana_list.html"
    context_object_name = "cabanas"

    def get_queryset(self):
        # Usamos el handler para obtener solo las disponibles
        return obtener_cabanas_disponibles()


class InterfazCabanaDetailView(DetailView):
    """Muestra el detalle de una cabaña en la interfaz."""
    model = Cabana
    template_name = "interfaz_gestion_cabanas/cabana_detail.html"
    context_object_name = "cabana"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cabana = self.get_object()
        context["resumen"] = resumen_cabana(cabana.id)
        context["reservas"] = Reserva.objects.filter(cabana=cabana).order_by("-fecha_inicio")
        return context
