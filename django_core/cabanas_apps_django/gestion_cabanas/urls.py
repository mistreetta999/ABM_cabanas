"""URLs de la aplicación Gestión de Cabañas, integradas con el sistema."""

from django.urls import path, include
from .views import (
    GestionCabanaListView,
    GestionCabanaCreateView,
    GestionCabanaUpdateView,
    GestionCabanaDeleteView,
    GestionCabanaDetailView,
)

app_name = "gestion_cabanas"

urlpatterns = [
    # CRUD de gestión de cabañas
    path("", GestionCabanaListView.as_view(), name="gestion_cabana_list"),
    path("nueva/", GestionCabanaCreateView.as_view(), name="gestion_cabana_create"),
    path("<int:pk>/", GestionCabanaDetailView.as_view(), name="gestion_cabana_detail"),
    path("<int:pk>/editar/", GestionCabanaUpdateView.as_view(), name="gestion_cabana_update"),
    path("<int:pk>/borrar/", GestionCabanaDeleteView.as_view(), name="gestion_cabana_delete"),

    # 🔗 Integraciones con otras apps del sistema
    path("cabanas/", include("cabanas.urls")),          # relación con cabañas
    path("alquileres/", include("alquileres.urls")),    # relación con alquileres
    path("reservas/", include("reservas.urls")),        # relación con reservas
    path("clientes/", include("clientes.urls")),        # relación con clientes
    path("facturas/", include("facturas.urls")),        # relación con facturas
    path("pagos/", include("pagos.urls")),              # relación con pagos
    path("usuarios/", include("usuarios.urls")),        # relación con usuarios
    path("chatbot/", include("chatbot_app.urls")),      # relación con chatbot
]
