"""URLs de la aplicación Alquileres, integradas con el resto del sistema."""

from django.urls import path, include
from .views import (
    AlquilerListView,
    AlquilerCreateView,
    AlquilerUpdateView,
    AlquilerDeleteView,
    AlquilerDetailView,
)

app_name = "alquileres"

urlpatterns = [
    # CRUD de alquileres
    path("", AlquilerListView.as_view(), name="alquiler_list"),
    path("nuevo/", AlquilerCreateView.as_view(), name="alquiler_create"),
    path("<int:pk>/", AlquilerDetailView.as_view(), name="alquiler_detail"),
    path("<int:pk>/editar/", AlquilerUpdateView.as_view(), name="alquiler_update"),
    path("<int:pk>/borrar/", AlquilerDeleteView.as_view(), name="alquiler_delete"),

    # 🔗 Integraciones con otras apps del sistema
    path("cabanas/", include("cabanas.urls")),        # relación con cabañas
    path("reservas/", include("reservas.urls")),      # relación con reservas
    path("clientes/", include("clientes.urls")),      # relación con clientes
    path("pagos/", include("pagos.urls")),            # relación con pagos
    path("usuarios/", include("usuarios.urls")),      # relación con usuarios
]
