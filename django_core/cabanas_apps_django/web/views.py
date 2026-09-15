"""Vistas de la aplicación web principal."""

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Vistas secundarias requeridas por tu sistema
class WebHomeView(View):
    """web home"""

    def get(self, _request):
        """get"""
        return HttpResponse("Bienvenido al sistema de cabañas")


class WebContactView(View):
    """web contact"""

    def get(self, _request):
        """get"""
        return HttpResponse("Formulario de contacto")


class WebInfoView(View):
    """web info"""

    def get(self, _request):
        """get"""
        return HttpResponse("Información sobre el sistema")


class WebHelpView(View):
    """web help"""

    def get(self, _request):
        """get"""
        return HttpResponse("Sección de ayuda y soporte")


def ping(_request):
    """web ping"""
    return HttpResponse("pong")


def home(request):
    """Vista principal: Dashboard que despliega todos los módulos del sistema."""
    # Datos simulados de tus aplicaciones que luego vendrán de la base de datos
    estadisticas = {
        "total_cabanas": 8,
        "reservas_activas": 3,
        "clientes_registrados": 14,
        "ingresos_mes": "$120.000",
    }

    context = {"estadisticas": estadisticas}
    return render(request, "web/dashboard.html", context)


def reservas_list(_request):
    """Reservaslista."""
    return HttpResponse(
        "<h1>Módulo de Reservas y Alquileres</h1><p>Calendario y registro de estadías.</p><a href='/'>Volver al Panel</a>"
    )


def pagos_list(_request):
    """Módulo: Pagos y Facturas."""
    return HttpResponse(
        "<h1>Módulo de Finanzas</h1><p>Control de señas, pagos y facturación.</p><a href='/'>Volver al Panel</a>"
    )


from django.shortcuts import render


def home(request):
    """Carga el panel principal de control."""
    return render(request, "web/dashboard.html")


def cabanas_list(request):
    """Carga la interfaz de cabañas."""
    return render(request, "web/cabanas.html")


def reservas_list(request):
    """Carga la interfaz de reservas."""
    return render(request, "web/reservas.html")


def clientes_list(request):
    """Carga la interfaz de clientes."""
    return render(request, "web/clientes.html")


def pagos_list(request):
    """Carga la interfaz de pagos."""
    return render(request, "web/pagos.html")


def consultas_view(_request):
    """Vista temporal para la sección de consultas."""
    return HttpResponse(
        "<h1>Sección de Consultas en Desarrollo</h1><a href='/'>Volver al inicio</a>"
    )
