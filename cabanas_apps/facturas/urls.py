"""URLs de la aplicación Facturas, integradas con el sistema."""

from django.urls import path, include
from .views import (
    FacturaListView,
    FacturaCreateView,
    FacturaUpdateView,
    FacturaDeleteView,
    FacturaDetailView,
)

app_name = "facturas"

urlpatterns = [
    # CRUD de facturas
    path("", FacturaListView.as_view(), name="factura_list"),
    path("nueva/", FacturaCreateView.as_view(), name="factura_create"),
    path("<int:pk>/", FacturaDetailView.as_view(), name="factura_detail"),
    path("<int:pk>/editar/", FacturaUpdateView.as_view(), name="factura_update"),
    path("<int:pk>/borrar/", FacturaDeleteView.as_view(), name="factura_delete"),

    # 🔗 Integraciones con otras apps del sistema
    path("cabanas/", include("cabanas.urls")),                # relación con cabañas
    path("alquileres/", include("alquileres.urls")),          # relación con alquileres
    path("reservas/", include("reservas.urls")),              # relación con reservas
    path("clientes/", include("clientes.urls")),              # relación con clientes
    path("pagos/", include("pagos.urls")),                    # relación con pagos
    path("usuarios/", include("usuarios.urls")),              # relación con usuarios
    path("chatbot/", include("chatbot_app.urls")),            # relación con chatbot
    path("gestion/", include("gestion_cabanas.urls")),        # relación con gestión de cabañas
    path("