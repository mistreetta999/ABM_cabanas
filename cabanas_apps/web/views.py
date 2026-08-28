"""
Vistas de la aplicación Web.
Se encargan de mostrar las páginas públicas del sistema.
"""

from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from cabanas.models import Cabana
from reservas.models import Reserva


class HomeView(TemplateView):
    """Página principal del sitio web."""
    template_name = "web/home.html"


class ContactoView(TemplateView):
    """Página de contacto."""
    template_name = "web/contacto.html"


class NosotrosView(TemplateView):
    """Página de información sobre la empresa."""
    template_name = "web/nosotros.html"


class CabanaListView(ListView):
    """Lista todas las cabañas disponibles para mostrar en la web pública."""
    model = Cabana
    template_name = "web/cabana_list.html"
    context_object_name = "cabanas"


class CabanaDetailView(DetailView):
    """Muestra el detalle de una cabaña específica."""
    model = Cabana
    template_name = "web/cabana_detail.html"
    context_object_name = "cabana"


def disponibilidad(request):
    """
    Vista personalizada para consultar disponibilidad de cabañas.
    Filtra reservas y muestra cuáles están libres en un rango de fechas.
    """
    cabanas_disponibles = Cabana.objects.all()
    reservas = Reserva.objects.all()
    return render(request, "web/disponibilidad.html", {
        "cabanas": cabanas_disponibles,
        "reservas": reservas
    })
