"""URLs de la aplicación Alquileres, integradas con el sistema."""

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
    path("cabanas/", include("cabanas.urls")),                # relación con cabañas
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
