"""
Vistas de la aplicación Interfaz de Gestión de Cabañas.
Sirven como punto central de navegación y administración del sistema.
"""

from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from cabanas.models import Cabana
from reservas.models import Reserva
from clientes.models import Cliente
from facturas.models import Factura
from pagos.models import Pago


class InterfazHomeView(TemplateView):
    """Vista principal de la interfaz de gestión."""
    template_name = "interfaz_gestion_cabanas/home.html"


class InterfazDashboardView(TemplateView):
    """Dashboard con métricas generales del sistema."""
    template_name = "interfaz_gestion_cabanas/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Métricas básicas
        context["total_cabanas"] = Cabana.objects.count()
        context["total_reservas"] = Reserva.objects.count()
        context["total_clientes"] = Cliente.objects.count()
        context["facturas_pendientes"] = Factura.objects.filter(estado="pendiente").count()
        context["pagos_registrados"] = Pago.objects.count()
        return context


class InterfazReportesView(TemplateView):
    """Vista para reportes generales del sistema."""
    template_name = "interfaz_gestion_cabanas/reportes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ejemplo de reporte: reservas activas
        context["reservas_activas"] = Reserva.objects.filter(estado="activa")
        # Ejemplo de reporte: facturas vencidas
        context["facturas_vencidas"] = Factura.objects.filter(estado="vencida")
        return context
