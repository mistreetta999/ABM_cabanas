"""URLs de la aplicación Chatbot, integradas con el sistema."""

from django.urls import path, include
from .views import (
    ChatbotHomeView,
    ChatbotInteractView,
    ChatbotHistoryView,
)

app_name = "chatbot_app"

urlpatterns = [
    # Vistas principales del chatbot
    path("", ChatbotHomeView.as_view(), name="chatbot_home"),
    path("interactuar/", ChatbotInteractView.as_view(), name="chatbot_interact"),
    path("historial/", ChatbotHistoryView.as_view(), name="chatbot_history"),

    # 🔗 Integraciones con otras apps del sistema
    path("cabanas/", include("cabanas.urls")),                # relación con cabañas
    path("alquileres/", include("alquileres.urls")),          # relación con alquileres
    path("reservas/", include("reservas.urls")),              # relación con reservas
    path("clientes/", include("clientes.urls")),              # relación con clientes
    path("facturas/", include("facturas.urls")),              # relación con facturas
    path("pagos/", include("pagos.urls")),                    # relación con pagos
    path("usuarios/", include("usuarios.urls")),              # relación con usuarios
    path("gestion/", include("gestion_cabanas.urls")),        # relación con gestión de cabañas
    path("interfaz/", include("interfaz_gestion_cabanas.urls")),  # relación con interfaz de gestión
    path("registros/", include("registros.urls")),            # relación con registros
    path("web/", include("web.urls")),                        # relación con web pública
]
