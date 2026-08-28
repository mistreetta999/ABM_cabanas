"""URLs de la aplicación Pagos."""

from django.urls import path, include
from .views import (
    PagoListView,
    PagoCreateView,
    PagoDetailView,
    PagoUpdateView,
    PagoDeleteView,
)

app_name = "pagos"

urlpatterns = [
    # CRUD de pagos
    path("", PagoListView.as_view(), name="pago_list"),
    path("nuevo/", PagoCreateView.as_view(), name="pago_create"),
    path("<int:pk>/", PagoDetailView.as_view(), name="pago_detail"),
    path("<int:pk>/editar/", PagoUpdateView.as_view(), name="pago_update"),
    path("<int:pk>/borrar/", PagoDeleteView.as_view(), name="pago_delete"),

    # 🔗 Integraciones con otras apps del sistema
    path("cabanas/", include("cabanas.urls")),                # relación con cabañas
    path("alquileres/", include("alquileres.urls")),          # relación con alquileres
    path("reservas/", include("reservas.urls")),              # relación con reservas
    path("clientes/", include("clientes.urls")),              # relación con clientes
    path("facturas/", include("facturas.urls")),              # relación con facturas
    path("usuarios/", include("usuarios.urls")),              # relación con usuarios
    path("chatbot/", include("chatbot_app.urls")),            # relación con chatbot
    path("gestion/", include("gestion_cabanas.urls")),        # relación con gestión de cabañas
    path("interfaz/", include("interfaz_gestion_cabanas.urls")),  # relación con interfaz de gestión
    path("registros/", include("registros.urls")),            # relación con registros
    path("web/", include("web.urls")),                        # relación con web pública
]
