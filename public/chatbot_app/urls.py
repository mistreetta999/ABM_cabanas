"""URLs de la aplicación Chatbot (pública)."""

from django.urls import path
from . import views

app_name = "chatbot_app"

urlpatterns = [
    # Página principal del chatbot
    path("", views.ChatbotHomeView.as_view(), name="chatbot_home"),

    # Endpoint para procesar mensajes
    path("send/", views.chatbot_send, name="chatbot_send"),

    # Endpoint para recibir respuestas (AJAX / API)
    path("response/", views.chatbot_response, name="chatbot_response"),

    # Endpoint para historial de conversaciones
    path("history/", views.ChatbotHistoryView.as_view(), name="chatbot_history"),
]
