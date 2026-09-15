"""URLs de la aplicación Chatbot, integradas con el sistema."""

from django.urls import include, path

from . import chatbot_panel
from .views import ChatbotHistoryView, ChatbotHomeView, ChatbotInteractView

app_name = "chatbot_app"  # pylint: disable=invalid-name

urlpatterns = [
    # Página principal del chatbot
    path("", ChatbotHomeView.as_view(), name="chatbot_home"),
    path("panel/", chatbot_panel.chatbot_panel, name="chatbot_panel"),
    # Interacción con el chatbot
    path("interactuar/", ChatbotInteractView.as_view(), name="chatbot_interact"),
    # Historial de conversaciones
    path("historial/", ChatbotHistoryView.as_view(), name="chatbot_history"),
    # 🔗 Integraciones con otras apps del sistema
    path("cabanas/", include("cabanas.urls")),  # relación con cabañas
    path("alquileres/", include("alquileres.urls")),  # relación con alquileres
    path("reservas/", include("reservas.urls")),  # relación con reservas
    path("clientes/", include("clientes.urls")),  # relación con clientes
    path("pagos/", include("pagos.urls")),  # relación con pagos
    path("usuarios/", include("usuarios.urls")),  # relación con usuarios
    path("chatbot/history/", ChatbotHistoryView.as_view(), name="chatbot_history"),
]
