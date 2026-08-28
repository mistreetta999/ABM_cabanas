"""URLs de la aplicación Registros."""

from django.urls import path, include
from .views import (
    RegistroListView,
    RegistroDetailView,
)

app_name = "registros"

urlpatterns = [
    # Vistas principales de registros
    path("", RegistroListView.as_view(), name="registro_list"),
    path("<int:pk>/", RegistroDetailView.as_view(), name="registro_detail"),

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
    path("web/", include("web.urls")),                        # relación con web pública
]
