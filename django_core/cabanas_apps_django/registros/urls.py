"""URLs de la aplicación Registros, integradas con el sistema."""

from django.urls import path, include
from .views import (
    RegistroListView,
    RegistroCreateView,
    RegistroUpdateView,
    RegistroDeleteView,
    RegistroDetailView,
)

app_name = "registros"

urlpatterns = [
    # CRUD de registros
    path("", RegistroListView.as_view(), name="registro_list"),
    path("nuevo/", RegistroCreateView.as_view(), name="registro_create"),
    path("<int:pk>/", RegistroDetailView.as_view(), name="registro_detail"),
    path("<int:pk>/editar/", RegistroUpdateView.as_view(), name="registro_update"),
    path("<int:pk>/borrar/", RegistroDeleteView.as_view(), name="registro_delete"),

    # 🔗 Integraciones con otras apps del sistema
    path("cabanas/", include("cabanas.urls")),                # relación con cabañas
    path("alquileres/", include("alquileres.urls")),          # relación con alquileres
    path("reservas/", include("reservas.urls")),              # relación con reservas
    path("clientes/", include("clientes.urls")),              # relación con clientes
    path("facturas/", include("facturas.urls")),              # relación con facturas
    path("pagos/", include("pagos.urls")),                    # relación con pagos
    path("usuarios/", include("usuarios.urls")),              # relación con usuarios
    path("chatbot/", include("chatbot_app.urls")),            # relación con chatbot
    path("gestion/", include("gestion_cabanas.urls")),        # relación con gestión de cabañas
    path("interfaz/", include("interfaz_gestion_cabanas.urls")),  # relación con interfaz de gestión
]
