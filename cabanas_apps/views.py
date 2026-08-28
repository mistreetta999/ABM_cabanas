"""
Vistas generales de la carpeta cabanas_apps.
Sirven como integración y acceso rápido a las distintas apps del sistema.
"""

from django.shortcuts import render
from django.views.generic import TemplateView
from cabanas.models import Cabana
from reservas.models import Reserva
from clientes.models import Cliente


class DashboardView(TemplateView):
    """Vista principal del panel de gestión."""
    template_name = "cabanas_apps/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_cabanas"] = Cabana.objects.count()
        context["total_reservas"] = Reserva.objects.count()
        context["total_clientes"] = Cliente.objects.count()
        context["reservas_pendientes"] = Reserva.objects.filter(estado="pendiente").count()
        return context


def resumen(request):
    """
    Vista personalizada que muestra un resumen rápido del sistema.
    """
    data = {
        "cabanas": Cabana.objects.count(),
        "reservas": Reserva.objects.count(),
        "clientes": Cliente.objects.count(),
    }
    return render(request, "cabanas_apps/resumen.html", data)
