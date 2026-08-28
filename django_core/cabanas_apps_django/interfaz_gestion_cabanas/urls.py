"""URLs de la aplicación Interfaz de Gestión de Cabañas, integradas con el sistema."""

from django.urls import path, include
from .views import (
    InterfazHomeView,
    InterfazDashboardView,
    InterfazReportesView,
)

app_name = "interfaz_gestion_cabanas"

urlpatterns = [
    # Vistas principales de la interfaz
    path("", InterfazHomeView.as_view(), name="interfaz_home"),
    path("dashboard/", InterfazDashboardView.as_view(), name="interfaz_dashboard"),
    path("reportes/", InterfazReportesView.as_view(), name="interfaz_reportes"),

    # 🔗 Integraciones con otras apps del sistema
    path("cabanas/", include("cabanas.urls")),            # relación con cabañas
    path("alquileres/", include("alquileres.urls")),      # relación con alquileres
    path("reservas/", include("reservas.urls")),          # relación con reservas
    path("clientes/", include("clientes.urls")),          # relación con clientes
    path("facturas/", include("facturas.urls")),          # relación con facturas
    path("pagos/", include("pagos.urls")),                # relación con pagos
    path("usuarios/", include("usuarios.urls")),          # relación con usuarios
    path("chatbot/", include("chatbot_app.urls")),        # relación con chatbot
    path("gestion/", include("gestion_cabanas.urls")),    # relación con gestión de cabañas
]
