"""URLs de la aplicación Cabañas, integradas con el sistema."""

from django.urls import path, include
from .views import (
    CabanaListView,
    CabanaCreateView,
    CabanaUpdateView,
    CabanaDeleteView,
    CabanaDetailView,
)

app_name = "cabanas"

urlpatterns = [
    # CRUD de cabañas
    path("", CabanaListView.as_view(), name="cabana_list"),
    path("nueva/", CabanaCreateView.as_view(), name="cabana_create"),
    path("<int:pk>/", CabanaDetailView.as_view(), name="cabana_detail"),
    path("<int:pk>/editar/", CabanaUpdateView.as_view(), name="cabana_update"),
    path("<int:pk>/borrar/", CabanaDeleteView.as_view(), name="cabana_delete"),

    # 🔗 Integraciones con otras apps del sistema
    path("alquileres/", include("alquileres.urls")),          # relación con alquileres
    path("reservas/", include("reservas.urls")),              # relación con reservas
    path("clientes/", include("clientes.urls")),              # relación con clientes
    path("facturas/", include("facturas.urls")),              # relación con facturas
    path("pagos/", include("pagos.urls")),                    # relación con pagos
    path("usuarios/", include("usuarios.urls")),              # relación con usuarios
    path("chatbot/", include("chatbot_app.urls")),            # relación con chatbot
    path("gestion/", include("gestion_cabanas.urls")),        # relación con gestión de cabañas
    path("interfaz/", include("interfaz_gestion_cabanas.urls")),  # relación con interfaz de gestión
    path("registros/", include("registros.urls")),            # relación con registros
    path("web/", include("web.urls")),                        # relación con web pública
]
